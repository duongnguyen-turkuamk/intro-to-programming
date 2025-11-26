"""
# Filename: product_functions.py
# Purpose: create functionalities related to products
# Authors: Nguyen, Duong Nguyen - Maraggun, Jeane - Nguyen, Dung - Nguyen, Duy Linh
# Created: 23.11.2025
# Modified: 25.11.2025
# Description:
    # Data structure for a product
        - Use tuple to store of (ID (int), name (str), description (str), price (float), stock (int))
        - Use list to manipulate products
    # Functionalitites:
        - Add a product: create_product(name: str, description: str, price: float, stock: int)
        - Remove a product: delete_product(product_id: str)
        - View all products
        - Search product: get_product(product_id: str)
        - Update product: update_product(product_id: str, name: str, description: str, price: float, stock: int)
"""

# initialise empty list of products
products = []

def create_new_product():
    product = (int(input("Product ID (intergers only): ")), input("Product name: "), float(input("Price (decimals only - eg. 1.00): ")), input("Description: "), int(input("Stock (integers only): ")))
    return product

# add the product to the list
def add_product():
   new_product = create_new_product()
   products.append(new_product)
   print(f"Successfully added: {new_product}")

# view a list products
def get_all_products():
    for product in products:
        print(product)

# searching for a product by name or ID
def search_product(id=None,name=None):
    for prod in products:
        if prod[0] == id or prod[1]==name: # if the id or the name matches, return the product
            return prod
    else:
        print("No match found")
        return None


#def update_product():


#def remove_product():
def remove_product(inventory):
    """
    Removes a product from the inventory by product ID.
    Displays product details for confirmation before deleting.
    Handles invalid or not found product ID with clear messages.
    """
    product_id = input("Enter the ID of the product you want to remove: ").strip()
    # Iterate through inventory to find matching product ID
    for product in inventory:
        if product['id'] == product_id:
            print(f"Product found: {product['name']} (Stock: {product['stock']})")
            confirm = input("Are you sure you want to delete this product? (y/n): ").lower()
            if confirm == 'y':
                inventory.remove(product)
                print("Product has been removed successfully.")
                return True
            else:
                print("Remove operation cancelled.")
                return False
    # If no product matches the entered ID
    print("No product found with the entered ID.")
    return False

# Example inventory structure
inventory = [
    {"id": "A", "name": "Product A", "price": 100, "stock": 5},
    {"id": "B", "name": "Product B", "price": 200, "stock": 10},
    {"id": "C", "name": "Product C", "price": 150, "stock": 8}
]

# Test the remove product function
remove_product(inventory)
print(inventory) 

