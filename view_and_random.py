import pandas as pd
from random import randint
allRecipes= pd.read_csv('recipes.csv')
size=allRecipes.shape[0]
def view_all_recipes():
    '''Display all recipes with their name and preparation time'''
    
    if size==0:
        print('\n-----THERE IS NO RECIPES----')
    else:
        print('\n-----ALL RECIPES----')
        allRecipes[['name', 'preparing time']]
        

def random_recipe ():
    '''randomly select and display a complete recipe'''
    if size==0:
        print('\n-----THERE IS NO RECIPES----')
    else: 
        num=randint(0,size-1)
        allRecipes.iloc[[num]]