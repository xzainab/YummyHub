import pandas as pd
import streamlit as sl

def search_by_ingredients(recipe): 
    """ To search for ingredients
        Done by Malak Mahdi
    
    """
    # Asking the user to input an ingredient
    search_ingredient = input("Enter an ingredient to search recipes:").lower()
    found = False
    #ingredients =ingredient["garlic", "onion", "salt", "black pepper", "lettuce", "tomato", "cucumber", "rice", "oil", "eggs", "flour", "chocolate", "water", "tomato paste", "sugar", "chicken", "meat", "fish"]
    for recipe in recipes: 
        if search_ingredient in recipe['ingredients'].lower():
            print(f"Recipe available. Recipe: {recipe['name']}")
            found = True
    if not found:
        print("No available recipes found with mentioned ingredient.")


def display_recipes(recipe):
    """ To display all recipes with the given ingredient.
    Done by Malak Mahdi
    """
    print(" ALL RECIPES: ")
    for recipe in recipes:
        print(f"Name: {recipe['name']} - Preping Time: {recipe['prepping']} mins - Difficulty level: {recipe['difficulty level']}")
    else:
        print("Recipe not avaliable!")

""" Stretch Goal: The program allows users to rate recipes and sort by rating."""

def rate_recipe(recipe):
    """ To allow users to rate a recipe.
    """
    recipe_to_rate= input("Enter a recipe you'd like to rate: ").lower()
    found == False
    
    for recipe in recipes:
        if recipe['name'].lower() == recipe_to_rate:
            found = True
    rating = input("Enter a rating from 1 to 5: ")
    recipe['rating'] = rating
    
    if found = True:
        print(f" Recipe: {recipe['name']} -Rating: {rating['rate']}")
    else: print(" Recipe not found! Please input another recipe to rate.")
        


              
