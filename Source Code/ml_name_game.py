from random import choice


def print_list(my_list, ctr):
    for idx, item in enumerate(my_list, 1):
        print(f"{item} ", end="")

        if idx % ctr == 0:
            print()


def welcome_message(count):
    print(f"""
--------------[ Welcome to Mobile Legends! ]--------------
\tThis game is about Mobile Legends hero names. We will 
give a clue about the hero's first letter and you will
guess the hero's name. Capitalization is not strict but
make sure about the spelling.  Currently, there's {count}
heroes on my list. 
""")


hero_list = ["Granger", "Gusion", "Fanny", "Alucard", "Nana", "Gatotkaca", "Bane", "Moskov", "Carmilla", "Freya",
           "Miya", "Balmond", "Saber", "Alice", "Tigreal", "Karina", "Akai", "Franco", "Bruno", "Clint",
           "Rafaela", "Eudora", "Zilong", "Layla", "Minotaur", "Lolita", "Hayabusa", "Gord", "Natalia", "Kagura",
           "Chou", "Sun", "Alpha", "Ruby", "Yi Sun-shin", "Johnson", "Diggie", "Estes", "Hilda", "Aurora",
           "Lapu-Lapu", "Vexana", "Roger", "Karrie", "Harley", "Irithel", "Grock", "Argus", "Odette", "Lancelot",
           "Hylos", "Zhask", "Helcurt", "Pharsa", "Lesley", "Jawhead", "Angela", "Valir", "Martis", "Uranus",
           "Hanabi", "Chang'e", "Kaja", "Selena", "Aldous", "Claude", "Leomord", "Lunox", "Hanzo", "Belerick",
           "Kimmy", "Thamuz", "Harith", "Minsitthar", "Kadita", "Faramis", "Badang", "Khufra", "Guinevere",
           "Esmeralda", "Terizla", "X.Borg", "Ling", "Dyrroth", "Lylia", "Baxia", "Masha", "Wanwan", "Silvanna",
           "Cecilion", "Atlas", "Popol and Kupa", "Yu Zhong", "Luo Yi", "Benedetta", "Khaleed", "Barats", "Brody",
           "Yve", "Mathilda", "Paquito", "Gloo", "Beatrix", "Phoveus", "Natan", "Aulus", "Aamon", "Valentina",
           "Edith", "Floryn", "Yin", "Melissa", "Xavier", "Julian", "Fredrinn", "Joy", "Novaria", "Arlott", "Ixia",
           "Nolan", "Vale"]


hero_counts = len(hero_list)
welcome_message(hero_counts)

score = 0
hero_list = [hero.capitalize() for hero in hero_list]
already_guessed = []

while True:
    clue = choice(hero_list)[0]
    guess = input(f"Type hero's name starting from letter {clue}: ").capitalize()

    if guess in hero_list and guess[0] == clue:
        hero_list.remove(guess)
        score += 1
        print(f"You got it right!\U0001F4AA\nScore: {score}\n")
        already_guessed.append(guess)

    else:
        if guess in already_guessed:
            print(f"\nYou already guessed {guess}.")

        print(f"Game over\U0001F97A\nYour final score is {score}\n")

        mylist = [x for x in hero_list if x[0] == clue]  # filter by letter

        print(f"Possible answer(s): ")

        print_list(mylist, 5)
        print()
        break
