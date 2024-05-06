# Question:2
# Initialize an empty dictionary to store the recipes
recipes = {}

# Recipe class
class Recipe:
    def __init__(self, id, name, ingredients, instructions):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

# Function to add a new recipe or update the existing recipe
def add_recipe(id, name, ingredients, instructions):
    if id in recipes:
        recipes[id].name = name
        recipes[id].ingredients = ingredients
        recipes[id].instructions = instructions
    else:
        recipes[id] = Recipe(id, name, ingredients, instructions)

# Function to update an existing recipe
def update_recipe(id, name=None, ingredients=None, instructions=None):
    if id in recipes:
        if name:
            recipes[id].name = name
        if ingredients:
            recipes[id].ingredients = ingredients
        if instructions:
            recipes[id].instructions = instructions
    else:print("ID not found.")

# Function to remove a recipe from the system
def remove_recipe(id):
    if id in recipes:
        del recipes[id]
    else:
        print("ID not found.")

# Function to search for a recipe by name or ingredient
def search_recipe(name=None, ingredient=None):
    results = []
    for recipe in recipes.values():
        if (name and recipe.name.lower() == name.lower()) or (ingredient and any(ingredient.lower() in ingredient_name.lower() for ingredient_name in recipe.ingredients)):
            results.append(recipe)
    return results

# Function to display all recipes available in the system
def display_recipes():
    for recipe in recipes.values():
        print(f"ID: {recipe.id}, Name: {recipe.name}")

# Main menu-driven interface
while True:
    print("\n1. Add a new recipe")
    print("2. Update an existing recipe")
    print("3. Remove a recipe")
    print("4. Search for a recipe")
    print("5. Display all recipes")
    print("6. Exit the program")

    option = int(input("Enter your choice: "))

    if option == 1:
        id = int(input("Enter the recipe ID: "))
        name = input("Enter the recipe name: ")
        ingredients = input("Enter the ingredients (comma-separated): ").split(',')
        instructions = input("Enter the instructions: ")
        add_recipe(id, name, ingredients, instructions)
    elif option == 2:
        id = int(input("Enter the recipe ID: "))
        name = input("Enter the new recipe name (leave blank to keep unchanged): ")
        ingredients = input("Enter the new ingredients (comma-separated, leave blank to keep unchanged): ").split(',')
        instructions = input("Enter the new instructions (leave blank to keep unchanged): ")
        update_recipe(id, name, ingredients, instructions)
    elif option == 3:
        id = int(input("Enter the recipe ID: "))
        remove_recipe(id)
    elif option == 4:
        name = input("Enter the recipe name (leave blank to search by ingredient): ")
        ingredient = input("Enter the ingredient (leave blank to search by name): ")
        results = search_recipe(name, ingredient)
        for recipe in results:
            print(f"ID: {recipe.id}, Name: {recipe.name}, Ingredients: {', '.join(recipe.ingredients)}, Instructions: {recipe.instructions}")
    elif option == 5:
        display_recipes()
    elif option == 6:
        break
    else:
        print("Invalid choice. Please try again.")