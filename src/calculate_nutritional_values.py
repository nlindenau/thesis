def get_nutritional_value(serving, nutritional_value_per_100g):
    '''Calculate nutritional value for a serving.'''
    nutritional_value = nutritional_value_per_100g * (serving / 100)
    return nutritional_value