def get_nutritional_value(serving, nutritional_value_per_100g):
    '''Takes in size of the serving of the ingredient and a nutritional value (eg. calories) per 100 g.'''
    nutritional_value = nutritional_value_per_100g * (serving / 100)
    return nutritional_value