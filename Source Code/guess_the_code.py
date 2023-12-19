import random

MIN_CHARACTERS = 2
MAX_CHARACTERS = 8

#  setting the allowed characters
valid_character = ["A", "B", "C", "D", "E", "F", "G", "H"]

print('\nWelcome to "Break the Code" game!\n')

print("""\tYour task is to guess the code using the clues we provide for every guess you make. The clue we give 
    is about the placement of the characters you input. The first number represents the count of characters in the 
    correct placement, and the second number represents the count of characters in the incorrect placement.

    For example:
    (2, 1) means that two characters are in the correct placement, and one character is in the incorrect placement.
    (0, 3) means that nothing is in the correct placement, and three characters are in the incorrect placement.
    """)

while True:
    #  declaring variables for future use
    correct_answer = []
    guess_history = []
    random_letter = ""
    checked_letter = []
    hardness = MIN_CHARACTERS
    total_guess = 0

    #  looping until the use type a valid level hardness
    while True:
        MIN_LEVEL = MIN_CHARACTERS - 1
        MAX_LEVEL = MAX_CHARACTERS - 2

        #  prompting user for level hardness input
        print("1. Student (2-Character Code)")
        print("2. Scholar (3-Character Code)")
        print("3. Master (4-Character Code)")
        print("4. Ninja (5-Character Code)")
        print("5. Hacker (6-Character Code)")
        print("6. CIA Agent (7-Character Code)\n")

        user_input = input("Select the level hardness[1-6]: ")

        #  checking if user type a valid number
        try:
            hardness = int(user_input) + 1

        except ValueError:
            print(f"\nPlease type a number from {MIN_LEVEL} to {MAX_LEVEL}.")

        else:
            # checking if user input is in range of minimum and maximum hardness
            if MIN_CHARACTERS <= hardness <= MAX_CHARACTERS:
                print()
                break

            else:
                print(f"\nPlease type a number from {MIN_LEVEL} to {MAX_LEVEL}.")

        print()

    #  generating random characters for the user to guess
    #  looping till the correct answer list has enough characters
    while len(correct_answer) < hardness:
        #  getting random letters from character list
        random_letter = valid_character[random.randrange(0, MAX_CHARACTERS)]

        if random_letter not in correct_answer:
            correct_answer.append(random_letter)

    #  printing the correct answer for debugging purposes, this will be removed once the program is final
    #  print(correct_answer)

    #  looping till the game ended
    while True:
        #  resetting the value of variables
        correct_position = 0
        wrong_position = 0
        checked_letter.clear()

        #  looping till the user type a valid guess, making sure that the guess is long enough and a valid characters
        while True:
            #  prompting user to set the hardness of the game
            guess = input(f"Guess the {hardness}-character code from A-{valid_character[-1]}(separated by space): ")

            #  removing spaces and comma's and convert to a list
            guess_orig = guess.split()
            guess = guess.upper().split()

            #  checking if user guess is same in the level hardness
            if len(guess) == hardness:

                #  checking every character in the guess list
                for i in range(hardness):
                    if guess[i] not in valid_character:
                        #  print(f"\nGuess must only contain character from [A to {valid_character[-1]}]\n")
                        print(f"\n'{guess_orig[i]}' is not valid.\n")
                        break

                else:
                    break

            else:
                print(f"\nCharacter must be equal to {hardness}\n")

        #  adding the number of guess
        total_guess += 1

        #  looping through every character to give user a clue about correct placement
        for i in range(len(guess)):
            if guess[i] in correct_answer:
                if guess[i] == correct_answer[i]:
                    correct_position += 1
                    checked_letter.append(guess[i])

        #  looping through every character to give user a clue about incorrect placement
        for i in range(len(guess)):
            if guess[i] not in checked_letter:
                if guess[i] in correct_answer:
                    if guess[i] != correct_answer[i]:
                        wrong_position += 1
                        checked_letter.append(guess[i])

        #  adding the guess
        guess_history.append([f"({correct_position}, {wrong_position}) - {guess}"])

        # printing the guess history
        for i in guess_history:
            print(i)
        print()

        #  checking if the user make the correct guess
        if guess == correct_answer:
            difficulty = ""

            if hardness == 2:
                difficulty = "Student"

            elif hardness == 3:
                difficulty = "Scholar"

            elif hardness == 4:
                difficulty = "Master"

            elif hardness == 5:
                difficulty = "Ninja"

            elif hardness == 6:
                difficulty = "Hacker"

            elif hardness == 7:
                difficulty = "CIA Agent"

            if total_guess == 1:
                print(f"Congratulations! You solved {difficulty}-level puzzle in just 1 try!")

            elif 2 <= total_guess <= 9:
                print(f"Congratulations! You solved {difficulty}-level puzzle in just {total_guess} tries!")

            else:
                print(f"Congratulations! You solved {difficulty}-level puzzle in {total_guess} tries!")

            print()

            break

    #  prompting for new game
    play_again = input("Type y to play again: ").upper()

    #  checking if player wants to play again
    if play_again != "Y":
        break

    print("Creating new game...")
    print("--------------------------------------------------------------------------------\n")
