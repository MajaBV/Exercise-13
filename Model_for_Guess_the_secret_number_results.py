import json
import datetime
import random

player_name = input("What is your name? ")


class Result():
    def __init__(self, broj_pokusaja, player_name, datum):
        self.broj_pokusaja = broj_pokusaja
        self.player_name = player_name
        self.datum = datum


def play_game():
    secret = random.randint(1, 30)
    broj_pokusaja = 0
    wrong_guesses = []
    best_score = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        broj_pokusaja = broj_pokusaja + 1

        if guess == secret:
            new_score = Result(broj_pokusaja=broj_pokusaja, player_name=player_name, datum=str(datetime.datetime.now()))
            best_score.append(new_score.__dict__)

            with open("score.txt", "w") as score_file:
                score_file.write(str(new_score.__dict__))

            print("Congratulations! You guessed the secret number.")
            print("Broj pokusaja: " + str(broj_pokusaja))
            break
        elif broj_pokusaja > 10:
            print("Zao mi je, premasili ste broj pokusaja")
            break
        elif 30 < guess < 1:
            print("Error")
        elif guess > secret:
            print("Probaj manji broj")
        elif guess < secret:
            print("Probaj veci broj")
        else:
            print("Sorry, your guess is not correct... The secret number is not " + str(guess))

        wrong_guesses.append(guess)


def get_score_list():
    with open("score.txt", "r") as score_file:
        best_score = json.loads(score_file.read())
        return best_score


def get_top_scores():
    best_score = get_score_list()
    new_best_score = sorted(best_score, key=lambda x: x['broj_pokusaja'])[:3]
    return new_best_score


while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print("Dan/sat {0} Igrac {1} je imao/la {2} pokusaja. Skriveni broj je broj {3}. Pogresni pokusaji {4}".format(score_dict.get("datum"), score_dict.get("igrac"), str(score_dict.get("broj_pokusaja")), score_dict.get("tajni_broj"), score_dict.get("pogresni_pokusaji")))
    else:
        break




