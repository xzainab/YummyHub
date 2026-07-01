import pandas as pd
import os
import uuid
from random import randint
import streamlit as sl

FILE_NAME = "recipes.csv"

# Mandatory 1 - categorize recipes
def recipes_categorize():
    """
       Categorizes a given recipe into Breakfast, Lunch, Dinner, or Dessert.
       Done by Zainab Abdulwahab
    """
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

# Mandatory 3 - rating recipes
def rate_recipe():
    """ 
       To allow users to rate a recipe using float values.
       Done by Malak Mahdi
    """
    df, size = load_recipes()
    if size == 0:
        print("\nThere are no recipes available to rate!")
        return 0.0

    recipe_name = input("\nEnter the name of the recipe you want to rate: ").strip().lower()
    
    # Check if the recipe exists
    match = df[df['name'].str.lower() == recipe_name]
    if match.empty:
        print(f"Recipe '{recipe_name}' not found.")
        return 0.0

    # Get the exact row index and extract the existing rating safely as a float
    idx = match.index[0] 
    old_rating = float(df.at[idx, 'rating'])

    while True:
        try:
            new_rating = float(input("Enter your rating (1 to 5 stars, e.g., 4.5): "))
            if 1.0 <= new_rating <= 5.0:
                break
            print("Rating must be between 1.0 and 5.0.")
        except ValueError:
            print("Invalid input! Please enter a valid decimal number.")

    # Calculate the average if a previous rating exists
    if old_rating > 0.0:
        final_rating = (old_rating + new_rating) / 2.0
        print(f"Old rating was {old_rating:.1f}. New calculated average is {final_rating:.1f}")
    else:
        final_rating = float(new_rating)
        print(f"First rating recorded for this recipe!")

    # Round the final result to 1 decimal place
    saved_rating = float(round(final_rating, 1))

    df.at[idx, 'rating'] = saved_rating
    df.to_csv(FILE_NAME, index=False)
    print(f"Success! '{df.at[idx, 'name']}' is now rated {saved_rating}/5 stars.")
    
    return saved_rating

# Mandatory 4 - shopping list
def shopping_list():
    """
       Creat a shopping list depending on the selected recipes
       Done by Kawthar Hussain
    """
    shopping_list = []
    allRecipes = pd.read_csv("recipes.csv")

    print("\nPlease enter each recipe below, then type 'done' when finished to print the shopping list:")

    while True:
        recipe_name = input("Enter recipe name (or type 'done') to print the shopping list: ").strip()

        if recipe_name.lower() == 'done':
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


def add_new_recipe():
    """
       Adding a new recipe into the recipe csv file
       Done by Zainab Abdulwahab
    """
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
        "category": [category_val],
        "rating": 0
    }

    dataframe = pd.DataFrame(new_recipe)
    file_exists = os.path.exists(FILE_NAME)
    
    if file_exists:
        dataframe.to_csv(FILE_NAME, mode="a", header=False, index=False)
        print(f"\nFile {FILE_NAME} has been successfully updated with {recipe_name}!")
    else:
        dataframe.to_csv(FILE_NAME, mode="w", header=True, index=False)
        print(f"\nFile {FILE_NAME} has been successfully created with your first recipe!")

def search_by_ingredients():
    """
    Search for recipes by a specific ingredient.
    Done by Malak Mahdi
    """
    # Load the recipes dataframe
    df = load_recipes()[0]
    
    search_ingredient = input("Enter an ingredient to search recipes: ").lower().strip()
    
    # Filter the dataframe safely by checking if the ingredient string contains the input
    matched_recipes = df[df['ingredients'].str.lower().str.contains(search_ingredient, na=False)]
    
    # Check if any matches were found
    if not matched_recipes.empty:
        print("\n=== FOUND RECIPES ===")
        # Display specific columns cleanly without the dataframe index
        print(matched_recipes[['name', 'preparing time', 'difficulty level']].to_string(index=False))
    else:
        print("\nNo available recipes found with the mentioned ingredient.")


def load_recipes():
    """Helper function to safely load recipes, ensure columns exist, and match data types"""
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        if 'rating' not in df.columns:
            df['rating'] = 0.0
            
        df['rating'] = df['rating'].astype(float)
        return df, df.shape[0]
    return pd.DataFrame(), 0

def view_all_recipes():
    """
       Display all recipes with their name and preparation time
       Done by Kawthar Hussain
    """
    try:
        allRecipes = pd.read_csv("recipes.csv")
        size = allRecipes.shape[0]

        if size == 0:
            print("\n-----THERE IS NO RECIPES----")
        else:
            print("\n-----ALL RECIPES----")
            print(allRecipes[["name", "preparing time"]])

    except FileNotFoundError:
        print("\n-----ERROR: recipes.csv FILE NOT FOUND----")


def random_recipe():
    """
       randomly select and display a complete recipe
       Done by Kawthar Hussain
    """
    try:
        allRecipes = pd.read_csv("recipes.csv")
        size = allRecipes.shape[0]

        if size == 0:
            print("\n-----THERE IS NO RECIPES----")
        else:
            num = randint(0, size - 1)
            print(allRecipes.iloc[[num]])

    except FileNotFoundError:
        print("\n-----ERROR: recipes.csv FILE NOT FOUND----")

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
    print("5. Rating recipes")
    print("6. Create a shopping list")
    print("7. Exit")
    return input("Enter your choice (1-7): ")

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
            search_by_ingredients()
        elif choice == "3":
            view_all_recipes()
        elif choice == "4":
            random_recipe()
        elif choice == "5":
            rate_recipe()
        elif choice == "6":
            shopping_list()
        elif choice == "7":
            print("Thank you for using DIGITAL RECIPE BOOK. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

