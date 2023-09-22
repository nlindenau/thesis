from calculate_nutritional_value import create_nutritional_label_for_ingredient, display_nutritional_label

EXAMPLE_APPLE_NUTRITIONAL_FACTS_PER_100G = {"calories": 52,
                                   "fat": 0.17,
                                   "saturated_fat":0.028,
                                   "carbohydrates":13.8,
                                   "sugars":10.4,
                                   "sodium":1,
                                   "protein":0.26,
                                   }


def main():
    my_label = create_nutritional_label_for_ingredient(600, EXAMPLE_APPLE_NUTRITIONAL_FACTS_PER_100G)
    display_nutritional_label(my_label)
    print(my_label)

main()