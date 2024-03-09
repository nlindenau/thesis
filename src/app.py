from calculate_nutritional_values import create_nutrition_facts_for_ingredient, pretty_print_label, sum_nutrition_facts
from example_values import APPLE_NUTRITIONAL_FACTS_PER_100G, CREAM_CHEESE_NUTRITIONAL_FACTS_PER_100G, HONEY_NUTRITIONAL_FACTS_PER_100G

def main():
    my_apple_label = create_nutrition_facts_for_ingredient(600, APPLE_NUTRITIONAL_FACTS_PER_100G)
    my_cheese_label = create_nutrition_facts_for_ingredient(200, CREAM_CHEESE_NUTRITIONAL_FACTS_PER_100G)

    full_meal = sum_nutrition_facts(my_apple_label, my_cheese_label)
    pretty_print_label(full_meal)
    #print(full_meal)

main()