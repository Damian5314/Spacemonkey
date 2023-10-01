import os 
import random
import time

def slow_text_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

slow_text_print("Welcome to Space Monkey!\n")
slow_text_print("You are expected to solve puzzles and riddles to progress through different stages of the game and eventually win.")
slow_text_print("Please note that your choices will influence the storyline so don't hesitate to play again!")
slow_text_print("Now let the story begin, have fun!\n")
while True: 
    slow_text_print("Do you want to start?")
    slow_text_print("A: Yes")
    slow_text_print("B: No")

    Start_Answer = input("").capitalize()

    if Start_Answer == "A": 
        break
    else: 
        slow_text_print("That's fine, whenever you're ready.\n")

os.system('cls' if os.name == 'nt' else 'clear')


#Level 1: Unknown planet
slow_text_print(
    """Jararis was a special trained monkey that can talk and who was trained to go to space.
One day he was needed for a space mission to get a special rock to save humanity but when he finally got the item,
A astroid hit his ship and he crashed down on a unknown planet.\n                                                                            """)

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("""Jararis: Huh, where am I? 
My head is pounding, and my vision is blurry. I recall flashes of alarm signals and sudden turbulence. 
The last memory I have is looking out the window of my spaceship as I crashed. 
Now I lie here, surrounded by lush green leaves and the sweet scent of tropical flowers.
This is not a place I am familiar with. It's as if I've landed on an entirely different world.
I hear the sounds of unfamiliar creatures and see strange, colorful birds high in the trees. 
Adrenaline rushes through me as I realize I am stranded on this mysterious tropical planet. 
I must find ways to protect myself and explore what this new world has to offer.
I need to go as soon as possible from this planet to save humanity!!
The adventure begins.\n                                                                                                                       """)

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    slow_text_print("What should I do?")
    slow_text_print("A: Get out the ship.")
    slow_text_print("B: Sit down.")
    question_one = input("").capitalize()

    if question_one == "A":
        slow_text_print("You got out of the ship.")
        break
    elif question_one == "B":
        slow_text_print("Grrr I'm hungry, sitting down won't get me anywhere.")

slow_text_print("You look around and see that you're on a different planet.")
slow_text_print("Your spaceship is also broken and you must find a way to fix it.")

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    slow_text_print("Which way should I go?")
    slow_text_print("A: Let's check out the forest.")
    slow_text_print("B: Let's walk around the beach.")
    question_two = input("").capitalize()

    if question_two == "A":
        slow_text_print("You went to check in the forest.\n                                    ")
        break
    elif question_two == "B":
        slow_text_print("Jararis:I don't like sand. It's coarse ,irritating and it gets everywhere.")

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("When entering the forest , there was a bord that Jararis did not see : Forest of riddles!")
slow_text_print("""Jararis:The forest is like a giant playground filled with towering trees, so tall they seem to touch the sky.
It smells like wet earth after rain, a refreshing scent. 
There are flowers everywhere, some as big as my head! 
There are flowers of all colors—red, yellow, blue—all over the place. It's like a rainbow on the ground.
\n                                                                                                           """)

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("""Jararis: As I ventured through the lush forest, my eyes were drawn to a towering banana tree.
Its slender trunk reached up into the sky, and at the top, a cluster of banana hung. 
These bananas were enormous, larger than any I had ever come across in my life.                       
I felt a mix of excitement and hunger.
I wanted to taste the delicious banana and savor the sweet taste of it. 
However, the bananas seemed unreachable, swaying high above the ground.\n                                                                        """)

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("""Beside the tree, I noticed a weathered wooden sign. 
It was weathered and had some faded writing.
I strained my eyes to read: "If you wish to feast on bananas delights, solve the puzzle and prove your might.\n                                                 """)

slow_text_print("Answer at least one questions correctly to make the bananas fall!")

play_count = 0

while play_count < 4:
    question_1 = ("Tuana needs 22 cartons of space-milk from the space-market."
                  " She can only carry 4 cartons at a time.\nHow many trips does she need to make to the space-market?")
    answer_1 = "6"

    question_2 = ("Raees is twelve years old, and he is three times as old as his brother. "
                  "How old will Raees be when he is twice as old as his brother?")
    answer_2 = "8"

    question_3 = "What has to be broken before you can use it?"
    possible_answers_3 = ["egg", "grenade", "heart", "glow stick", "seal", "save", "crust", "seed", "rule",
                          "word", "dream", "solution", "trust", "horse", "code", "habit", "bar"]

    bananas_fallen = False

    while True:
        slow_text_print("\nQuestion 1:", question_1)
        user_answer_1 = input("Your answer for question 1: ").strip().lower()

        slow_text_print("\nQuestion 2:", question_2)
        user_answer_2 = input("Your answer for question 2: ").strip().lower()

        slow_text_print("\nQuestion 3:", question_3)
        user_answer_3 = input("Your answer for question 3: ").lower()

        correct_answers = 0

        if "6" in user_answer_1:
            correct_answers += 1
        if "8" in user_answer_2:
            correct_answers += 1
        if any(word in user_answer_3 for word in possible_answers_3):
            correct_answers += 1

        if correct_answers >= 1:
            slow_text_print("\nCongratulations! You answered at least two questions correctly.")
            slow_text_print("Bananas fall from the tree!")
            slow_text_print("""The correct answers were: q1: 6, q2: 8, and q3 egg, grenade, glow stick, seal, save, crust, seed, rule,
word, dream, solution, trust, horse, code, habit, bar.\n""")
            bananas_fallen = True
            break
        else:
            slow_text_print("\nUnfortunately, you didn't answer at least two questions correctly. Try again.")
            play_count += 1

    if bananas_fallen:
        slow_text_print("You now have enough food to last for a while on this planet.")
        slow_text_print("Jararis: Yeah, I did it! Bananas are coming to me, baby!!\n")
        break

    if play_count >= 2:
        slow_text_print("Unfortunately, you tried too many times. The answers were:")
        slow_text_print('q1: 6, q2: 8, q3: egg')
        slow_text_print('Lararis:Ahh i am so hungry\n')

slow_text_print("""Jararis: Feeling energized after enjoying the delicious bananas, I knew I had to get back on track.
It reminds me of a friend Elias , he is also back on track.""")
slow_text_print("I needed to find the missing parts of my spaceship scattered across the island.")
slow_text_print("Equipped with determination and a belly full of bananas, I ventured deeper into the forest.\n                                                ")

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("The forest was vast and mysterious. Tall trees and dense vegetation made it challenging to navigate.")
slow_text_print("But I was determent. I knew my spaceship parts were somewhere out here, waiting to be found.")

slow_text_print("""After hours of searching, I stumbled upon a unusual clearing in the forest.
In the middle of the clearing lay a important repair kit and my navigation of my ship.
But the problem was how can i get there. Because I saw only a bridge connecting to the clearing\n                                                        """)

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("""jararis: As I approached the bridge, I noticed a massive barrier blocking the way.
It seemed impossible to proceed.
Upon closer inspection, I discovered a control panel with three slots for riddles.
To raise the barrier and access the bridge, I had to solve three riddles: an easy riddle, a medium riddle, 
and a difficult riddle or find a man in the forest named Jango  that now the answers of the riddles.
The fate of my journey depended on my wit and the answers I could provide.
I took a deep breath, ready to face the challenge.\n                                                                """)

os.system('cls' if os.name == 'nt' else 'clear')

# yeahh tog
riddles = {
    'easy': "It's an animal that has four legs, white with black stripes. What is it?",
    'medium': "Boe, boe, boe. What am I?",
    'difficult': "It's given to you by your parent, it's yours, but others use it more than you use it. What am I?"
}

answers = {
    'easy': 'zebra',
    'medium': 'cow',
    'difficult': 'X'
}


def ask_riddle(difficulty):
    return riddles.get(difficulty.lower(), "Invalid difficulty level")


def validate_answer(difficulty, answer):
    return answer.lower() in answers.get(difficulty.lower(), [])


# locomotief
slow_text_print("Options:")
slow_text_print("A. Attempt to solve the riddles.")
slow_text_print("B. Look for a man named Jango for help.")

