from typing import TypedDict

class NutritionFactsLabel(TypedDict):
    name: str   
    energy: float
    fat: float
    saturatedFat: float
    carbohydrates: float
    sugars: float
    protein: float
    salt: float
