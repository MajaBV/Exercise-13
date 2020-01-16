import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


def bb_player():
    first_n = input("Enter first name: ")
    last_n = input("Enter last name: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    point = input("Enter the number of points: ")
    rebound = input("Enter the number of rebounds: ")
    assist = input("Enter the number of assists: ")

    b_player = BasketballPlayer(first_name=first_n, last_name=last_n, height_cm=height, weight_kg=weight, points=point,
                                rebounds=rebound, assists=assist)

    with open("b_players.txt", "a") as player_file:
        player_file.write(json.dumps(b_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(b_player.__dict__))


def fb_player():
    first_n = str(input("Enter first name: "))
    last_n = str(input("Enter last name: "))
    height = int(input("Enter height: "))
    weight = int(input("Enter weight: "))
    goal = int(input("Enter the number of goals: "))
    yellow_card = int(input("Enter the number of yellow cards: "))
    red_card = int(input("Enter the number of red cards: "))

    f_player = FootballPlayer(first_name=first_n, last_name=last_n, height_cm=height, weight_kg=weight, goals=goal,
                              yellow_cards=yellow_card, red_cards=red_card)

    with open("f_players.txt", "a") as player_file:
        player_file.write(str(f_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(f_player.__dict__))


while True:
    selection = input("Would you like to A) create new basketball player B) create new football player or c) quit? ")

    if selection.upper() == "A":
        bb_player()
    elif selection.upper() == "B":
        fb_player()
    else:
        print("Goodbye!")
        break