player_choice = input("Enter your choice (A or B): ").lower()

if player_choice == "a":
    slow_text_print("You choose option A to attempt to solve the riddles.")

    continue_with_riddles = True

    for difficulty_level in ['easy', 'medium', 'difficult']:
        if not continue_with_riddles:
            break

        slow_text_print(f"\nRiddle ({difficulty_level.capitalize()}): {ask_riddle(difficulty_level)}")

        attempts = 0
        max_attempts_easy_medium = 3
        max_attempts_difficult = 3

        while attempts < (
                max_attempts_easy_medium if difficulty_level in ['easy', 'medium'] else max_attempts_difficult):
            user_answer = input("Your answer: ").lower()

            if validate_answer(difficulty_level, user_answer):
                if difficulty_level == 'difficult':
                    slow_text_print("\nCorrect answer! The barrier will open now. Well done!\n")
                    continue_with_riddles = False
                    break
                else:
                    slow_text_print("Correct answer! The barrier is slowly lifting...")
                    break

            else:
                attempts += 1
                remaining_attempts = max_attempts_easy_medium if difficulty_level in ['easy',
                                                                                      'medium'] else (
                    max_attempts_difficult)
                slow_text_print(f"Incorrect answer. Attempts left: {remaining_attempts - attempts}")

                if attempts == remaining_attempts:
                    slow_text_print(f"You've exhausted all attempts for this {difficulty_level} riddle.")
                    retry_option = input("Would you like to retry (R) or stop the puzzle (S)? ").lower()
                    if retry_option == "r":
                        slow_text_print(f"You decide to retry the {difficulty_level} riddle.")
                        attempts = 0
                    elif retry_option == "s":
                        slow_text_print("You decide to stop the puzzle and go find jango.\n")
                        continue_with_riddles = False
                        break
                    else:
                        slow_text_print("Invalid choice. Please enter 'R' to retry or 'S' to stop the puzzle.")

elif player_choice == "b":
    slow_text_print("\nYou chose option B to look for a man named Jango.")
    slow_text_print("You venture further into the forest in search of Jango.")

# Voeg hier de controle voor "S" toe
elif player_choice == "s":
    slow_text_print("\nYou chose to skip. Moving on to the next step.")

else:
    slow_text_print("Invalid choice. Please choose either A, B, or S.")

while True:
    if player_choice == "b":
        slow_text_print("")

    slow_text_print(
        "Jararis: I see the dense trees and the dimming light make it an "
        "eerie journey.")
    slow_text_print("After a while, I hear rustling in the bushes and encounter a man who introduces himself as Jango.")
    slow_text_print("Jararis: He was a men with three eyes.")
    slow_text_print("I had never seen some one like him.")
    slow_text_print("I asked a lot of questions to him. But he didn't want to answer them.")
    slow_text_print("""But when I told him about the riddles by the bridge.
He said the following I can help you with the riddles, but first, I need a favor. 
Can you get one of the following things: toilet paper, green apple, cigarette or my glasses.
Find it for me, and I'll provide you with the answers to the riddles""")
    break

while True:
    jango_favor_choice = input("\nDo you accept Jango's favor? (Yes/No): ")

    if jango_favor_choice.lower() == "yes":
        slow_text_print("\nYou agree to help Jango and  to find things on his list.")
        break
    else:
        print("\nJararis: We need this deal or else we won't get of this planet.")

lvl1_outer_loop = True
while lvl1_outer_loop:
    slow_text_print("Which item will you try to find for Jango?")
    slow_text_print("A: Toilet paper")
    slow_text_print("B: Green apple")
    slow_text_print("C: Glasses")
    slow_text_print("D: Cigarette")
    item_choice = input("Your choice (A, B, C, or D): ").capitalize()

    if item_choice == "A":
        slow_text_print("\nYou decide to find toilet paper for Jango.")
        slow_text_print("You search the nearby areas and come across an abandoned campsite.")
        slow_text_print("A: Go to the table")
        slow_text_print("B: Look in the tent")
        question_toilet = input("Your choice (A or B): ").capitalize()

        if question_toilet == 'A':
            slow_text_print("There is a closet here and a barbecue set.")
            while True:
                slow_text_print("A: Should I look in the closet")
                slow_text_print("B: Should I look in the barbecue set")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    slow_text_print("Ahhhh, a crazy black doll!")
                    continue
                elif closet_choice == 'B':
                    slow_text_print("Yes, there it is! We finally found the toilet paper. Let's head back to Jango.")
                    slow_text_print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_toilet == 'B':
            slow_text_print("Wow, there is a toilet here but no paper. Let's go to the table.")
            while True:
                slow_text_print("A: Look in the area of the table")
                slow_text_print("B: Check the tent")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    slow_text_print("There is a closet here and a barbecue set.")
                    while True:
                        slow_text_print("A: Should I look in the closet")
                        slow_text_print("B: Should I look in the barbecue set")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            slow_text_print("Ahhhh, a crazy black doll!")
                            continue
                        elif closet_choice == 'B':
                            slow_text_print(
                                "Yes, there it is! We finally found the toilet paper. Let's head back to Jango.")
                            slow_text_print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")

                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    slow_text_print("He he, I finally found this toilet paper!")
                    slow_text_print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")

                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            slow_text_print("Invalid choice. Please select A or B.")

    elif item_choice == "B":
        slow_text_print("\nYou decide to venture into the forest to look for a green apple.")
        slow_text_print("You explore the forest and spot an apple tree in the distance.")
        slow_text_print("As you approach the tree, you find a delicious green apple.")
        slow_text_print("You pick the apple and head back to Jango.")
        lvl1_outer_loop = False
        c = """After you found the Green apple that jango needed, he opened the barrier for you."""
        break
    elif item_choice == "C":
        slow_text_print("\nYou decide to find the glasses for Jango.")
        slow_text_print("You search the nearby areas and come across two paths.")
        slow_text_print('Each path lead to another way.')
        slow_text_print("A: Hmmm, should I take the left path. ")
        slow_text_print("B: Oei oei, should I take the right path.")
        question_glasses = input("Your choice (A or B): ").capitalize()

        if question_glasses == 'A':
            slow_text_print("There is a house and a barn.")
            while True:
                slow_text_print("A: Should I look in the house.")
                slow_text_print("B: Should I look in the barn.")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    slow_text_print("Ahhh, f**k I see a huge dog for the house!")
                    slow_text_print("No way I will go there.")
                    continue
                elif closet_choice == 'B':
                    slow_text_print("Yes, there it is! We finally found the glasses. Let's head back to Jango.")
                    slow_text_print("finally after you got to jango and gave his stuff.He helped you open the barrier.")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            slow_text_print("Jararis: nahh i see spooky shit there and no banana there.")
            while True:
                slow_text_print("A:Hmmm, left is good ")
                slow_text_print("B:Oei oei, I take the right path.")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    slow_text_print("There is a house and a barn here")
                    while True:
                        slow_text_print("A: Should I look in the house.")
                        slow_text_print("B: Should I look in the barn.")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            slow_text_print("Ahhh, f**k I see a huge dog for the house.")
                            slow_text_print("Nah now way I'm going there!")
                            continue
                        elif closet_choice == 'B':
                            slow_text_print(
                                "Yes, there it is! We finally found the glasses. Let's head back to Jango.")
                            slow_text_print("finally after you got to jango and gave his stuff.He helped you open the barrier.")

                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    slow_text_print("He he, I finally found this stupid glasses!")
                    slow_text_print("finally after you got to jango and gave his stuff.He helped you open the barrier.")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            slow_text_print("Invalid choice. Please select A or B.")
    elif item_choice == "D":
        slow_text_print("\nYou decide to find the cigarette for Jango.")
        slow_text_print("You search the nearby areas and come across a three.")
        slow_text_print("A:Quickly climb up the tree to explore the area. ")
        slow_text_print("B:Pee on the three.")
        question_glasses = input("Your choice (A or B): ").capitalize()

        if question_glasses == 'A':
            slow_text_print("jararis: Wow this is high.")
            slow_text_print("I think I see a bird's nest. ")
            while True:
                slow_text_print("A: Lets go climb higher.")
                slow_text_print("B: Go to the bird nest.")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    slow_text_print("You misjudged your steps, now you going to fall down Stupid Monkey. ")
                    continue
                elif closet_choice == 'B':
                    slow_text_print("Yes, there it is! We finally found the cigarette in the nest.Let's head back to Jango.")
                    slow_text_print("finally after you got to jango and gave his stuff.He helped you open the barrier.")

                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            slow_text_print("Jararis: Ahh I a freaking spider bit my little monkey while peeing.")
            while True:
                slow_text_print("A:Quickly climb up the tree to explore the area. ")
                slow_text_print("B:Pee on the three.")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    slow_text_print("I see a bird nest")
                    while True:
                        slow_text_print("A:Lets go climb higher.")
                        slow_text_print("B:Go to the bird nest.")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            slow_text_print("You misjudged your steps, now you going to fall down Stupid Monkey")
                            continue
                        elif closet_choice == 'B':
                            slow_text_print(
                                "Yes, there it is! We finally found the cigarette. Let's head back to Jango.")
                            slow_text_print("finally after you got to jango and gave his stuff.He helped you open the barrier.")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    slow_text_print("He he, I finally found this stupid cigarette"
                          "!")
                    slow_text_print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")

                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            slow_text_print("Invalid choice. Please select A or B.")

