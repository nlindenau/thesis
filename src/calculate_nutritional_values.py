def get_nutritional_value(serving, nutritional_value_per_100g):
    '''Takes in size of the serving of the ingredient and 
    a nutritional value (eg. calories) per 100 g.'''
    nutritional_value = round(nutritional_value_per_100g * (serving / 100), 2)
    return nutritional_value

def create_nutrition_facts_for_ingredient(serving, nutritional_values_per_100g):
    '''Takes in size of the serving of the ingredient and 
    a dictionary of nutritional facts per 100g, 
    returns a dictionary of nutritional values for the entire serving.'''
    nutrition_facts = {}
    for nutrient in nutritional_values_per_100g:
        nutrient_amount_per_100g = nutritional_values_per_100g[nutrient]
        nutrient_amount_per_serving = get_nutritional_value(serving, nutrient_amount_per_100g)
        nutrition_facts.update({nutrient: nutrient_amount_per_serving})

    return nutrition_facts

def sum_nutrition_facts(label_a, label_b):
    summarized_nutrition_facts = {}

    for nutrient_1, value_1 in label_a.items():
            value_2 = label_b[nutrient_1]
            sum_of_nutrient_values = value_1 + value_2
            rounded_sum_of_nutrient_values = round(sum_of_nutrient_values, 2)
            summarized_nutrition_facts.update({nutrient_1: rounded_sum_of_nutrient_values})

    return summarized_nutrition_facts

def pretty_print_label(nutritional_label):
    print("Nutrition Facts (total)")
    for nutrient in nutritional_label:
        print(nutrient, nutritional_label[nutrient])