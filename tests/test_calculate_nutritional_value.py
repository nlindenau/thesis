from src.calculate_nutritional_value import get_nutritional_value

def test_nutritional_value():
    result = get_nutritional_value(serving=600, nutritional_value_per_100g=100)
    assert result == 600