bridge = ("""Jararis: Yes we dit it!!
Now we can get al of the ship-stuff back and repair the ship\n.
After working for hours jararis finally repaired the ship with his repair kit.
But he realised that he got no fuel to fly.
In his quest for fuel, Jararis explored the planet further.
As he walked through the dense forest, he stumbled upon peculiar markings on the trees.
These markings seemed to be a clue leading to a temple.\n
Eager to find fuel, Jararis followed the markings deep into the forest, leading him to a mysterious temple.
As he stepped inside, the temple seemed to come alive, narrating the tale of the legendary Super Special Banan, 
an extraordinary fruit with unmatched energy that can be used as fuel for the space-ship.
""")
slow_text_print(bridge)
b = ("""Intrigued by the temple's message, Jararis proceeded further and encountered a road.
There was a men at the end of the road. the men was very happy to see someone enter his temple. Because nobody had entered in a long time.
He offered jararis to play a game.
if you would like to play the game with me then I will hand you a super banana.
""")
slow_text_print(b)
while True:
    slow_text_print('Offer play hangmen for super banana fuel')
    slow_text_print("A: Take this offer")
    slow_text_print("B: Decline this offer?")
    offer = input('').capitalize()
    if offer == "A":
        slow_text_print("Lets beat this guy, oehh oehh ah ah ")
        break
    elif offer == "B":
        slow_text_print('We need this change or we will die on this planet.')
import random

words = [
    "banana", "peel", "fruit", "yellow", "men", "zebra", "monkey", "gorilla", "jungle", "riddles", "shiny",
    "rocket", "astronaut", "orbit", "fuel", "cosmos", "galaxy", "spaceship", "chimp", "ape", "orbiting"
]

hangman_art = [
    """
    ------
    |    |
    |
    |
    |
    |
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    """,
    """
    ------
    |    |
    |    O
    |    |
    |
    |
    """,
    """
    ------
    |    |
    |    O
    |   /|
    |
    |
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |
    |
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   /
    |
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    """
]


def play_hangman():
    attempts = 8
    guessed_letters = []
    word_to_guess = random.choice(words).lower()
    word_display = ["_"] * len(word_to_guess)

    slow_text_print("Welcome to Hangman - Banana Edition!")
    slow_text_print("Try to guess the word related to bananas, space and animals.")

    while attempts > 0:
        slow_text_print("\nAttempts left:", attempts)
        slow_text_print("Guessed letters:", ' '.join(guessed_letters) if guessed_letters else "None")
        slow_text_print("Word:", ' '.join(word_display))

        hangman_idx = 8 - attempts
        if hangman_idx >= 0 and hangman_idx < len(hangman_art):
            slow_text_print(hangman_art[hangman_idx])

        guess = input("Enter a letter or the whole word: ").lower()

        if len(guess) == 1:  # Guessing a letter
            if guess in guessed_letters:
                slow_text_print("You already guessed that letter.")
            elif guess in word_to_guess:
                slow_text_print("Good guess!")
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        word_display[i] = guess
                guessed_letters.append(guess)
            else:
                slow_text_print("Wrong guess!")
                attempts -= 1
                guessed_letters.append(guess)
        elif len(guess) == len(word_to_guess) and guess.isalpha():  # Guessing the whole word
            if guess == word_to_guess:
                slow_text_print("Congratulations! You guessed the word:", word_to_guess)
                return True
            else:
                slow_text_print("Wrong guess!")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            slow_text_print("Invalid input. Please enter a valid letter or the whole word.")

        if "_" not in word_display:
            slow_text_print("Congratulations! You guessed the word:", word_to_guess)
            return True

    slow_text_print("You ran out of attempts. The word was:", word_to_guess)
    return False


slow_text_print("We need to win this game to get the super banana!")
while True:
    won = play_hangman()

    if won:
        slow_text_print("Congratulations! You won the game.\n")
        break
    else:
        slow_text_print("Game over. You can try again.")

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        slow_text_print("\nWe need to play this game to win the super banana!\n")

slow_text_print("Finally, after what seemed like an eternity, we got all the things we need to go out of this planet")
slow_text_print("My spaceship was ready.")
slow_text_print("I bid farewell to the Forest of Riddles, a place that had tested my problem solving skills.")
slow_text_print("With a heart full of gratitude, I boarded my spaceship and soared into the cosmic unknown.")
slow_text_print("And so, my adventure continued as I ventured into the depths of the universe, heading back to earth!!\n                                      ")

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("""The journey to Earth was expected to take 14 days.
After 2 days of tending to ship duties and relaxing, something unexpected happened.
I noticed a peculiar, compelling light that seemed to pull my ship upwards.
My spaceship's engines struggled against the force of this strange light, but it was too powerful. 
Before I knew it, I was being drawn into a massive alien spacecraft.
The ship's door opened, and I found myself face to face with aliens who had abducted me.
I was hit and lost consciousness.\n                                        """)

os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print(".............................")
slow_text_print("Guess what, The third riddle was literally impossible to guess.")
slow_text_print("We wanted to waste your time, stupid monkey XD")
slow_text_print("                                       XD                       XD               ")

  

#Level 2: Alien ship
slow_text_print("You've been abducted by aliens.")
slow_text_print("Jararis: I should probably try to escape since they're planning on keeping you imprisoned and steal the rock.")
slow_text_print("You look around you and see three items: Spoon, Toilet paper, Alien playboy magazine.\n                              ")

os.system('cls' if os.name == 'nt' else 'clear')

