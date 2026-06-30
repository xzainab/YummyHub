import pandas as pd
import os
import uuid
from datetime import date, datetime, timedelta

def new_recipe(data, filename):
     """Adding a new recipe into the recipe csv file
        Done by Zainab Abdulwahab 
     """
    try:
        # convert the passed data into a DataFrame
        dataframe = pd.DataFrame(data)
        
        # Check if the file already exists on your system using os.path.exists
        file_exists = os.path.exists(filename)
        
        if file_exists:
            # Append data: 'a' mode, turn off headers so columns aren't duplicated in mid-file
            dataframe.to_csv(filename, mode = 'a', header = False, index = False)
            print(f'file {filename} has been successfully updated!')

        
        else:
            # Create new file: 'w' mode (default), write the header columns
            dataframe.to_csv(filename, mode = 'w', header = True, index = False)
            print(f'file {filename} has been successfully created!')
    except:

    



    # add new recipe
    print("\n=== Add a New Recipe ===")
    recipe_id = str(uuid.uuid4())[:6]  # Creates unique id
    recipe_name = input("Enter recipe name: ")

    # ingredients list 
    ingredients = []
    print('\nPlease enter ingredients below (separated by commas OR one by one), then type "done" when finished:')

    while True:
        recipe_ingredient = input('Add ingredient(s): ').strip()
    
        if recipe_ingredient.lower() == 'done':
            break
        
        if not recipe_ingredient:
            print('Input cannot be blank! Please enter an ingredient.')
            continue
        
    # 3. Split by commas, clean spaces, and add them to the ingredients list
    items = [item.strip() for item in recipe_ingredient.split(',') if item.strip()]
    ingredients.extend(items)

    recipe_book = {recipe_name: ingredients}
    print(f"\nSaved! {recipe_name}: {recipe_book[recipe_name]}")


    # preparing time 