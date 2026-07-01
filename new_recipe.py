import pandas as pd
import os
import uuid
from datetime import timedelta

def add_new_recipe():
    """
    Adding a new recipe into the recipe csv file
    Done by Zainab Abdulwahab 
    """
    file_name = 'recipes.csv'

    # 1. Add new recipe name
    print("\n=== Add a New Recipe ===")
    recipe_id = str(uuid.uuid4())[:6]  # Creates unique id
    recipe_name = input("Enter recipe name: ").strip()

    # 2. Ingredients list 
    ingredients = []
    print('\nPlease enter ingredients below (separated by commas OR one by one), then type "done" when finished:')

    while True:
        recipe_ingredient = input('Add ingredient(s): ').strip()
    
        if recipe_ingredient.lower() == 'done':
            break
        if not recipe_ingredient:
            print('Input cannot be blank! Please enter an ingredient.')
            continue
        
        items = [item.strip() for item in recipe_ingredient.split(',') if item.strip()]
        ingredients.extend(items)

    # Convert list of ingredients to a single string separated by semicolons for clean CSV storage
    ingredients_str = "; ".join(ingredients)

    # 3. Preparing time 
    while True:
        try:    
            minutes = int(input('Enter preparation time in minutes: '))
            prep_duration = minutes
            break
        except ValueError:
            print('Invalid input! Please enter a valid number of minutes (e.g., 20).')

    # 4. Cooking instructions
    instructions = []
    print('\nPlease enter cooking instructions step-by-step. Type "done" when finished:')

    step_number = 1
    while True:
        step_input = input(f"Step {step_number}: ").strip()

        if step_input.lower() == 'done':
            break
        if not step_input:
            print('Instruction cannot be blank! Please enter a step.')
            continue
        
        instructions.append(step_input)
        step_number += 1

    # Convert instructions list to a single string separated by semicolons
    instructions_str = "; ".join(instructions)

    # 5. Difficulty level
    valid_levels = ['easy', 'medium', 'hard']
    print('\nDifficulty options: Easy, Medium, Hard')
    while True:
        level = input("Enter recipe difficulty level: ").strip().lower()
        if level in valid_levels:
            level = level.capitalize() 
            break 
        else:
            print('Invalid Input! Please enter a valid Difficulty: Easy, Medium, or Hard.')


    # Mandatory 1 - Recipe Category
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
    

    # Create a new recipe dictionary
    new_recipe = {
        'id': [recipe_id],
        'name': [recipe_name],
        'ingredients': [ingredients_str],
        'preparing time': [prep_duration],
        'instructions': [instructions_str],
        'difficulty level': [level],
        'category': [recipe_categorize]
    }

    # Convert the dictionary into a DataFrame
    dataframe = pd.DataFrame(new_recipe)
        
    # Check if the file already exists on your system using os.path.exists
    file_exists = os.path.exists(file_name)
        
    if file_exists:
        dataframe.to_csv(file_name, mode='a', header=False, index=False)
        print(f'\n File {file_name} has been successfully updated with "{recipe_name}"!')
    else:
        dataframe.to_csv(file_name, mode='w', header=True, index=False)
        print(f'\n File {file_name} has been successfully created with your first recipe!')

    
