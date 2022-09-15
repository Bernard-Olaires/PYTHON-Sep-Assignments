# Player class with updated constructor
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

    # not needed but wanted to create a print method
    def print_player(self):
        print(f"Player: {self.name},")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Team: {self.team}")


kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

# Challenge 2: Create instances using individual player dictionaries.

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)



player_kevin.print_player()
print("-------------------------")
player_jason.print_player()
print("-------------------------")
player_kyrie.print_player()
print("-------------------------")




players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

# Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

new_team = []

for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)
    #new_team.append(Player(player_dict))
print(new_team)
