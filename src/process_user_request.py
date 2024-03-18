from src.call_fineli_api import run_fineli_workflow
from src.fuzzy_match_fineli_response import run_fuzzy_matching_workflow
from src.calculate_nutritional_values import get_nutritional_value
from copy import deepcopy



def get_list_of_ingredients(nutrition_facts_label):
    '''Get list of ingredient names from a nutrition label.

    Keyword arguments:
    nutrition_facts_label -- Dictionary with nutrition facts.
    '''
    ingredients_list = []

    for element in nutrition_facts_label:
        ingredient_name = element["name"]
        ingredients_list.append(ingredient_name)

    return ingredients_list

def get_ingredients_facts_from_fineli(list_of_ingredients):
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

def calculate_nutiritonal_values_for_servings(user_request, processed_fineli_response):
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
            saturated_fat = get_nutritional_value(original_element["weight"], fineli_element["saturatedFat"])
            carbohydrates = get_nutritional_value(original_element["weight"], fineli_element["carbohydrates"])
            sugars = get_nutritional_value(original_element["weight"], fineli_element["sugars"])
            protein = get_nutritional_value(original_element["weight"], fineli_element["protein"])
            salt = get_nutritional_value(original_element["weight"], fineli_element["salt"])
            new_element = {"name": original_element["name"],
                           "energy": energy,
                           "fat":  fat,
                           "saturated_fat": saturated_fat,
                           "carbohydrates": carbohydrates,
                           "sugars": sugars,
                           "protein": protein,
                           "salt": salt, 
                           }
            list_with_values_per_serving.append(new_element)
            
    return list_with_values_per_serving
        
def sum_nutritional_values_for_all_ingredients(list_with_values_per_serving):
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

    final_nutrition_facts_label = {"energy": round(total_energy, 2), 
                                   "fat": round(total_fat, 2), 
                                   "saturated_fat": round(total_saturated_fat, 2),
                                   "carbohydrates": round(total_carbohydrates, 2), 
                                   "sugars": round(total_sugars, 2), 
                                   "protein": round(total_protein, 2),
                                   "salt": round(total_salt, 2),
                                   }
    
    return(final_nutrition_facts_label)

def create_full_response(list_of_ingredients, fineli_response_names, final_label):
    response = deepcopy(final_label)

    response["fineli_returned_ingredients"] = fineli_response_names
    response["original_ingredients"] = list_of_ingredients

    return(response)

