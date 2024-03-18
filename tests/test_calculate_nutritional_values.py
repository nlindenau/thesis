from src.calculate_nutritional_values import get_nutritional_value, create_nutrition_facts_for_ingredient, sum_nutrition_facts
from example_values import APPLE_NUTRITIONAL_FACTS_PER_100G, CREAM_CHEESE_NUTRITIONAL_FACTS_PER_100G

def test_get_nutritional_value():
    result = get_nutritional_value(serving=600, nutritional_value_per_100g=100)
    assert result == 600

def test_create_nutrition_facts_for_ingredient():
    result = create_nutrition_facts_for_ingredient(serving=600, 
                                                     nutritional_values_per_100g=APPLE_NUTRITIONAL_FACTS_PER_100G)
    assert result == {'calories': 312.0, 
                      'fat': 1.02, 
                      'saturated_fat': 0.17, 
                      'carbohydrates': 82.8, 
                      'sugars': 62.4, 
                      'sodium': 6.0, 
                      'protein': 1.56}
    
def test_sum_nutrition_facts():
    result = sum_nutrition_facts(APPLE_NUTRITIONAL_FACTS_PER_100G, CREAM_CHEESE_NUTRITIONAL_FACTS_PER_100G)
    assert result == {'calories': 395.0, 
                      'fat': 33.67, 
                      'saturated_fat': 19.73, 
                      'carbohydrates': 18.36, 
                      'sugars': 14.16, 
                      'sodium': 369.0, 
                      'protein': 6.05}