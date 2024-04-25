# Initialize an empty shopping list
shopping_list = []

# Display the shopping list
def display_list():
    print("Shopping List:")
    if shopping_list:
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

# Add an item to the shopping list
def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

# Remove an item from the shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. Display Shopping List")
        print("2. Add Item to Shopping List")
        print("3. Remove Item from Shopping List")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_list()
        elif choice == '2':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '3':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '4':
            print("Thank you for using the Shopping List Manager. Bye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the main function
if __name__ == "__main__":
    main() 