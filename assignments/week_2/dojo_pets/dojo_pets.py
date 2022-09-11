class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        print(f"{self.first_name}" " is walking!")
    
    def feed(self):
        print("Feeding ", f"{self.first_name}")

class Pet(Ninja):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type 
        self.tricks = tricks
    
    def sleep(self):
        print("Increasing", f"{self.name}", "energy by 25")
    
    def eat(self):
        print("Increasing", f"{self.name}", "energy by 5 & health by 10")
    
    def play(self):
        print("Increasing", f"{self.name}", "health by 5")
    
    def noise(self):
        print("RAWRRR")


bern = Ninja("Bernard", "Olaires", "bacon", "steak", "Rocco")

rocco = Pet("Rocco", "Dinosour", "Play Dead")

bern.walk()