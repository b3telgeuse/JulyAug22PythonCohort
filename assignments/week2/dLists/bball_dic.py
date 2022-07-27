# Class here
class Player:
    def __init__(self, john):
        self.name = john['name']
        self.age = john['age']
        self.position = john['position']
        self.team = john['team']

    def __repr__(self):
        display = f"Player: {self.name}, age: {self.age}, pos: {self.position}, team: {self.team}"
        return display


# Dictionaries here
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


# Player instances here
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
print(player_jason)
print(player_kevin)
print(player_kyrie)

