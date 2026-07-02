import pandas as pd
import os
import uuid
from random import randint
import streamlit as sl

FILE_NAME = "recipes.csv"

def load_recipes():
    """Helper function to safely load recipes and get current size"""
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        return df, 0
    return pd.DataFrame(), 0

def recipes_categorize():
    """
    Categorizes a given recipe into Breakfast, Lunch, Dinner, or Dessert.
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

def rate_recipe():
    """
       Allow users to rate a recipe.
       Done by Malak Mahdi
    """
    recipes, _ = load_recipes()
    if recipes.empty:
        print("No recipes available to rate!")
        return

    recipe_to_rate = input("Enter a recipe you'd like to rate: ").strip().lower()
    output = recipes[recipes["name"].str.lower().str.contains(recipe_to_rate, na=False, regex=False)]

    if output.empty:
        print("Recipe not found! Please input another recipe to rate.")
        return

    if len(output) > 1:
        print("Multiple recipes matched.")
        print(output[["name"]].to_string(index=False))
        recipe_choice = input("Type the exact recipe name you want to rate: ").strip().lower()
        output = output[output["name"].str.lower() == recipe_choice]

        if output.empty:
            print("Exact recipe not found.")
            return

    while True:
        try:
            new_rating = float(input("Enter a rating from 1 to 5: "))
            if 1 <= new_rating <= 5:
                break
            print("Invalid input! The rating must be a number between 1 and 5.")
        except ValueError:
            print("Invalid input! You must enter a number.")

    index = output.index[0]
    old_rating = recipes.loc[index, "rating"]

    if pd.notna(old_rating):
        recipes.loc[index, "rating"] = round((float(old_rating) + new_rating) / 2, 1)
        print(f"An existing rating has been found! The new average rating is {recipes.loc[index, 'rating']}/5.")
    else:
        recipes.loc[index, "rating"] = round(new_rating, 1)
        print(f"First rating has been recorded! The rating is {recipes.loc[index, 'rating']}/5.")

    recipes.to_csv(FILE_NAME, index=False)

def sort_by_rating():
    """
       Sort recipes by their ratings.
       Done by Malak Mahdi
    """
    recipes, _ = load_recipes()
    if recipes.empty:
        print("No recipes available to sort!")
        return

    rated_recipes = recipes.dropna(subset=["rating"])
    sorted_recipes_rt = rated_recipes.sort_values(by="rating", ascending=False)

    if sorted_recipes_rt.empty:
        print("No rated recipes available to sort!")
        return

    print(sorted_recipes_rt[["name", "rating"]].to_string(index=False))

def add_new_recipe():
    """Adding a new recipe into the recipe csv file."""
    print("\n=== Add a New Recipe ===")
    recipe_id = str(uuid.uuid4())[:6]
    recipe_name = input("Enter recipe name: ").strip()

    ingredients = []
    print("\nPlease enter ingredients below (separated by commas OR one by one), then type 'done' when finished:")
    while True:
        recipe_ingredient = input("Add ingredient(s): ").strip()
        if recipe_ingredient.lower() == "done":
            break
        if not recipe_ingredient:
            print("Input cannot be blank! Please enter an ingredient.")
            continue
        items = [item.strip() for item in recipe_ingredient.split(",") if item.strip()]
        ingredients.extend(items)

    ingredients_str = "; ".join(ingredients)

    while True:
        try:
            prep_duration = int(input("Enter preparation time in minutes: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number of minutes (e.g., 20).")

    instructions = []
    print("\nPlease enter cooking instructions step-by-step. Type 'done' when finished:")
    step_number = 1
    while True:
        step_input = input(f"Step {step_number}: ").strip()
        if step_input.lower() == "done":
            break
        if not step_input:
            print("Instruction cannot be blank! Please enter a step.")
            continue
        instructions.append(step_input)
        step_number += 1

    instructions_str = "; ".join(instructions)

    valid_levels = ["easy", "medium", "hard"]
    print("\nDifficulty options: Easy, Medium, Hard")
    while True:
        level = input("Enter recipe difficulty level: ").strip().lower()
        if level in valid_levels:
            level = level.capitalize()
            break
        print("Invalid Input! Please enter a valid Difficulty: Easy, Medium, or Hard.")

    category_val = recipes_categorize()

    new_recipe = {
        "id": [recipe_id],
        "name": [recipe_name],
        "ingredients": [ingredients_str],
        "preparing time": [prep_duration],
        "instructions": [instructions_str],
        "difficulty level": [level],
        "category": [category_val],
        "rating": [None]
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
    """Search for recipes by a specific ingredient."""
    df, _ = load_recipes()
    if df.empty:
        print("No available recipes found.")
        return

    search_ingredient = input("Enter an ingredient to search recipes: ").lower().strip()
    matched_recipes = df[df["ingredients"].str.lower().str.contains(search_ingredient, na=False)]

    if not matched_recipes.empty:
        print("\n=== FOUND RECIPES ===")
        print(matched_recipes[["name", "preparing time", "difficulty level"]].to_string(index=False))
    else:
        print("\nNo available recipes found with the mentioned ingredient.")

    print("\n=== ALL RECIPES ===")
    for _, row in df.iterrows():
        print(f"Name: {row['name']} - Preping Time: {row['preparing time']} mins - Difficulty level: {row['difficulty level']}")

def view_all_recipes():
    """Display all recipes with their name and preparation time."""
    allRecipes, _ = load_recipes()
    if allRecipes.empty:
        print("\n-----THERE ARE NO RECIPES----")
    else:
        print("\n-----ALL RECIPES----")
        print(allRecipes[["name", "preparing time"]].to_string(index=False))

def random_recipe():
    """Randomly select and display a complete recipe."""
    allRecipes, _ = load_recipes()
    if allRecipes.empty:
        print("\n-----THERE ARE NO RECIPES----")
    else:
        num = randint(0, len(allRecipes) - 1)
        print("\n=== RANDOM RECIPE ===")
        print(allRecipes.iloc[[num]].to_string(index=False))

def display_menu():
    """Display the main menu options."""
    print("\n=== DIGITAL RECIPE BOOK ===")
    print("1. Add a new recipe")
    print("2. Search for a recipe by ingredient")
    print("3. View all recipes")
    print("4. Generate a random recipe")
    print("5. Rating recipes")
    print("6. Sort by rating")
    print("7. Exit")
    return input("Enter your choice (1-7): ")

def main():
    """Main application function."""
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
        elif choice == '6':
            sort_by_rating()
        elif choice == '7':
            print("Thank you for using DIGITAL RECIPE BOOK. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.") 
if __name__ == "__main__":
    main()