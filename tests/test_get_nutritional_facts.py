from src.get_nutritional_facts import get_nutritional_facts

def test_nutritional_facts():
    result = get_nutritional_facts()
    assert result == {"calories": 100, "fat": 9, "saturated_fat": 1, "sodium": 7, "protein": 4}