outer1 = True
while outer1:
    slow_text_print("Which item will you try to use to escape.")
    slow_text_print("A: Spoon")
    slow_text_print("B: Toilet paper")
    slow_text_print("C: Alien playboy magazine")
    Lvl2_Question_One = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')
    if Lvl2_Question_One == "A":
        slow_text_print("You sharpen the edge of the spoon against the wall making it something like a knife.")
        slow_text_print("A Guard is stupid enough to walk close to the iron bars of your jailcell, think fast.")
        slow_text_print("What will you do?")
        slow_text_print("A: Pull him close and stab him in the neck")
        slow_text_print("B: Do nothing and rot in a cell for the rest of your life like a sad little monkey.")
        Lvl2_Question_Two = input("").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            if Lvl2_Question_Two == "A":
                slow_text_print("HE MANAGED TO BLOCK IT, THINK FAST.")
                slow_text_print("A: Grab his gun and shoot him in the head.")
                slow_text_print("B: Grab his neck and choke him to death")
                Lvl2_Question_Two_One = input("").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if Lvl2_Question_Two_One == "A":
                    slow_text_print("You try to shoot him but his gun was on safety mode,\n He runs off for backup and eventually you get publicly executed.")
                    slow_text_print("Try an alternative")
                    break
                    

                elif Lvl2_Question_Two_One == "B":
                    slow_text_print("You succesfully choke him to death,\nAllowing you to grab his keys and silently sneak of the Ship")
                    outer1 = False
                    break

                else:
                    slow_text_print("Pick eiter A or B!!!!!!")
                    break

            elif Lvl2_Question_Two == "B": 
                slow_text_print ("You stay in jail and rot away until you die...")
                slow_text_print("Let's try the more logical answer this time don't you think? :D\n(No but seriously, why would you let that chance slide ._.)")
                break
            
            else:
                slow_text_print("Pick a or b")
                break

    elif Lvl2_Question_One == "B":
        slow_text_print("You use the Toilet paper to clog up your toilet.")
        slow_text_print("A guard comes in trying to unclog the toilet, and leaves the door open like an idiot (lol)")
        slow_text_print("What will you do?")
        slow_text_print("A: You silently steal his spare key out of his back pocket.")
        slow_text_print("B: You sneak out as he's trying to unclog the toilet.")
        Lvl2_Question_Three = input("").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            if Lvl2_Question_Three == "A":
                slow_text_print("You wait for him to fix the toilet and walk out.")
                slow_text_print("When the coast is clear you sneak out,")
                slow_text_print("As you're running you see a guard, he notices you too.")
                slow_text_print("Act fast")
                slow_text_print("A: Run away!")
                slow_text_print("B: Fight him!")
                Lvl2_Question_Three_One = input("").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if Lvl2_Question_Three_One == "A":
                    slow_text_print("You turn your back to him and he shoots you in the back of your head.")
                    slow_text_print("(Why did you think that would work lol??)")
                    break
                            
                elif Lvl2_Question_Three_One == "B":
                    slow_text_print("You quickly run towards him before he could react,\n and use some super advanced monkey ninja move to kill him and get off the spaceship.")
                    outer1 = False
                    break
                
                else:
                    slow_text_print("Pick between A or B :()")
                    break

            elif Lvl2_Question_Three == "B":
                slow_text_print("Long story short, you're a monkey :) you climb up inside the air conditioning system and safely escape the ship.")
                break

            else:
                slow_text_print("PICK BETWEEN A OR B YOU MONKEY!")
                break
               
    elif Lvl2_Question_One == "C":
        slow_text_print("You use the magazine to distract him and steal his keys,\nBut you get distracted aswell and he notices that you try to steal the keys (You're executed, if only you didn't have such a dirty mind)\n                           ")
        
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("PICK BETWEEN A, B OR C >:(\n                        ")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
#Level 3: Alien planet
slow_text_print("You have succesfully escaped the alien spaceship but you are now on their planet.")
slow_text_print("You quickly go hiding because the whole planet is filled with the hostile aliens.")
slow_text_print("Your ship is still on the big alien ship but there is also an other alien ship in sight.")

while True:
    slow_text_print("What will you do?")
    slow_text_print("A: Try to get back your own ship.")
    slow_text_print("B: Try to steal the alien ship.")
    Lvl3_Question_One = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')

    if Lvl3_Question_One == "A":
        slow_text_print("You go back on the alien ship to get your ship back")
        slow_text_print("(You just escaped, you really don't know what you want... -_-)")
        break
    elif Lvl3_Question_One == "B":
        slow_text_print("Jararis: Hmm I feel like I'm forgetting something, but screw that.")
        break


outer_loop = True
while outer_loop:
    if Lvl3_Question_One == "A":
        slow_text_print("You hop into the vents of the spaceship")
        slow_text_print("As you're silently crawling through the vents you see a set of lasers moving towards you.")
        slow_text_print("Probably a defence mechanism designed for sneaky monkeys like you...")
        slow_text_print("Anyways THINK FAST! You look up and see a box, when you open it you see 4 wires.")
        slow_text_print("Which wire will you snap in order to stop the lazers from coming towards you?")
        slow_text_print("A: Red")
        slow_text_print("B: Green")
        slow_text_print("C: Blue")
        slow_text_print("D: Yellow")
        Lvl3_Question_TwoA = input("").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            if Lvl3_Question_TwoA == "D":
                slow_text_print("Well arent you a lucky monkey :D")
                slow_text_print("The lasers turned off!")
                outer_loop = False
                break
                        
            elif Lvl3_Question_TwoA == "A" or Lvl3_Question_TwoA == "B" or Lvl3_Question_TwoA == "C":
                slow_text_print("R.I.P. The wires moved even faster and you didn't move in time...")
                slow_text_print("Try again.")
                break

            else:
                slow_text_print("Are you even trying to survive?")
                slow_text_print("Pick between A, B, C OR D!")
                break

    elif Lvl3_Question_One == "B":
        slow_text_print("You silently sneak over towards the alien ship")
        slow_text_print("When you get the you see that there is a lock on the ships door")
        slow_text_print("It seems as if you need to translate their language to yours...")
        slow_text_print("Language: .. .----. -- / .- / ... - ..- .--. .. -.. / .-.. .. - - .-.. . / -- --- -. -.- . -.-- -.-.--")
        slow_text_print("Jararis: Hmmm, this sure does look like morse code")
        Lvl3_Question_TwoB = input("Please enter the password: ").upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        sanka_loop = True
        while sanka_loop:
            if Lvl3_Question_TwoB == "I'M A STUPID LITTLE MONKEY!":
                slow_text_print("Nice! The door unlocked and you fly off without any problems!")
                outer_loop = False
                second_outer_loop = True
                while second_outer_loop:
                        if Lvl3_Question_TwoB == "I'M A STUPID LITTLE MONKEY!":
                            slow_text_print("Suddenly you get a alarm message on the ships dashboard.")
                            slow_text_print("Jararis: Ah yes I'm flying in a registered ship so I probably need some sort of identification.")
                            slow_text_print("Two messages pop up:")
                            slow_text_print("6x - 8 = 4x + 4")
                            Lvl3_Question_ThreeB = input("Please enter the password x = ")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            while True:
                                if Lvl3_Question_ThreeB == "6":
                                    slow_text_print("Great, those dumb aliens fully believe you're one of them.")
                                    slow_text_print("You fly off into outer space...")
                                    second_outer_loop = False
                                    sanka_loop = False
                                    break
                                
                                elif int(Lvl3_Question_ThreeB) < 6 or int(Lvl3_Question_ThreeB) > 6:
                                    slow_text_print("Wrong answer")
                                    slow_text_print("They fire rockets at you and you die, try again (Damn, you're not that good at maths are you XD)\n              ")
                                    break

                                else:
                                    slow_text_print("Come on this is basic math!")
                                    slow_text_print("What did you even do in math class...               ")
                                    break
            else:
                slow_text_print("You took too long to unlock the door and got noticed by a guard")
                slow_text_print("You got shot, and died...")
                break

bombo_loop = True
if Lvl3_Question_One == "B": bombo_loop = False
while bombo_loop:
    if Lvl3_Question_TwoA == "D":
        slow_text_print("You climb through the vents towards the ships hangar")
        slow_text_print("You're finally reunited with your ship but see that there is a lock on the ship.")
        slow_text_print("It seems as if you need to translate their language to yours...")
        slow_text_print("Language: - ..- .- -. .- / -.- .- -. / -. .. . - / .-. .. .--- -.. . -. / .... .- .... .- -.-.--")
        slow_text_print("Jararis: Hmmm, this sure does look like morse code")
        Lvl3_Question_ThreeA = input("Please enter the password: ").upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        if Lvl3_Question_ThreeA == "TUANA KAN NIET RIJDEN HAHA!":
            slow_text_print("Jararis: Nice! The door unlocked, that was easier than I thought!")
            slow_text_print("I do wonder who Tuana is though...")
            slow_text_print("You fly off into outerspace wondering where else this adventure might lead you to...")
            break
        else:
            slow_text_print("You took too long to unlock the door and got noticed by a guard")
            slow_text_print("You got shot, and died...")
            break

#Level 4:Elysium Prime
slow_text_print("As you're wandering through the vast void of outer space, not knowing where to go all you can think of are bananas...")
slow_text_print("You're going to have to make a stop very soon as you're running out of food")
slow_text_print("You check the space map and see your only hope is an interstellar space station called Elysium Prime")
slow_text_print("You decide to give it a shot as it's your only hope...")

