class Robot:
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30
r1.introduce_self()

r2 = Robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40
r2.introduce_self()

print("------------------------") #gives space to output



class Cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_information(self):
        print("My cars brand is " + self.brand)
    
    
c1 = Cars("Scion", "tC", 2013)
c2 = Cars("Mazda", 6, 2015)

c1.car_information()
c2.car_information()

print("------------------------") #gives space to output



class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

user_1 = User("Bernard", "Olaires", 26)
print(user_1.first_name)
print(user_1.last_name)
print(user_1.age)
user_1.greeting()



print("------------------------") #gives space to output



class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1 - percent_off)

    # Returns a total with tax added to the price
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    # Reduces the price by a fixed dollar amount
    def cut_price_by(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("price defuction too large.")


my_converse = Shoe("Converse", "High-tops", 59.99)
print(f"Price before 50% off sale:")
print(my_converse.price)
my_converse.on_sale_by_percent(0.5) 
print(f"Price after 50% off sale:")
print(my_converse.price)



print("------------------------") #gives space to output



my_vans = Shoe("Vans", "High-tops", 69.99)
print(f"Price before tax:")
print(my_vans.price)
print(f"Price after tax:")
print(my_vans.total_with_tax(.08))



print("------------------------") #gives space to output

my_adidas = Shoe("Adidas", "NMD", 120.00)
print(f"Price before cut price:")
print(my_adidas.price)
my_adidas.cut_price_by(30)
print(f"Price after cut pruce:")
print(my_adidas.price)