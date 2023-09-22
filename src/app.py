from calculate_nutritional_values import create_nutritional_label_for_ingredient, display_nutritional_label, sum_nutritional_facts
from example_values import APPLE_NUTRITIONAL_FACTS_PER_100G, CREAM_CHEESE_NUTRITIONAL_FACTS_PER_100G, HONEY_NUTRITIONAL_FACTS_PER_100G

def main():
    my_apple_label = create_nutritional_label_for_ingredient(600, APPLE_NUTRITIONAL_FACTS_PER_100G)
    my_cheese_label = create_nutritional_label_for_ingredient(200, CREAM_CHEESE_NUTRITIONAL_FACTS_PER_100G)
    my_honey_label = create_nutritional_label_for_ingredient(20, HONEY_NUTRITIONAL_FACTS_PER_100G)
    display_nutritional_label(my_apple_label)
    display_nutritional_label(my_cheese_label)
    display_nutritional_label(my_honey_label)

    full_meal = sum_nutritional_facts(my_apple_label, my_cheese_label)
    display_nutritional_label(full_meal)
    print(full_meal)

main()