def shopping_list ():
    """
       Creat a shopping list depending on the selected recipes
       Done by Kawthar Hussain
    """
    # df, size = load_recipes()
    # if size == 0:
    #     print("\nThere are no recipes available!")
    #     return
    # shopping_list = []
    # print("\nPlease enter recipes below (separated by commas OR one by one), then type 'done' when finished:")
    # while True:
    #     shopping = input("Add recipe(s): ").strip()
    #     if shopping.lower() == 'done':
    #         break
    #     if not shopping:
    #         print("Input cannot be blank! Please enter an ingredient.")
    #         continue
    #     selected_recipes = [r.strip().lower() for r in shopping.split(',')]
    #     for recipe in selected_recipes:
    #         # Find the recipe row in the DataFrame
    #         match = df[df['name'].str.lower() == recipe]
            
    #         if not match.empty:
    #             # Get the ingredients string and split it by your separator '; '
    #             ingredients_str = match.iloc[0]['ingredients']
    #             ingredients_list = [i.strip() for i in ingredients_str.split(';')]
                
    #             for ingredient in ingredients_list:
    #                 if ingredient not in final_shopping_list:
    #                     final_shopping_list.append(ingredient)
    #             print(f" Added ingredients for '{recipe}'")
    #         else:
    #             print(f" '{recipe}' not found in recipes.")

    # print("\n=== YOUR FINAL SHOPPING LIST ===")
    # for item in final_shopping_list:
    #     print(f" {item}")
    
    shopping_list = []

    print("\nPlease enter each recipe below, then type 'print' when finished to print the shopping list:")

    while True:
        recipe_name = input("Enter recipe name (or type 'print') to print the shopping list: ").strip()

        if recipe_name.lower() == 'print':
            break

        finding_recipe = allRecipes[allRecipes['name'] == recipe_name]

        if finding_recipe.empty:
            print(f"\n {recipe_name} not found.")
            continue

        ingredients = finding_recipe.iloc[0]['ingredients'].split(";")

        for item in ingredients:
            item = item.strip()

            if item not in shopping_list:
                shopping_list.append(item)

        print("\nItems added to the shopping list.")

    if len(shopping_list) == 0:
        print("\n----- SHOPPING LIST IS EMPTY -----")
    else:
        print("\n========== SHOPPING LIST ==========")

        for item in shopping_list:
            print("-", item)