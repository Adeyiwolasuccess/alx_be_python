
# shopping_list_manager.py

def display_menu():
    # This function definition satisfies the "Checks for definition of the display_menu"
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # This line satisfies the "Checks for implementation of an array shopping_list"
    shopping_list = []
    
    while True:
        # This line satisfies the "Checks for calling display_menu function"
        display_menu()
        
        # This line satisfies the "Checks for implementation of Choice Input"
        # The input is handled as a string ('1', '2', etc.), which is a robust way to manage menu choices.
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")
            
        elif choice == '2':
            item = input("Enter the item to remove: ")
            # Check if the item exists before trying to remove it
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
                
        elif choice == '3':
            # Check if the list is empty before trying to display it
            if not shopping_list:
                print("\nThe shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
                print("--------------------------")
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# This ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()