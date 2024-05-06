# Question 1
# Initialize an empty dictionary to store the inventory
inventory = {}

# Function to add a new book or update the quantity
def add_book(isbn, title, author, price, quantity):
    if isbn in inventory:
        inventory[isbn] = (title, author, price, quantity)
    else:
        inventory[isbn] = (title, author, price, quantity)

# Function to update the details of an existing book
def update_book(isbn, title, author, price):
    if isbn in inventory:
        inventory[isbn] = (title, author, price, inventory[isbn][3])
    else:
        print("ISBN not found.")

# Function to remove a book from the inventory
def remove_book(isbn):
    if isbn in inventory:
        del inventory[isbn]
    else:
        print("ISBN not found.")

# Function to display the current inventory
def display_inventory():
    for isbn, (title, author, price, quantity) in inventory.items():
        print(f"ISBN: {isbn}, Title: {title}, Author: {author}, Price: {price}, Quantity: {quantity}")

# Main menu-driven interface
while True:
    print("\n1. Add a new book")
    print("2. Update existing book details")
    print("3. Remove a book")
    print("4. Display current inventory")
    print("5. Exit the program")

    option = int(input("Enter your choice: "))

    if option == 1:
        isbn = input("Enter the ISBN: ")
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        add_book(isbn, title, author, price, quantity)
    elif option == 2:
        isbn = input("Enter the ISBN: ")
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        price = float(input("Enter the price: "))
        update_book(isbn, title, author, price)
    elif option == 3:
        isbn = input("Enter the ISBN: ")
        remove_book(isbn)
    elif option == 4:
        display_inventory()
    elif option == 5:
        break
    else:
        print("Invalid choice. Please try again.")