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
 
