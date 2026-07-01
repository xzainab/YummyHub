def recipes_categorize():
    """
     Categorizes a given recipe into Breakfast, Lunch, Dinner, or Dessert.
     Done by Zainab Abdulwahab
    """
    categorize = ['Breakfast', 'Lunch', 'Dinner', 'Dessert']
    print('\n categorize options: Breakfast, Lunch, Dinner, Dessert)
    while True:
        recipe_categorize = input("Enter recipe categorize: ").strip().lower()
        if recipe_categorize in categorize:
            recipe_categorize = recipe_categorize.capitalize() 
            break 
        else:
            print('Invalid Input! Please enter a valid categorize: Breakfast, Lunch, Dinner or Dessert.')


    