Third_outer_loop = True
while Third_outer_loop:
    slow_text_print("You've landed and managed to find a restaurant")
    slow_text_print("You look around and see that the space station is filled with different alien races")
    slow_text_print("Luckily you stole some money from those alien guards so you've got enough for one meal")
    slow_text_print("What would you like to eat?")
    slow_text_print("A: Spicy Banana Soup")
    slow_text_print("B: Strange looking tentacles")
    slow_text_print("C: A bowl of spiky looking fruits")
    Lvl4_Question_Food = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        if Lvl4_Question_Food == "A":
            slow_text_print("You couldn't resist your monkey urges and obviously picked the Spicy Banana Soup")
            slow_text_print("You finish the WHOLE bowl in 3 minutes! (It was amazing...)")
            Third_outer_loop = False
            break

        elif Lvl4_Question_Food == "B":
            slow_text_print("You decided to go for something new huh?")
            slow_text_print("(How did you not pick the Spicy Banana Soup??? Are you even a real monkey? ._.)")
            slow_text_print("You finish your plate pretty fast, the food wasn't that bad")
            Third_outer_loop = False
            break

        elif Lvl4_Question_Food == "C":
            slow_text_print("Why did you pick this, are you trying to starve Jararis?")
            slow_text_print("Jararis managed to eat some of the food after removing all the spikes")
            slow_text_print("Jararis: That didn't really taste that good but food is food I guess...")
            Third_outer_loop = False
            break

        else:
            slow_text_print("Pick between A,B or C")
            slow_text_print("(Only weirdos don't :D)")

Fourth_outer_loop = True
while Fourth_outer_loop: 
    if Lvl4_Question_Food == "A":
        slow_text_print("Jararis: I should probably get moving now")
        slow_text_print("What will you do?")
        slow_text_print("A: Start looking for usefull things")
        slow_text_print("B: Stay seated...")
        Lvl4_Question_FoodOne = input("").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            if Lvl4_Question_FoodOne == "A":
                slow_text_print("You get up and start exploring the space station")
                Fourth_outer_loop = False
                break

            elif Lvl4_Question_FoodOne == "B":
                slow_text_print("That ain't going to get you far is it")
                slow_text_print("Perhaps you should pick a more serious answer :O")
                slow_text_print("(Seriously, why would you do that to Jararis you monster >:/ )")
                break

    elif Lvl4_Question_Food == "B":
        slow_text_print("Jararis: I should probably get moving now")
        slow_text_print("What will you do?")
        slow_text_print("A: Start looking for usefull things")
        slow_text_print("B: Stay seated...")
        Lvl4_Question_FoodTwo = input("").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            if Lvl4_Question_FoodTwo == "A":
                slow_text_print("You get up and start exploring the space station")
                Fourth_outer_loop = False
                break

            elif Lvl4_Question_FoodTwo == "B":
                slow_text_print("That ain't going to get you far is it")
                slow_text_print("Perhaps you should pick a more serious answer :O")
                slow_text_print("(Seriously, why would you do that to Jararis you monster >:/ )")
                break

    elif Lvl4_Question_Food == "C":
        slow_text_print("Jararis: I should probably get moving now")
        slow_text_print("What will you do?")
        slow_text_print("A: Start looking for usefull things")
        slow_text_print("B: Stay seated...")
        Lvl4_Question_FoodThree = input("").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            if Lvl4_Question_FoodThree == "A":
                slow_text_print("You get up and start exploring the space station")
                Fourth_outer_loop = False
                break

            elif Lvl4_Question_FoodThree == "B":
                slow_text_print("That ain't going to get you far is it")
                slow_text_print("Perhaps you should pick a more serious answer :O")
                slow_text_print("(Seriously, why would you do that to Jararis you monster >:/ )")
                break


        
Fifth_outer_loop = True
while Fifth_outer_loop:
    slow_text_print("Jararis: This is nice, finally no annoying alien guards that chase me around...")
    slow_text_print("Suddenly you hear a loud screaming voice behind you")
    slow_text_print("Alien guard: - .... . .-. . / .... . / .. ... --..-- / --. . - / - .... .- - / ... - ..- .--. .. -.. / -- --- -. -.- . -.-- -.-.--")
    slow_text_print("Jararis: YOU'VE GOT TO BE KIDDING ME!!! (What is this idiot even saying anyways...)")
    slow_text_print("The guards start charging towards you, you have to find a hiding spot.")
    slow_text_print("You have 2 options:")
    slow_text_print("A: You hide in the toilets")
    slow_text_print("B: You hide in a big crowd of people")
    Lvl4_Question_One = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        if Lvl4_Question_One == "A":
            slow_text_print("You run over to the toilers and quickly lock the door. Not too long after you hear the guards charge in and check if you're there")
            slow_text_print("Alien Guard: --. --- -.. / .. / .... .- - . / -- --- -. -.- . -.-- ... -.-.--")
            slow_text_print("Lucky for you, they don't check all the toilets and just leave. (These guards are almost as stupid as you! XD)")
            slow_text_print("Suddenly you feel your stomach starting to burn like CRAZY")
            if Lvl4_Question_Food == "A":
                slow_text_print("Jararis: THAT SPICY BANANA SOUP REALLY WASN'T A GREAT IDEA NOW THAT I THINK ABOUT IT")
                slow_text_print("Jararis now faces his greatest enemy so far on this crazy adventure, The Toilet...")
                slow_text_print("After fighting like a warrior for 4 HOURS STRAIGHT, Jararis has lost a lot...")
                slow_text_print("He's thirsty, hungry and last but not least... has no toilet paper")
                Fifth_outer_loop = False
                break

            elif Lvl4_Question_Food == "B":
                slow_text_print("Jararis: THOSE WEIRD TENTACLES WE'RE A BAD IDEA WHY WOULD I EAT THAT IN THE FIRST PLACE")
                slow_text_print("Jararis now faces his greatest enemy so far on this crazy adventure, The Toilet...")
                slow_text_print("After fighting like a warrior for 4 HOURS STRAIGHT, Jararis has lost a lot...")
                slow_text_print("He's thirsty, hungry and last but not least... has no toilet paper")
                Fifth_outer_loop = False
                break
            
            elif Lvl4_Question_Food == "C":
                slow_text_print("Jararis: WHY DID I EAT THOSE STUPID SPIKE FRUITS THEY LITERALLY LOOKED LIKE A MORNING STAR")
                slow_text_print("(Morning star: A club with a heavy spiked head, sometimes attached to the handle by a chain, this weapon was mostly used in medieval times.)")
                slow_text_print("Jararis now faces his greatest enemy so far on this crazy adventure, The Toilet...")
                slow_text_print("After fighting like a warrior for 4 HOURS STRAIGHT, Jararis has lost a lot...")
                slow_text_print("He's thirsty, hungry and last but not least... has no toilet paper")
                Fifth_outer_loop = False
                break

        elif Lvl4_Question_One == "B":
            slow_text_print("As you're quietly walking with the crowd of people you suddenly get tasered in the back")
            slow_text_print("You pass out...")
            slow_text_print("(You will be tortured for the rest of your life, unlucky lol)")
            break

slow_text_print("After 4 hours someone else finally enters the toilet")
slow_text_print("Jararis: Hey man could you please hand me some toilet paper?")
slow_text_print("Stranger: DAMN it smells like a dead body in here!")
slow_text_print("Jararis (In an ashamed voice): Please just hand me some toilet paper...")
slow_text_print("You finish all the stinky business on the toilet and open the door")
slow_text_print("There he was Monkvano, with his deep, soulful eyes and tuft of unruly fur, he looked back at you with a blend of curiosity and amusement.") 
slow_text_print("He was no ordinary monkey; he was a resident of Elysium Prime, known for his uncanny ability to navigate the city's intricate maze of walkways and rooftops.")
slow_text_print("Jararis: Y-y-you're like me!?")
slow_text_print("Monkvano: Y-y-you're like me!?")
slow_text_print("                                                                           ")
os.system('cls' if os.name == 'nt' else 'clear')

