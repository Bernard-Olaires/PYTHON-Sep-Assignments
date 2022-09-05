class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(f"Points:", self.gold_card_points)
    
    def enroll(self):
        self.is_rewards_member = True 
        self.gold_card_points = 200
        if self.is_rewards_member == True:
            print(f"User is already a member")
            return True
        else:
            return False
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else: 
            print(f"Not enought points to spend")

user_1 = User("Bernard", "Olaires", "bolairesjr@gmail.com", 25)
user_1.display_info()
user_1.spend_points(50)

print("------------------------") #gives space to output

user_2 = User("Jordan", "Jarandson", "Jjarandson@hotmail.com", 21)
user_2.display_info()

print("------------------------") #gives space to output

user_2.enroll()
print(user_2.gold_card_points)
user_2.spend_points(80)
print(user_2.gold_card_points)

print("------------------------") #gives space to output

user_3 = User("Patrick", "Olaires", "pmatthewolaires@gmail.com", 24)
user_3.display_info()