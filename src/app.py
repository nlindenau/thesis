from calculate_nutritional_values import create_nutritional_label_for_ingredient, display_nutritional_label
from example_values import APPLE_NUTRITIONAL_FACTS_PER_100G, CREAM_CHEESE_NUTRITIONAL_FACTS_PER_100G, HONEY_NUTRITIONAL_FACTS_PER_100G

def main():
    my_label = create_nutritional_label_for_ingredient(600, APPLE_NUTRITIONAL_FACTS_PER_100G)
    display_nutritional_label(my_label)
    print(my_label)

main()