Sixth_outer_loop = True
while Sixth_outer_loop: 
    slow_text_print("Do you ask Monkvano to help you?")
    slow_text_print("A: Yes")
    slow_text_print("B: No")
    Lvl4_Question_Two = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        if Lvl4_Question_Two == "A":
            slow_text_print("Jararis: Do you know how to get back home? I really need to get back home!")
            slow_text_print("Monkvano: Of course my fellow monkey brother, we have to help eachother out ain't that right")
            slow_text_print("Jararis: Could you try to keep me out of sight of those scary Alien Guards though, I think they don't really like me...")
            slow_text_print("Monkvano: Oh yeah same for some reason I've been getting chased around all day")
            slow_text_print("Monkvano: I think there's a criminal monkey on Elysium Prime which they're trying to catch right now")
            slow_text_print("Jararis: Yeah let's just make sure we avoid them...")
            slow_text_print("                                                    ")
            os.system('cls' if os.name == 'nt' else 'clear')
            Sixth_outer_loop = False
            break

        elif Lvl4_Question_Two == "B":
            slow_text_print("After a long talk about how tasty bananas en peanuts are you both part ways.")
            slow_text_print("(You get lost on Elysium Prime and the Alien guards manage to arrest you after a while.)")
            slow_text_print("(WHY WOULDN'T YOU JUST ASK THAT BEAUTIFUL MONKEY MONKVANO FOR HELP?)")
            slow_text_print("                                                                    ")
            os.system('cls' if os.name == 'nt' else 'clear')
            break

slow_text_print("You and Monkvano get to the ship and head into out space again")
slow_text_print("After flying through space for a while, you and monkvano finally arive 'home'")
slow_text_print("(You also farted a lot during the trip, smelly little monkey XD)")
slow_text_print("                                                                 ")
os.system('cls' if os.name == 'nt' else 'clear')

#Level 5: Banana Haven
slow_text_print("You and Monkvano finally landed.")
slow_text_print("Wow this place looks beautifull. Look at those trees and waterfalls!")
slow_text_print("But wait...")
slow_text_print("Are these my...my family???")
slow_text_print("Jararis: Monkvano where on earth are we?")
slow_text_print("Monkvano: Earth? This is Banana Haven, Home right?")
slow_text_print("\nThe locals of Banana Haven seem apprehensive, eyeing you and Monkvano with suspicion.")
slow_text_print("It appears that they are not thrilled to have outsiders on their beloved planet.")
slow_text_print("Jararis: Wow Monkvano my home is earth not this planet! And why are all these people looking mad at us?")
slow_text_print("Monkvano: To be honest with you Jararis, I am exhiled from this planet.")
slow_text_print("Jararis: Exhiled? What did you do to get exhiled?")
slow_text_print("Monkvano: My mother is the queen of this planet and yeah...")

while True:
    slow_text_print("A: We must find your mother, maybe she can help me get off this planet again")
    slow_text_print("B: What do you mean with yeah?")
    lvl5_question_one = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')

    if lvl5_question_one == "A":
        slow_text_print("Monkvano: Wowwww are you sure you want to go to her?")
        slow_text_print("Jararis: Yes because I need to get to earth.")
        break

    elif lvl5_question_one == "B":
        slow_text_print("Monkvano: yeah she exhiled me for no reason. That is just how she works I guess...")
        slow_text_print("Jararis: Oh Ok. I need to get of this planet asap.")
        break

slow_text_print("Monkvano: Well if I get you to her you need to take me with you because I also don't want to stay here.")

while True:
    slow_text_print("A: Alright we have a deal.")
    slow_text_print("B: No I am not taking you with me")
    lvl5_question_two = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')

    if lvl5_question_two == "A":
        slow_text_print("Monkvano: Yes let's go!")
        break

    elif lvl5_question_two == "B":
        slow_text_print("Monkvano: Then I am not taking you to her.")
        slow_text_print("Maybe you should help him because he tried to help you.")

slow_text_print("After a lot of walking and swinging you reached Monkvano's mother. The Monkey Queen.")
slow_text_print("Monkey Queen: Well well well little Monkvano is back and he brought a little friend with him.")
slow_text_print("Monkvano: Hello mother. I am not here to make amends.")
slow_text_print("Monkey Queen: Ok son. What do you want?")
slow_text_print("Monkvano: Can you help me and Jararis to get to earth.")
slow_text_print("Monkey Queen: If you want help, your monkey friend must first beat me at coconut throwing.")

while True:
    slow_text_print("A: Let's play Queen")
    slow_text_print("B: No I don't have time for games.")
    lvl5_question_three = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')

    if lvl5_question_three == "A":
        slow_text_print("Monkvano: No we don't have time for that. Spare us for this time.")
        break

    elif lvl5_question_three == "B":
        slow_text_print("Monkvano: Please mother we don't have time for that. Spare us for this time.")
        break

slow_text_print("Monkey Queen: You are lucky...")
slow_text_print("Monkey Queen: I dont know how to get to earth but I know someone who does.")
slow_text_print("Monkey Queen: He lives on Dwarfmania.")
slow_text_print("                                                                  ")
os.system('cls' if os.name == 'nt' else 'clear')


#Level 6: Dwarfmania
slow_text_print("""Monkvano mother kindly explained that she didn't know where Earth was. However, she mentioned an old monkey  
named Bob Monkey living on Dwarfmania. Yararis and Monkvano embarked on a thrilling adventure, 
boarding a special, magical banana train known for its ability to travel the cosmic expanse between planets.
Only with this train, could you go to Dwarfmania and not with a Spaceship.
As the train zoomed through the galaxy, they felt a surge of excitement, their destination drawing near—the mysterious 
Dwarfsmania.\n 
Upon arriving at Dwarfmania, they were greeted by an indescribable city and world.
It was stunning, yet bustling with dwarves, each deeply engrossed in their own affairs.
Monkvano and Yararis headed to a nearby shop to inquire about the whereabouts of Bob Monkey.
There, they learned that he resided on the highest mountain of the dwarf planet.
To reach the mountain, they needed to take a lift. So the shopkeeper gave them a map and there they went to the unknown.\n
The journey to the mountain was just as smooth, with the lift providing breathtaking views of Dwarfmania.
Upon reaching the mountain, they noticed a grand entrance adorned with magic symbols and markings.
A sign nearby indicated that to speak with or reach Bob Monkey, one must pass a series of challenging trials and tests.
But one off the parkour has a free passage without any danger. So choose your parkour wisely.
                                    """)
os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("Welcome in Bob Monkey trial of death")
slow_text_print("Survive the parkour and you can enter Bob Monkey's house.")

