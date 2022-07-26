class User:
    def __init__(self, first_name, last_name, example_Email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = example_Email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.gold_card_points)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points = (self.gold_card_points) - (amount)


Adam = User("Adam", "Ulrich", "ulrichac00@gmail.com", 22)

Theo = User("Theo", "Oakley", "toakley6@gmail.com", 21)

Lily = User("Lily", "Huron", "lhuron3@gmail.com", 23)


Theo.spend_points(50)

Lily.enroll()

Lily.spend_points(80)


Adam.display_info()
print()
Theo.display_info()
print()
Lily.display_info()
print()
