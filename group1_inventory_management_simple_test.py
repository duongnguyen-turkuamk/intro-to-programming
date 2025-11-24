"""
# Filename: group1_inventory_management_simple.py
# Purpose: Main program to initiate CLI menu of Inventory Management System
# Authors: Nguyen, Duong Nguyen - Maraggun, Jeane - Nguyen, Dung - Nguyen, Duy Linh
# Created: 23.11.2025
# Modified: 25.11.2025
# Description: Implement simple Inventory Management System
    # CLI menu:
        + 1. Add product
        + 2. View list of products
        + 3. Search for a product
        + 4. Update a product
        + 5. Remove a product
        + 6. Add customer
        + 7. Update customer
        + 8. Remove customer
        + 9. Search for a customer
        + 10. Order a product
        +.11. Search for an order
        + 12. Exit


"""
# import defined functions from product_functions, customer_products, sales_functions
#from product_functions_test import add_product, search_product, get_all_products, update_product, remove_product
#from customer_functions_test import add_customer_to_db, update_customer, delete_customer, get_customer
#from sales_functions_test import create_order, search_order, calculate_total

from product_functions_test import add_product, create_new_product, search_product, get_all_products

# CLI main menu:
def main():
    # implement the menu for the user interaction
    while True:
        print("1. Add product")
        print("2. View list of products")
        print("3. Search for a product")
        print("4. Update a product")
        print("5. Remove a product")
        print("6. Add customer")
        print("7. Update customer")
        print("8. Remove customer")
        print("9. Search for a customer")
        print("10. Order a product")
        print("11. Search for an order")
        print("12. Exit")
        
        choice = input("Choose an option: ") # ask user for option

        if choice == "1": # adding product
            """
            # function to add product here
            """
            add_product()
        
        elif choice == "2": # view list of products
            """
            # view products function
            """
            get_all_products()
        
        elif choice == "3": # search for a product
            id = input("Enter the ID of the product to search: ")
            # if empty ID then use product name
            if id == "":
               name = input("Enter product name to search: ")
            else: # catch invalid ID exception
                try:
                    id = int(id) # convert id from string to int
                except ValueError:
                    print("Invalid ID")
                name = input("Enter the name: ")

            print("Product details:" , search_product(id,name))

        elif choice == "4": # update a product
            """
            # update function for a product here
            """

        elif choice == "5": # remove a product
            """
            # remove a product function here
            """
        
        elif choice == "6": # adding a customer
            """
            # adding a customer here
            """
        
        elif choice == "7": # updating customer's info
            """
            # update customer's info here
            """
        
        elif choice == "9": # remove a customer
            """
            # remove a customer
            # """
        
        elif choice == "10": # search for a customer
            """
            # search for a customer function
            """      
        
        elif choice == "11": # search for an order
            """
            # search for an order here
            """

        elif choice == "12": # quit program
            print("Thank you. Goodbye!")
            break
        
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()