lvl1_outer_loop = True
while lvl1_outer_loop:
    slow_text_print("Which parkour will we go?")
    slow_text_print("A: Dragon slayer")
    slow_text_print("B: Dwarf  slayer")
    slow_text_print("C: Seductive slayer")
    slow_text_print("D: Monkey slayer")
    item_choice = input("Your choice (A, B, C, or D): ").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')

    if item_choice == "A":
        slow_text_print("\nYou decide to go for the Dragon slayer parkour.")
        slow_text_print("You walk straight in the parkour you see two paths:")
        slow_text_print("A: Take left path")
        slow_text_print("B: Take right path")
        question_toilet = input("Your choice (A or B): ").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')

        if question_toilet == 'A':
            slow_text_print("\n You see holes on the ground.")
            while True:
                slow_text_print("A: Run straight as a crazy gorilla")
                slow_text_print("B: Step back, because you a b*tch")
                closet_choice = input("Your choice (A or B): ").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if closet_choice == 'A':
                    slow_text_print("\nAhhhh, fire came out of the holes!You and monkvano died")
                    slow_text_print("Try again")
                    continue
                elif closet_choice == 'B':
                    slow_text_print("\nJararis and Monkvano: yesss we made it across the parkour.")
                    slow_text_print("Lets goo to Bob fuc***ng Monkey.")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_toilet == 'B':
            slow_text_print("\nJararis and  monkvano: Blehhhh, you monkeys died of extreme heat")
            slow_text_print("Try again")
            while True:
                slow_text_print("A: Take left path")
                slow_text_print("B: Take right path")
                table_choice = input("Your choice (A or B): ").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if table_choice == 'A':
                    slow_text_print("\nYou see holes in the ground!.")
                    while True:
                        slow_text_print("A: Run straight as a crazy gorilla")
                        slow_text_print("B: Step back, because you a b*tch")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if closet_choice == 'A':
                            slow_text_print("\n Ahhhh, fire came out of the holes!You and monkvano died")
                            slow_text_print("Try again")
                            continue
                        elif closet_choice == 'B':
                            slow_text_print("\n Jararis and Monkvano: yesss we made it across the parkour.")
                            slow_text_print("Lets goo to Bob fuc***ng Monkey.")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    slow_text_print("\n Jararis and Monkvano: yesss we made it across the parkour.")
                    slow_text_print("Lets goo to Bob fuc***ng Monkey.")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            slow_text_print("Invalid choice. Please select A or B.")

    elif item_choice == "B":
        slow_text_print("\nYou decide to choose parkour Dwarf slayer.")
        slow_text_print("Congratulation you chose the save parkour without any danger.")
        slow_text_print("You can goo freely through the parkour ")
        lvl1_outer_loop = False
        slow_text_print("Jararis and monkvano:Yeahh baby, We got our lucky pants on.")
        break
    elif item_choice == "C":
        slow_text_print("\nYou decide to choose the seductive sc"
              "layer parkour.")
        slow_text_print("You came across two paths with names.")
        slow_text_print('Each path lead to another way.')
        slow_text_print("A: Go left for bananas ")
        slow_text_print("B: Go right for a lady")
        question_glasses = input("Your choice (A or B): ").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')

        if question_glasses == 'A':
            slow_text_print("\nYou see a bananas on the ground!")
            while True:
                slow_text_print("A: Eat the banana")
                slow_text_print("B: Ignore the banana")
                closet_choice = input("Your choice (A or B): ").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if closet_choice == 'A':
                    slow_text_print("\nIt was a trap stupid monkey's.You guys died because of poison!")
                    slow_text_print("Try again")
                    continue
                elif closet_choice == 'B':
                    slow_text_print("Nice job, you almost died of poison.")
                    slow_text_print("Jararis and Monavano: We were to sexy to get seduced. Lets go to the sexy old Bob Monkey")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            slow_text_print("\nYou guys died. The lady shot two arrows through your hearts.")
            slow_text_print("Try again")
            while True:
                slow_text_print("A: Go left for bananas ")
                slow_text_print("B: Go right for a lady")
                table_choice = input("Your choice (A or B): ").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if table_choice == 'A':
                    while True:
                        slow_text_print("A: Go left for bananas ")
                        slow_text_print("B: Go right for a lady")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if closet_choice == 'A':
                            slow_text_print("\nIt was a trap stupid monkey's.You guys died because of poison!")
                            slow_text_print("Try again")
                            continue
                        elif closet_choice == 'B':
                            slow_text_print("Nice job, you almost died of poison")
                            slow_text_print(
                                "Jararis and Monavano: We were too sexy to get seduced. Let's go to the sexy old Bob "
                                "Monkey")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    slow_text_print("\nNIce job, you almost died of poison!")
                    slow_text_print("Jararis and Monavano: We were to sexy to get seduced. Lets go to the sexy old Bob Monkey.")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            slow_text_print("Invalid choice. Please select A or B.")
    elif item_choice == "D":
        slow_text_print("\nYou decided for Monkey Slayer parkour.")
        slow_text_print("While walking in the parkour you read a board congratulation this was the save passage!")
        slow_text_print("A:Walk past the board")
        slow_text_print("B:Stand still")
        question_glasses = input("Your choice (A or B): ").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')

        if question_glasses == 'A':
            slow_text_print("You are know past the board")
            while True:
                slow_text_print("A: Run straight forward.")
                print("B: Walk slowly the parkour out")
                closet_choice = input("Your choice (A or B): ").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if closet_choice == 'A':
                    slow_text_print("\nYou activated a motion detector. It was a bait to say this was a free passage.")
                    slow_text_print("You Monkey's died by a shotgun in the ear")
                    slow_text_print("Try again")
                    continue
                elif closet_choice == 'B':
                    slow_text_print("While walking slowly out of the parkour, no motion detector went of.")
                    slow_text_print("Yararis and Monkvano: Yahhh, lets go to popsy Bob Monkey")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            slow_text_print("\nThe ground suddenly opened up,  and you Stupid Monkey's felt in large spikes")
            while True:
                slow_text_print("A:Walk past the board")
                slow_text_print("B:Stand still")
                table_choice = input("Your choice (A or B): ").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')
                if table_choice == 'A':
                    while True:
                        slow_text_print("A: Run straight forward.")
                        slow_text_print("B: Walk slowly the parkour out")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if closet_choice == 'A':
                            slow_text_print("\n You activated a motion detector. It was a bait to say this was a free passage.")
                            slow_text_print("You Monkey's died by a shotgun in the ear")
                            slow_text_print("Try again")
                            continue
                        elif closet_choice == 'B':
                            slow_text_print("While walking slowly out of the parkour, no motion detector went of.")
                            slow_text_print("Yararis and Monkvano: Yahhh, lets go to popsy Bob Monkey")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    slow_text_print("While walking slowly out of the parkour, no motion detector went of.")
                    slow_text_print("Yararis and Monkvano: Yahhh, lets go to popsy Bob Monkey")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            slow_text_print("Invalid choice. Please select A or B.\n")

slow_text_print("""After Jararis and Monkvano successfully completed the obstacle course, they arrived at the door of Bob Monkey's house.
They knocked, and they could hear these words: "I'm just a Buffalo Soldier
In the heart of America. Stolen from Africa, brought to America.\n 

Jararis then asked, "How can I reach planet Earth?" Bob Monkey explained that he unfortunately couldn't remember the 
coordinates due to his dementia. However, he knew a Jamaican friend: Yara Larissa who might have the information. He offered them a 
submarine and pointed towards the other side of the mountain where a waterfall was located. Bob Monkey advised, 
"Follow the waterfall and the path beyond to reach Aqualandia."
                                        """)
os.system('cls' if os.name == 'nt' else 'clear')

#Level 7: Otoh Gunga 
print("""
As they ventured deeper into the ocean, captivating lights started to illuminate the watery depths. At a certain 
point, they entered a passage, and upon passing through it, they were greeted by an astonishing sight - a realm 
filled with breathtaking underwater houses and awe-inspiring, indescribable structures. After a while, they guided 
their submarine into one of these mesmerizing structures, and the water in the chamber was drained.\n

A person appeared in the room as the submarine hatch opened, asking, "Can I assist you?"
Jararis requested help to reach Yara Larissa. 
Upon reaching Yara, they informed her that Bob had referred them, seeking the coordinates to Earth. After sharing the 
coordinates, Yara graciously presented them with a unique spaceship she had designed, capable of traversing both 
underwater and in the skies.\n
 
 She offered this as a token of gratitude since Bob Monkey had once saved her life, 
and considering their connection to Bob, she was more than willing to provide the ship.
Now armed with the coordinates and a remarkable vessel, Monkvano and Jararis set off on their journey to Earth.
""")

#Level 8: Jamaica
slow_text_print("After a save landing you have finally arrived back on earth, but it looks a bit weird...")
slow_text_print("You hear a stranger say: Wagwan bossy. Mi name is Agwe. Yuh luk lose or nuh?")

