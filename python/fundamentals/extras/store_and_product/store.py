from products import Products

# creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    # takes a product and adds it to the store
    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        for i in range(0,len(self.products)):
            self.products.pop(id)
            print(F"Selling {self.products[id]}")



nike_free_runners = Store("Nike Free Runners")
vans = Store("Vans High Tops")

nike_free_runners.add_product("Nike Free Runners")
vans.add_product("Vans High Tops")




# nike_free_runners.sell_product(0)
# nike_free_runners.print_products()