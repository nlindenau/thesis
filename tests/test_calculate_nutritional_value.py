from src.calculate_nutritional_value import get_nutritional_value, create_nutritional_label_for_ingredient
from src.example_values import APPLE_NUTRITIONAL_FACTS_PER_100G

def test_get_nutritional_value():
    result = get_nutritional_value(serving=600, nutritional_value_per_100g=100)
    assert result == 600

def test_create_nutritional_label_for_ingredient():
    result = create_nutritional_label_for_ingredient(serving=600, 
                                                     nutritional_values_per_100g=APPLE_NUTRITIONAL_FACTS_PER_100G)
    assert result == {'calories': 312.0, 
                      'fat': 1.02, 
                      'saturated_fat': 0.17, 
                      'carbohydrates': 82.8, 
                      'sugars': 62.4, 
                      'sodium': 6.0, 
                      'protein': 1.56}