while True:
    slow_text_print("A: Yes, where am I?")
    slow_text_print("B: No, I am good thank you.")
    lvl8_question_one = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')

    if lvl8_question_one == "A":
        slow_text_print("Djoemma: bommmbaaaclaaaatttt. I will answer fi question if you solve me riddle bossman.")
        slow_text_print("A: Tell me the riddle")
        slow_text_print("B: Nevermind I will try to find out my self")
        lvl8_question_two = input("").capitalize()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if lvl8_question_two == "A":
            slow_text_print("Djoemma: Alright listen here.")
            slow_text_print("""I'm a legend of music, with rhythm so grand,
                    In Jamaica, my roots firmly stand.
                    I sing of freedom, love, and good vibes,
                    Reggae's the genre where my spirit thrives.
                    Who am I?""")
            
            while True:
                correct_answer = "Bob Marley"
                enter_answer = input("Enter your answer: ")

                if enter_answer == correct_answer:
                    slow_text_print("You right!")
                    slow_text_print("Agwe: Ok bossman eff yuh wa fi get home yuh muss follow dis road but watch out it crosses a dangerous neighborhood.")
                    slow_text_print("You thank Agwe for his help and continue your journey.")
                    slow_text_print("While you're walking you notice you find yourself in a bad neighbourhood.")
                    slow_text_print("You hear people yelling and running away.")
                    slow_text_print("*BAM* *BAM*")
                    slow_text_print("Jararis: Oh no Monkvano got shot!!!")
                    slow_text_print("What will you do?")

                    while True:
                        slow_text_print("A: Try to save Monkvano.")
                        slow_text_print("B: Run away.")
                        lvl8_question_three =input("").capitalize()
                        os.system('cls' if os.name == 'nt' else 'clear')

                        if lvl8_question_three == "A":
                            slow_text_print("Wow are you also trying to get shot???")
                        elif lvl8_question_three == "B":
                            slow_text_print("You run as fast as you can to not get shot.")
                            break
                    break
                else:
                    slow_text_print("Wrong answer, try again bloodclat.")
            break

        elif lvl8_question_two == "B":
            slow_text_print("Djoemma: Nah wrong choice bossy")
            slow_text_print("*BAM* *BAM*")
            slow_text_print("Jararis: Oh no Monkvano got shot!!!")
            slow_text_print("What will you do?")
            while True:
                slow_text_print("A: Try to save Monkvano.")
                slow_text_print("B: Run away.")
                lvl8_question_three =input("").capitalize()
                os.system('cls' if os.name == 'nt' else 'clear')

                if lvl8_question_three == "A":
                    slow_text_print("Wow are you also trying to get shot???")
                elif lvl8_question_three == "B":
                    slow_text_print("You run as fast as you can to not get shot.")
                    break
            break

    elif lvl8_question_one == "B":
        slow_text_print("Djoemma: Alright bossy.")
        slow_text_print("While you're walking you notice you find yourself in a bad neighbourhood.")
        slow_text_print("You hear people yelling and running away.")
        slow_text_print("*BAM* *BAM*")
        slow_text_print("Jararis: Oh no Monkvano got shot!!!")
        slow_text_print("What will you do?")
        while True:
            slow_text_print("A: Try to save Monkvano.")
            slow_text_print("B: Run away.")
            lvl8_question_three =input("").capitalize()
            os.system('cls' if os.name == 'nt' else 'clear')

            if lvl8_question_three == "A":
                slow_text_print("Wow are you also trying to get shot???")
            elif lvl8_question_three == "B":
                slow_text_print("You run as fast as you can to not get shot.")
                break
        break

slow_text_print("Now you're finally at a safe space.")
slow_text_print("Jararis: wow my best friend just died and I could not save him. Now I need to finish this mission for him.")
slow_text_print("Let's go home...Rotterdam...")

#Level 9: Rotterdam
slow_text_print("You finally arived in Rotterdam South after a long journey. You are so close to the end")
slow_text_print("In the distance you see someone walking towards you.")
slow_text_print("It's 2 euro man!!!")
slow_text_print("He immediately asked you if you have 2 euros")
while True:
    slow_text_print("What should I do?")
    slow_text_print("A: Give him 2 euros.")
    slow_text_print("B: Say you don't have money.")
    lvl9_question_one = input("").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')

    if lvl9_question_one == "A":
        slow_text_print("Yes here 2 euro.")
        slow_text_print("Thank you for the 2 euros. Is there something I can help you with?")
        while True:
            slow_text_print("A: Yes i need to find a way to get to my base")
            slow_text_print("B: No I am good.")
            lvl9_question_two = input("").capitalize()
            os.system('cls' if os.name == 'nt' else 'clear')

            if lvl9_question_two == "A":
                slow_text_print("You need to go ask Djoemma.")
                slow_text_print("While you are walking you suddenly remember something \n Ofcourse I could've asked Djoemma if he knows the way!")
                break
            elif lvl9_question_two == "B":
                slow_text_print("You continue your journey through Rotterdam South.")
                slow_text_print("While you are walking you suddenly remember something \n I could ask Djoemma if he knows the way!")
                break
        break
    elif lvl9_question_one == "B":
        slow_text_print("No sorry I don't have money.")
        slow_text_print("You continue your journey through Rotterdam South.")
        slow_text_print("While you are walking you suddenly remember something \n I could ask Djoemma if he knows the way!")
        break

slow_text_print("You finally found Djoemma, he's chewing on some rat meat.")
slow_text_print("Hey Djoemma can you help me find the way back to my base?")
slow_text_print("Djoemma: Hello brother. Ofcourse I can help you but first you need to play rock paper scissors with me until you win.")

while True:
    player = input("rock, paper, scissor: ")
    opponent =["rock","paper", "scissor"]
    opponent = random.choice(opponent)
    print("opponent: "+ opponent)

    if player == "rock" and opponent=="scissor":
        print("You won")
        break
    elif player == "scissor" and opponent=="paper":
        print("You won")
        break
    elif player == "paper" and opponent=="rock":
        print("You won")
        break
    elif player == "rock" and opponent=="paper":
        print("You lost")
    elif player == "paper" and opponent=="scissor":
        print("You lost")
    elif player == "scissor" and opponent=="rock":
        print("You lost")
    else: 
        print("Draw")

slow_text_print("Djoemma: Here a map to your base. Good luck!")

#Level 10: Homebase
slow_text_print("After a long walk you finally made it to the secret space station base but it looks like you lost the keys.")
slow_text_print("Luckily you have to option to enter a passcode.")
slow_text_print("You remember the passcode was four numbers long and was the zonecode for Rotterdam South")

while True:
    correct_passcode = "5314"
    enter_passcode = input("Enter your passcode: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if enter_passcode == correct_passcode:
        slow_text_print("Access granted!")
        break
    else:
        slow_text_print("Access denied. Incorrect passcode.")

if Lvl3_Question_One == "A":
    slow_text_print("""As Jararis returns to the secret space station base and successfully enters the passcode to secure the rock,
he can't help but feel a sense of relief and accomplishment. The rock, essential for saving humanity, is finally safe and sound. 
But as he turns to leave the room and go back to his daily monkey business, 
a loud alarm suddenly blares throughout the base, red warning lights flashing all around him. The base is under attack!

Jararis is left standing there, clutching the precious rock, as the ground shakes from the impact of the attack. 
The fate of the base, the rock, and Jararis himself hang in the balance. Will he be able to protect the rock and the base from this unexpected threat? 
The adventure is far from over, and Jararis faces a new, dangerous challenge.\n                                                           """)
    os.system('cls' if os.name == 'nt' else 'clear')
          
elif Lvl3_Question_One == "B":
    slow_text_print("""As Jararis stands in the secret space station base, relieved that he has secured the rock, he suddenly feels a cold shiver down his spine. 
His hand, which had been gripping the rock tightly, is now empty. Panic sets in as he frantically searches the room, but the rock is nowhere to be found. It's gone!

His mind races as he tries to retrace his steps. Could he have dropped it somewhere along the way? Did someone or something steal it? 
The fate of humanity hangs in the balance, and Jararis is now faced with a gut-wrenching realization - he might have lost the rock on that alien planet.

Desperation takes over as he contemplates the possibility of having to return to that perilous planet to retrieve the rock. 
The weight of his failure and the uncertainty of the rock's whereabouts leave him in a state of despair.""")
    os.system('cls' if os.name == 'nt' else 'clear')

slow_text_print("To be continued...\n                      ")

os.system('cls' if os.name == 'nt' else 'clear')

#The end
slow_text_print("Thank you for playing Space Monkey! Feel free to play again ;)")
