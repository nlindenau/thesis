def get_nutritional_value(serving, nutritional_value_per_100g):
    '''Takes in size of the serving of the ingredient and 
    a nutritional value (eg. calories) per 100 g.'''
    nutritional_value = round(nutritional_value_per_100g * (serving / 100), 2)
    return nutritional_value

def create_nutritional_label_for_ingredient(serving, nutritional_values_per_100):
    '''Takes in size of the serving of the ingredient and 
    a dictionary of nutritional facts per 100g, 
    returns a dictionary of nutritional values for the entire serving.'''
    nutritional_label = {}
    for nutrient in nutritional_values_per_100:
        nutrient_amount_per_100g = nutritional_values_per_100[nutrient]
        nutrient_amount_per_serving = get_nutritional_value(serving, nutrient_amount_per_100g)
        nutritional_label.update({nutrient: nutrient_amount_per_serving})

    return nutritional_label

def display_nutritional_label(nutritional_label):
    for nutrient in nutritional_label:
        print(nutrient, nutritional_label[nutrient])