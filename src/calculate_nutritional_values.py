def get_nutritional_value(serving, nutritional_value_per_100g):
    '''Calculate nutritional value for a serving.'''
    nutritional_value = nutritional_value_per_100g * (serving / 100)
    return nutritional_value

def create_nutrition_facts_for_ingredient(serving, nutritional_values_per_100g):
    '''Get nutrition facts dictionary.

    Keyword arguments:
    serving -- size of a serving in g.
    nutritional_value_per_100g -- nutritional value per 100g.
    '''
    nutrition_facts = {}
    for nutrient in nutritional_values_per_100g:
        nutrient_amount_per_100g = nutritional_values_per_100g[nutrient]
        nutrient_amount_per_serving = get_nutritional_value(serving, nutrient_amount_per_100g)
        nutrition_facts.update({nutrient: nutrient_amount_per_serving})

    return nutrition_facts

def sum_nutrition_facts(label_a, label_b):
    '''Create a summarized nutrition facts label 
    for the entire serving.
    '''
    summarized_nutrition_facts = {}

    for nutrient_1, value_1 in label_a.items():
            value_2 = label_b[nutrient_1]
            sum_of_nutrient_values = value_1 + value_2
            rounded_sum_of_nutrient_values = round(sum_of_nutrient_values, 2)
            summarized_nutrition_facts.update({nutrient_1: rounded_sum_of_nutrient_values})

    return summarized_nutrition_facts

def pretty_print_label(nutrition_facts_label):
    '''Pretty print a nutrition facts label.'''
    print("Nutrition Facts (total)")
    for nutrient in nutrition_facts_label:
        print(nutrient, nutrition_facts_label[nutrient])