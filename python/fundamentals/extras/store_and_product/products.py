# create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
class Products:
    def __init__(self, name, price, category):
        self.name = name 
        self.price = price
        self.category = category

    # print the name of the product, its category, and its price.
    def print_info(self):
        print("Product: " f"{self.name}")
        print("Category: " f"{self.category}")
        print("Price: $", str(self.price))

    # updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (1 * percent_change)
            return self
        else:
            self.price = self.price - (1 * percent_change)












# banana = Products("banana", .50, "fruit")
# banana.print_info()

# print("---------------------------------------") # seperate print 
# banana.update_price(.05, is_increased= True)
# banana.print_info()

# print("---------------------------------------") # seperate print 

# banana.update_price(.05, is_increased= False)
# banana.print_info()
