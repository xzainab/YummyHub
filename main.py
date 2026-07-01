import pandas as pd
import os
import uuid
from random import randint

FILE_NAME = "recipes.csv"

def recipes_categorize():
    """Categorizes a given recipe into Breakfast, Lunch, Dinner, or Dessert."""
    categorize = ["breakfast", "lunch", "dinner", "dessert"]
    print("\nCategorize options: Breakfast, Lunch, Dinner, Dessert")
    while True:
        recipe_categorize = input("Enter recipe category: ").strip().lower()
        if recipe_categorize in categorize:
            validated_category = recipe_categorize.capitalize()
            print(f"Success! Category set to: {validated_category}")
            return validated_category
        else:
            print("Invalid Input! Please enter a valid category: Breakfast, Lunch, Dinner, or Dessert.")

def add_new_recipe():
    """Adding a new recipe into the recipe csv file"""
    print("\n=== Add a New Recipe ===")
    recipe_id = str(uuid.uuid4())[:6]
    recipe_name = input("Enter recipe name: ").strip()

    # 2. Ingredients list
    ingredients = []
    print("\nPlease enter ingredients below (separated by commas OR one by one), then type 'done' when finished:")
    while True:
        recipe_ingredient = input("Add ingredient(s): ").strip()
        if recipe_ingredient.lower() == 'done':
            break
        if not recipe_ingredient:
            print("Input cannot be blank! Please enter an ingredient.")
            continue
        items = [item.strip() for item in recipe_ingredient.split(",") if item.strip()]
        ingredients.extend(items)
        
    ingredients_str = "; ".join(ingredients)

    # 3. Preparing time
    while True:
        try:
            minutes = int(input("Enter preparation time in minutes: "))
            prep_duration = minutes
            break
        except ValueError:
            print("Invalid input! Please enter a valid number of minutes (e.g., 20).")

    # 4. Cooking instructions
    instructions = []
    print("\nPlease enter cooking instructions step-by-step. Type 'done' when finished:")
    step_number = 1
    while True:
        step_input = input(f"Step {step_number}: ").strip()
        if step_input.lower() == 'done':
            break
        if not step_input:
            print("Instruction cannot be blank! Please enter a step.")
            continue
        instructions.append(step_input)
        step_number += 1
        
    instructions_str = "; ".join(instructions)

    # 5. Difficulty level
    valid_levels = ["easy", "medium", "hard"]
    print("\nDifficulty options: Easy, Medium, Hard")
    while True:
        level = input("Enter recipe difficulty level: ").strip().lower()
        if level in valid_levels:
            level = level.capitalize()
            break
        else:
            print("Invalid Input! Please enter a valid Difficulty: Easy, Medium, or Hard.")

    # Call the categorization function
    category_val = recipes_categorize()

    # Create a new recipe dictionary
    new_recipe = {
        "id": [recipe_id],
        "name": [recipe_name],
        "ingredients": [ingredients_str],
        "preparing time": [prep_duration],
        "instructions": [instructions_str],
        "difficulty level": [level],
        "category": [category_val]
    }

    dataframe = pd.DataFrame(new_recipe)
    file_exists = os.path.exists(FILE_NAME)
    
    if file_exists:
        dataframe.to_csv(FILE_NAME, mode="a", header=False, index=False)
        print(f"\nFile {FILE_NAME} has been successfully updated with {recipe_name}!")
    else:
        dataframe.to_csv(FILE_NAME, mode="w", header=True, index=False)
        print(f"\nFile {FILE_NAME} has been successfully created with your first recipe!")

def load_recipes():
    """Helper function to safely load recipes and get current size"""
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        return df, df.shape[0]
    return pd.DataFrame(), 0

def view_all_recipes():
    """
       Display all recipes with their name and preparation time
       Done by Kawthar Hussain
    """
    allRecipes, size = load_recipes()
    if size == 0:
        print("\n-----THERE ARE NO RECIPES----")
    else:
        print("\n-----ALL RECIPES----")
        allRecipes[["name", "preparing time"]]

def random_recipe():
    """
       Randomly select and display a complete recipe
       Done by Kawthar Hussain
    """
    allRecipes, size = load_recipes()
    if size == 0:
        print("\n-----THERE ARE NO RECIPES----")
    else:
        num = randint(0, size - 1)
        print("\n=== RANDOM RECIPE ===")
        allRecipes.iloc[[num]]


def display_menu():
    """
       Display the main menu options
       Done by Zainab Abdulwahab
    """
    print("\n=== DIGITAL RECIPE BOOK ===")
    print("1. Add a new recipe")
    print("2. Search for a recipe by ingredient")
    print("3. View all recipes")
    print("4. Generate a random recipe")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def main():
    """
       Main application function
       Done by Zainab Abdulwahab
    """
    print("WELCOME TO THE DIGITAL RECIPE BOOK")
    print("This application helps you easily store, retrieve, and")
    print("manage your favorite cooking recipes all in one place.")
    
    while True:
        choice = display_menu()
        if choice == "1":
            add_new_recipe()
        elif choice == "2":
            search_for_recipe()
        elif choice == "3":
            view_all_recipes()
        elif choice == "4":
            random_recipe()
        elif choice == "5":
            print("Thank you for using DIGITAL RECIPE BOOK. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

