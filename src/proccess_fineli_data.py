def print_all_food_names(fineli_response, language="en"):
    '''Pretty print Fineli response basic data.

    Keyword arguments:
    fineli_response -- JSON of the Fineli API response.
    language -- search language (default en)
    '''
    print("Food ID - Food name")
    for element in fineli_response:
        print(element["id"], "-" ,element["name"][language])

def get_list_of_nutrition_values(fineli_response, language="en"):
    '''Clean up Fineli response to get only the EU-law required information for nutrition declaration per item.

    Keyword arguments:
    fineli_response -- JSON of the Fineli API response.
    language -- search language (default en)
    '''
    processed_response = []

    for element in fineli_response:
        #Create a shortened version of an entry from fineli response
        new_item = {
            "name": element["name"][language],        
            "energy": element["energyKcal"],
            "fat": element["fat"],
            "saturatedFat": element["saturatedFat"],
            "carbohydrates": element["carbohydrate"],
            "sugars": element["sugar"],
            "protein": element["protein"],
            "salt": element["salt"]
        }
        processed_response.append(new_item) 
    
    return (processed_response)
