from pets import Pet
# directly importing Pet class from pets

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

    def bathe(self):
        self.pet.noise_()

my_treats = ["Bacon", "Rabbit Ear", "Turkey Necks"]
my_pet_food = ["Meat Patties", "Chicken"]

rocco = Pet("Rocco", "Dog", ['rocco never gets full', 'can roll over'], "Hap Hap")

bernard = Ninja("Bernard", "Olaires", my_treats, my_pet_food, rocco)

bernard.feed()
bernard.walk()
bernard.bathe()



