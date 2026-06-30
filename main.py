def display_menu():
    """
       Display the main menu options
       Done by Zainab Abdulwahab
    """
    print('\n=== DIGITAL RECIPE BOOK ===')
    print('1. Add a new recipe')
    print('2. Search for a recipe')      
    print('3. View all recipes')
    print('4. Generate a random recipe')  
    print('5. Exit')
    return input('Enter your choice (1-5): ')


def main():
    """Main application function"""
    print('WELCOME TO THE DIGITAL RECIPE BOOK')
    print('This application helps you easily store, retrieve, and')
    print('manage your favorite cooking recipes all in one place.')

    while True:
        choice = display_menu()

        if choice == '1':
            add_new_recipe()
        elif choice == '2':
            search_for_recipe()
        elif choice == '3':
            view_all_recipes()
        elif choice == '4':
            random_recipe()
        elif choice == '5':
            print("Thank you for using DIGITAL RECIPE BOOK. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.") 

