from nutrition_facts import NutritionFactsLabel
from proccess_fineli_data import run_fineli_workflow, run_fuzzy_matching_workflow

def get_list_of_ingredients(nutrition_facts_label: NutritionFactsLabel) -> list:
    '''Get list of ingredient names from a nutrition label.

    Keyword arguments:
    nutrition_facts_label -- Dictionary with nutrition facts.
    '''
    ingredients_list = []

    for element in nutrition_facts_label:
        ingredient_name = element["name"]
        ingredients_list.append(ingredient_name)

    return ingredients_list

def get_ingredients_facts_from_fineli(list_of_ingredients: list) -> list:
    '''Get nutrition facts for each ingredient by calling Fineli. The returned values are
      for the fuzzy matched ingredients from Fineli.

    Keyword arguments:
    list_of_ingredients -- List of ingredient names

    See also:
    fuzzy_match_fineli_response.run_fuzzy_matching_workflow
    '''
    final_list = []

    for element in list_of_ingredients:
        fineli_response = run_fineli_workflow(element)
        most_similar_response = run_fuzzy_matching_workflow(fineli_response, element)
        final_list.append(most_similar_response)

    return final_list

def get_nutritional_value(serving: float, nutritional_value_per_100g: float) -> float:
    '''Calculate nutritional value for a serving.'''
    nutritional_value = nutritional_value_per_100g * (serving / 100)
    return nutritional_value

def calculate_nutiritonal_values_for_servings(user_request: list, processed_fineli_response: NutritionFactsLabel) -> list:
    '''Get nutrition facts for a serving of each ingredient.

    Keyword arguments:
    user_request -- Original user request
    processed_fineli_response -- Cleaned up response from Fineli containing only EU-law required information.

    See also:
    process_fineli_data.get_list_of_nutrition_values
    '''
    list_with_values_per_serving = []

    for original_element, fineli_element in zip(user_request, processed_fineli_response):
            energy = get_nutritional_value(original_element["weight"], fineli_element["energy"])
            fat = get_nutritional_value(original_element["weight"], fineli_element["fat"])
            saturated_fat = get_nutritional_value(original_element["weight"], fineli_element["saturated_fat"])
            carbohydrates = get_nutritional_value(original_element["weight"], fineli_element["carbohydrates"])
            sugars = get_nutritional_value(original_element["weight"], fineli_element["sugars"])
            protein = get_nutritional_value(original_element["weight"], fineli_element["protein"])
            salt = get_nutritional_value(original_element["weight"], fineli_element["salt"])
            new_element =  NutritionFactsLabel({"name": original_element["name"],
                           "energy": energy,
                           "fat":  fat,
                           "saturated_fat": saturated_fat,
                           "carbohydrates": carbohydrates,
                           "sugars": sugars,
                           "protein": protein,
                           "salt": salt
                           })
            list_with_values_per_serving.append(new_element)
            
    return list_with_values_per_serving
        
def sum_nutritional_values_for_all_ingredients(list_with_values_per_serving: list) -> NutritionFactsLabel:
    '''Get nutrition facts for the entire meal.

    Keyword arguments:
    list_with_values_per_serving - list of ingredients with nutrition facts calculated for the entire serving.
    '''
    total_energy = 0
    total_fat = 0
    total_saturated_fat = 0
    total_carbohydrates = 0
    total_sugars = 0
    total_protein = 0
    total_salt = 0

    for element in list_with_values_per_serving:
        total_energy += element["energy"]
        total_fat += element["fat"]
        total_saturated_fat += element["saturated_fat"]
        total_carbohydrates += element["carbohydrates"]
        total_sugars += element["sugars"]
        total_protein += element["protein"]
        total_salt += element["salt"]

    final_nutrition_facts_label = NutritionFactsLabel({"energy": round(total_energy, 2), 
                                   "fat": round(total_fat, 2), 
                                   "saturated_fat": round(total_saturated_fat, 2),
                                   "carbohydrates": round(total_carbohydrates, 2), 
                                   "sugars": round(total_sugars, 2), 
                                   "protein": round(total_protein, 2),
                                   "salt": round(total_salt, 2),
                                   })
    
    return(final_nutrition_facts_label)

def create_full_response(list_of_ingredients: list, fineli_response_names: list, final_label: NutritionFactsLabel):
    response = {}
    response["nutrition_facts"] = final_label
    response["fineli_returned_ingredients"] = fineli_response_names
    response["original_ingredients"] = list_of_ingredients

    return(response)

def run_request_processing_workflow(request_body):
    request_body = sorted(request_body, key=lambda d: d['name'])

    ingredients = get_list_of_ingredients(request_body)
    ingredients.sort()

    fineli_list = get_ingredients_facts_from_fineli(ingredients)
    fineli_list = sorted(fineli_list, key=lambda d: d['name'])

    fineli_ingredients = get_list_of_ingredients(fineli_list)
    fineli_ingredients.sort()

    nutritional_values_for_servings = calculate_nutiritonal_values_for_servings(request_body, fineli_list)

    final_label = sum_nutritional_values_for_all_ingredients(nutritional_values_for_servings)

    response = create_full_response(ingredients, fineli_ingredients, final_label)

    return response