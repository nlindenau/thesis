from src.get_nutritional_facts import get_nutritional_facts

def test_nutritional_facts():
    result = get_nutritional_facts()
    assert result == [1, 2, 3, 4]