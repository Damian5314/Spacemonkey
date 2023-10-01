import os 
import random
import time

def slow_text_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

print("Welcome to Space Monkey!\n")
print("You are expected to solve puzzles and riddles to progress through different stages of the game and eventually win.")
print("Please note that your choices will influence the storyline so don't hesitate to play again!")
print("Now let the story begin, have fun!\n")
while True: 
    print("Do you want to start?")
    print("A: Yes")
    print("B: No")

    Start_Answer = input("").capitalize()

    if Start_Answer == "A": 
        break
    else: 
        print("That's fine, whenever you're ready.\n")

os.system('cls' if os.name == 'nt' else 'clear')

#Level 1: Unknown planet
print(
    """Jararis was a specially trained monkey that can talk and who was trained to go to space.
One day he was needed for a space mission to get a special rock to save humanity but when he finally got the item,
An asteroid hit his ship and he crashed down on an unknown planet.\n""")
print("""Jararis: Huh, where am I? 
My head is pounding, and my vision is blurry. I recall flashes of alarm signals and sudden turbulence. 
The last memory I have is looking out the window of my spaceship as I crashed. 
Now I lie here, surrounded by lush green leaves and the sweet scent of tropical flowers.
This is not a place I am familiar with. It's as if I've landed in an entirely different world.
I hear the sounds of unfamiliar creatures and see strange, colorful birds high in the trees. 
Adrenaline rushes through me as I realize I am stranded on this mysterious tropical planet. 
I must find ways to protect myself and explore what this new world has to offer.
I need to go as soon as possible from this planet to save humanity!!
The adventure begins.\n""")

while True:
    print("What should I do?")
    print("A: Get out the ship.")
    print("B: Sit down.")
    question_one = input("").capitalize()

    if question_one == "A":
        print("You got out of the ship.")
        break
    elif question_one == "B":
        print("Grrr I'm hungry, sitting down won't get me anywhere.")

print("You look around and see that you're on a different planet.")
print("Your spaceship is also broken and you must find a way to fix it.")

while True:
    print("Which way should I go?")
    print("A: Let's check out the forest.")
    print("B: Let's walk around the beach.")
    question_two = input("").capitalize()

    if question_two == "A":
        print("You went to check in the forest.")
        break
    elif question_two == "B":
        print("Yararis:I don't like sand. It's coarse ,irritating and it gets everywhere.")

print("When entering the forest , there was a bord that Jararis did not see : Forest of riddles!")
print("""Jararis:The forest is like a giant playground filled with towering trees, so tall they seem to touch the sky.
It smells like wet earth after rain, a refreshing scent. 
There are flowers everywhere, some as big as my head! 
There are flowers of all colors—red, yellow, blue—all over the place. It's like a rainbow on the ground.
\n""")

print("""Jararis: As I ventured through the lush forest, my eyes were drawn to a towering banana tree.
Its slender trunk reached up into the sky, and at the top, a cluster of bananas hung. 
These bananas were enormous, larger than any I had ever come across in my life.                       
I felt a mix of excitement and hunger.
I wanted to taste the delicious banana and savor the sweet taste of it. 
However, the bananas seemed unreachable, swaying high above the ground.\n""")

print("""Beside the tree, I noticed a weathered wooden sign. 
It was weathered and had some faded writing.
I strained my eyes to read: "If you wish to feast on bananas delights, solve the puzzle and prove your might."
 """)

print("Answer at least one questions correctly to make the bananas fall!")

play_count = 0

while play_count < 4:
    question_1 = ("Tuana needs 22 cartons of space-milk from the space-market."
                  " She can only carry 4 cartons at a time.\nHow many trips does she need to make to the space-market?")
    answer_1 = "6"

    question_2 = ("Raees is twelve years old, and he is three times as old as his brother. "
                  "How old will Fernando be when he is twice as old as his brother?")
    answer_2 = "8"

    question_3 = "What has to be broken before you can use it?"
    possible_answers_3 = ["egg", "grenade", "heart", "glow stick", "seal", "save", "crust", "seed", "rule",
                          "word", "dream", "solution", "trust", "horse", "code", "habit", "bar"]

    bananas_fallen = False

    while True:
        print("\nQuestion 1:", question_1)
        user_answer_1 = input("Your answer for question 1: ").strip().lower()

        print("\nQuestion 2:", question_2)
        user_answer_2 = input("Your answer for question 2: ").strip().lower()

        print("\nQuestion 3:", question_3)
        user_answer_3 = input("Your answer for question 3: ").lower()

        correct_answers = 0

        if "6" in user_answer_1:
            correct_answers += 1
        if "8" in user_answer_2:
            correct_answers += 1
        if any(word in user_answer_3 for word in possible_answers_3):
            correct_answers += 1

        if correct_answers >= 1:
            print("\nCongratulations! You answered at least two questions correctly.")
            print("Bananas fall from the tree!")
            print("""The correct answers were: q1: 6, q2: 8, and q3 egg, grenade, glow stick, seal, save, crust, seed, rule,
word, dream, solution, trust, horse, code, habit, bar.\n""")
            bananas_fallen = True
            break
        else:
            print("\nUnfortunately, you didn't answer at least two questions correctly. Try again.")
            play_count += 1

    if bananas_fallen:
        print("You now have enough food to last for a while on this planet.")
        print("Jararis: Yeah, I did it! Bananas are coming to me, baby!!\n")
        break

    if play_count >= 2:
        print("Unfortunately, you tried too many times. The answers were:")
        print('q1: 6, q2: 8, q3: egg')
        print('Lararis:Ahh i am so hungry\n')

print("""Jararis: Feeling energized after enjoying the delicious bananas, I knew I had to get back on track.
It reminds me of a friend Elias, he is also back on track.""")
print("I needed to find the missing parts of my spaceship scattered across the island.")
print("Equipped with determination and a belly full of bananas, I ventured deeper into the forest.\n")

print("The forest was vast and mysterious. Tall trees and dense vegetation made it challenging to navigate.")
print("But I was determent. I knew my spaceship parts were somewhere out here, waiting to be found.")

print("""After hours of searching, I stumbled upon an unusual clearing in the forest.
In the middle of the clearing lay an important repair kit and the navigation of my ship.
But the problem was how can I get there. Because I saw only a bridge connecting to the clearing      
      \n""")

print("""jararis: As I approached the bridge, I noticed a massive barrier blocking the way.
It seemed impossible to proceed.
Upon closer inspection, I discovered a control panel with three slots for riddles.
To raise the barrier and access the bridge, I had to solve three riddles: an easy riddle, a medium riddle, 
and a difficult riddle, or find a man in the forest named Jango  that now has the answers to the riddles.
The fate of my journey depended on my wit and the answers I could provide.
I took a deep breath, ready to face the challenge.\n""")

# yeahh tog
riddles = {
    'easy': "It's an animal that has four legs, white with black stripes. What is it?",
    'medium': "Boe, boe, boe. What am I?",
    'difficult': "It's given to you by your parent, it's yours, but others use it more than you use it. What am I?"
}

answers = {
    'easy': 'zebra',
    'medium': 'cow',
    'difficult': ["name", "your name", "my name", "a name", "advice",
                  "education", "time", "last name", "dna",
                  "manners", "influence", "reputation",
                  "surname", "genes", "culture",
                  "legacy", "traditions", "heritage",
                  "knowledge", "example", "experience", "support", "legacy"]
}


def ask_riddle(difficulty):
    return riddles.get(difficulty.lower(), "Invalid difficulty level")


def validate_answer(difficulty, answer):
    return answer.lower() in answers.get(difficulty.lower(), [])


# locomotief
print("Options:")
print("A. Attempt to solve the riddles.")
print("B. Look for a man named Jango for help.")

player_choice = input("Enter your choice (A or B): ").lower()

if player_choice == "a":
    print("You choose option A to attempt to solve the riddles.")

    continue_with_riddles = True

    for difficulty_level in ['easy', 'medium', 'difficult']:
        if not continue_with_riddles:
            break

        print(f"\nRiddle ({difficulty_level.capitalize()}): {ask_riddle(difficulty_level)}")

        attempts = 0
        max_attempts_easy_medium = 3
        max_attempts_difficult = 3

        while attempts < (
                max_attempts_easy_medium if difficulty_level in ['easy', 'medium'] else max_attempts_difficult):
            user_answer = input("Your answer: ").lower()

            if validate_answer(difficulty_level, user_answer):
                if difficulty_level == 'difficult':
                    print("\nCorrect answer! The barrier will open now. Well done!\n")
                    continue_with_riddles = False
                    break
                else:
                    print("Correct answer! The barrier is slowly lifting...")
                    break

            else:
                attempts += 1
                remaining_attempts = max_attempts_easy_medium if difficulty_level in ['easy',
                                                                                      'medium'] else (
                    max_attempts_difficult)
                print(f"Incorrect answer. Attempts left: {remaining_attempts - attempts}")

                if attempts == remaining_attempts:
                    print(f"You've exhausted all attempts for this {difficulty_level} riddle.")
                    retry_option = input("Would you like to retry (R) or stop the puzzle (S)? ").lower()
                    if retry_option == "r":
                        print(f"You decide to retry the {difficulty_level} riddle.")
                        attempts = 0
                    elif retry_option == "s":
                        print("You decide to stop the puzzle and go find jango.\n")
                        continue_with_riddles = False
                        break
                    else:
                        print("Invalid choice. Please enter 'R' to retry or 'S' to stop the puzzle.")

elif player_choice == "b":
    print("\nYou chose option B to look for a man named Jango.")
    print("You venture further into the forest in search of Jango.")

# Voeg hier de controle voor "S" toe
elif player_choice == "s":
    print("\nYou chose to skip. Moving on to the next step.")

else:
    print("Invalid choice. Please choose either A, B, or S.")

while True:
    if player_choice == "b":
        print("")

    print(
        "Jararis: I see the dense trees and the dimming light makes it an "
        "eerie journey.")
    print("After a while, I hear rustling in the bushes and encounter a man who introduces himself as Jango.")
    print("Jararis: He was a men with three eyes.")
    print("I had never seen some one like him.")
    print("I asked a lot of questions to him. But he didn't want to answer them.")
    print("""But when I told him about the riddles by the bridge.
He said the following I can help you with the riddles, but first, I need a favor. 
Can you get one of the following things: toilet paper, green apple, cigarette or my glasses.
Find it for me, and I'll provide you with the answers to the riddles.""")
    break

while True:
    jango_favor_choice = input("\nDo you accept Jango's favor? (Yes/No): ")

    if jango_favor_choice.lower() == "yes":
        print("\nYou agree to help Jango and  to find things on his list.")
        break
    else:
        print("\nJararis: We need this deal or else we won't get of this planet.")

lvl1_outer_loop = True
while lvl1_outer_loop:
    print("Which item will you try to find for Jango?")
    print("A: Toilet paper")
    print("B: Green apple")
    print("C: Glasses")
    print("D: Cigarette")
    item_choice = input("Your choice (A, B, C, or D): ").capitalize()

    if item_choice == "A":
        print("\nYou decide to find toilet paper for Jango.")
        print("You search the nearby areas and come across an abandoned campsite.")
        print("A: Go to the table")
        print("B: Look in the tent")
        question_toilet = input("Your choice (A or B): ").capitalize()

        if question_toilet == 'A':
            print("\nThere is a closet here and a barbecue set.")
            while True:
                print("A: Should I look in the closet")
                print("B: Should I look in the barbecue set")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    print("\nAhhhh, a crazy black doll!")
                    continue
                elif closet_choice == 'B':
                    print("\nYes, there it is! We finally found the toilet paper. Let's head back to Jango.")
                    print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_toilet == 'B':
            print("\nWow, there is a toilet here but no paper. Let's go to the table.")
            while True:
                print("A: Look in the area of the table")
                print("B: Check the tent")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    print("\nThere is a closet here and a barbecue set.")
                    while True:
                        print("A: Should I look in the closet")
                        print("B: Should I look in the barbecue set")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            print("\nAhhhh, a crazy black doll!")
                            continue
                        elif closet_choice == 'B':
                            print(
                                "\nYes, there it is! We finally found the toilet paper. Let's head back to Jango.")
                            print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")

                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    print("\nHe he, I finally found this toilet paper!")
                    print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")

                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            print("Invalid choice. Please select A or B.")

    elif item_choice == "B":
        print("\nYou decide to venture into the forest to look for a green apple.")
        print("You explore the forest and spot an apple tree in the distance.")
        print("As you approach the tree, you find a delicious green apple.")
        print("You pick the apple and head back to Jango.")
        print("finally after you got to jango and gave his stuff.He helped you open the barrier.")

        lvl1_outer_loop = False
        c = """After you found the Green apple that jango needed, he opened the barrier for you."""
        break
    elif item_choice == "C":
        print("\nYou decide to find the glasses for Jango.")
        print("You search the nearby areas and come across two paths.")
        print('Each path lead to another way.')
        print("A: Hmmm, should I take the left path. ")
        print("B: Oei oei, should I take the right path.")
        question_glasses = input("Your choice (A or B): ").capitalize()

        if question_glasses == 'A':
            print("\nThere is a house and a barn.")
            while True:
                print("A: Should I look in the house.")
                print("B: Should I look in the barn.")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    print("\nAhhh, f**k I see a huge dog for the house!")
                    print("No way I will go there.")
                    continue
                elif closet_choice == 'B':
                    print("\nYes, there it is! We finally found the glasses. Let's head back to Jango.")
                    print("finally after you got to jango and gave his stuff.He helped you open the barrier.")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            print("\nJararis: nahh i see spooky shit there and no banana there.")
            while True:
                print("A:Hmmm, left is good ")
                print("B:Right is to scary! I'm a wimp!")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    print("\nThere is a house and a barn here")
                    while True:
                        print("A: Should I look in the house.")
                        print("B: Should I look in the barn.")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            print("\nAhhh, f**k I see a huge dog for the house.")
                            print("Nah now way I'm going there!")
                            continue
                        elif closet_choice == 'B':
                            print(
                                "\nYes, there it is! We finally found the glasses. Let's head back to Jango.")
                            print("finally after you got to jango and gave his stuff.He helped you open the barrier.")

                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    print("\nHe he, I finally found this stupid glasses!")
                    print("finally after you got to jango and gave his stuff.He helped you open the barrier.")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            print("Invalid choice. Please select A or B.")
    elif item_choice == "D":
        print("\nYou decide to find the cigarette for Jango.")
        print("You search the nearby areas and come across a three.")
        print("A:Quickly climb up the tree to explore the area. ")
        print("B:Pee on the three.")
        question_glasses = input("Your choice (A or B): ").capitalize()

        if question_glasses == 'A':
            print("\njararis: Wow this is high.")
            print("I think I see a bird's nest. ")
            while True:
                print("A: Lets go climb higher.")
                print("B: Go to the bird nest.")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    print("\nYou misjudged your steps, now you going to fall down Stupid Monkey.Try again ")
                    continue
                elif closet_choice == 'B':
                    print("\nYes, there it is! We finally found the cigarette in the nest.Let's head back to Jango.")
                    print("finally after you got to jango and gave his stuff.He helped you open the barrier.")

                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            print("\nJararis: Ahh I a freaking spider bit my little monkey while peeing.")
            while True:
                print("A:Quickly climb up the tree to explore the area. ")
                print("B:Pee on the three.")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    print("\nI see a bird nest")
                    while True:
                        print("A:Lets go climb higher.")
                        print("B:Go to the bird nest.")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            print("\nYou misjudged your steps, now you going to fall down Stupid Monkey")
                            continue
                        elif closet_choice == 'B':
                            print(
                                "\nYes, there it is! We finally found the cigarette. Let's head back to Jango.")
                            print("finally after you got to jango and gave his stuff.He helped you open the barrier.")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    print("\nHe he, I finally found this stupid cigarette"
                          "!")
                    print("finally after you got tho jango and gave his stuff.He helped you open the barrier.")

                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            print("Invalid choice. Please select A or B.\n")

bridge = ("""Jararis: Yes we did it!!
Now we can get all of the ship stuff back and repair the ship.\n
After working for hours jararis finally repaired the ship with his repair kit.
But he realized that he had no fuel to fly.
In his quest for fuel, Jararis explored the planet further.
As he walked through the dense forest, he stumbled upon peculiar markings on the trees.
These markings seemed to be a clue leading to a temple.\n
Eager to find fuel, Jararis followed the markings deep into the forest, leading him to a mysterious temple.
As he stepped inside, the temple seemed to come alive, narrating the tale of the legendary Super Special Banan, 
an extraordinary fruit with unmatched energy that can be used as fuel for the spaceship.
""")
print(bridge)
b = ("""Intrigued by the temple's message, Jararis proceeded further and encountered a road in the temple.
There was a man at the end of the road in the temple. The man was very happy to see someone enter his temple.
Because nobody had entered in a long time.
He offered jararis to play a game.
If you would like to play the game with me then I will hand you a super banana.
""")
print(b)
while True:
    print('Offer play hangmen for super banana fuel')
    print("A: Take this offer")
    print("B: Decline this offer?")
    offer = input('').capitalize()
    if offer == "A":
        print("Lets beat this guy, oehh oehh ah ah ")
        break
    elif offer == "B":
        print('We need this change or we will die on this planet.')
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

    print("Welcome to Hangman - Banana Edition!")
    print("Try to guess the word related to bananas, space and animals.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", ' '.join(guessed_letters) if guessed_letters else "None")
        print("Word:", ' '.join(word_display))

        hangman_idx = 8 - attempts
        if hangman_idx >= 0 and hangman_idx < len(hangman_art):
            print(hangman_art[hangman_idx])

        guess = input("Enter a letter or the whole word: ").lower()

        if len(guess) == 1:  # Guessing a letter
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word_to_guess:
                print("Good guess!")
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        word_display[i] = guess
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                attempts -= 1
                guessed_letters.append(guess)
        elif len(guess) == len(word_to_guess) and guess.isalpha():  # Guessing the whole word
            if guess == word_to_guess:
                print("Congratulations! You guessed the word:", word_to_guess)
                return True
            else:
                print("Wrong guess!")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a valid letter or the whole word.")

        if "_" not in word_display:
            print("Congratulations! You guessed the word:", word_to_guess)
            return True

    print("You ran out of attempts. The word was:", word_to_guess)
    return False


print("We need to win this game to get the super banana!")
while True:
    won = play_hangman()

    if won:
        print("Congratulations! You won the game.\n")
        break
    else:
        print("Game over. You can try again.")

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nWe need to play this game to win the super banana!\n")

print("Finally, after what seemed like an eternity, we got all the things we need to go out of this planet.")
print("My spaceship was ready.")
print("I bid farewell to the Forest of Riddles, a place that had tested my problem solving skills.")
print("With a heart full of gratitude, I boarded my spaceship and soared into the cosmic unknown.")
print("And so, my adventure continued as I ventured into the depths of the universe, heading back to earth!!\n")

print("""The journey to Earth was expected to take 14 days.
After 2 days of tending to ship duties and relaxing, something unexpected happened. 
I looked at the navigation and it said that the estimated time is still 14 days to Earth.
There was a malfunction in the navigation. I was heading somewhere else. Suddenly I felt a strange vibration in the ship.
I noticed a peculiar, compelling light pulling my ship upwards.
My spaceship's engines struggled against the force of this strange light, but it was too powerful. 
Before I knew it, I was being drawn into a massive alien spacecraft.
The ship's door opened, and I found myself face to face with aliens who had abducted me.
I was hit and lost consciousness.""")

  

#Level 2: Alien ship
print("You've been abducted by aliens.")
print("Jararis: I should probably try to escape since they're planning on keeping you imprisoned and steal the rock.")
print("You look around you and see three items: Spoon, Toilet paper, Alien playboy magazine.")

while True:
    print("Which item will you try to use to escape.")
    print("A: Spoon")
    print("B: Toilet paper")
    print("C: Alien playboy magazine")
    Lvl2_Question_One = input("").capitalize()
    if Lvl2_Question_One == "A":
        print("You sharpen the edge of the spoon against the wall making it something like a knife.")
        print("A Guard is stupid enough to walk close to the iron bars of your jailcell, think fast.")
        print("What will you do?")
        print("A: Pull him close and stab him in the neck")
        print("B: Do nothing and rot in a cell for the rest of your life like a sad little monkey.")
        Lvl2_Question_Two = input("").capitalize()
        if Lvl2_Question_Two == "A":
            print("HE MANAGED TO BLOCK IT, THINK FAST.")
            print("A: Grab his gun and shoot him in the head.")
            print("B: Grab his neck and choke him to death")
            Lvl2_Question_Two_One = input("").capitalize()
            if Lvl2_Question_Two_One == "A":
                print("You try to shoot him but his gun was on safety mode,\n He runs off for backup and eventually you get publicly executed.")
                print("Try an alternative")
                break

            elif Lvl2_Question_Two_One == "B":
                print("You successfully choke him to death,\nAllowing you to grab his keys and silently sneak of the Ship")
                break

            else:
                print("Pick eiter A or B!!!!!!")

        elif Lvl2_Question_Two == "B": 
            print ("You stay in jail and rot away until you die...")
            print("Let's try the more logical answer this time don't you think? :D\n(No but seriously, why would you let that chance slide ._.)")
            break
        
        else:
            print("Pick a or b")

    elif Lvl2_Question_One == "B":
        print("You use the Toilet paper to clog up your toilet.")
        print("A guard comes in trying to unclog the toilet, and leaves the door open like an idiot (lol)")
        print("What will you do?")
        print("A: You silently steal his spare key out of his back pocket.")
        print("B: You sneak out as he's trying to unclog the toilet.")
        Lvl2_Question_Three = input("").capitalize()
        if Lvl2_Question_Three == "A":
            print("You wait for him to fix the toilet and walk out.")
            print("When the coast is clear you sneak out,")
            print("As you're running you see a guard, he notices you too.")
            print("Act fast")
            print("A: Run away!")
            print("B: Fight him!")
            Lvl2_Question_Three_One = input("").capitalize()
            if Lvl2_Question_Three_One == "A":
                print("You turn your back to him and he shoots you in the back of your head.")
                print("(Why did you think that would work lol??)")
                        
            elif Lvl2_Question_Three_One == "B":
                print("You quickly run towards him before he could react,\n and use some super advanced monkey ninja move to kill him and get off the spaceship.")
                break
            else:
                print("Pick between A or B :()")

        elif Lvl2_Question_Three == "B":
            print("Long story short, you're a monkey :) you climb up inside the air conditioning system and safely escape the ship.")

        else:
            print("PICK BETWEEN A OR B YOU MONKEY!")
               
    elif Lvl2_Question_One == "C":
        print("You use the magazine to distract him and steal his keys,\nBut you get distracted aswell and he notices that you try to steal the keys (You're executed, if only you didn't have such a dirty mind)")

    else:
        print("PICK BETWEEN A, B OR C >:(")
        
#Level 3: Alien planet
print("You have succesfully escaped the alien spaceship but you are now on their planet.")
print("You quickly go hiding because the whole planet is filled with the hostile aliens.")
print("Your ship is still on the big alien ship but there is also an other alien ship in sight.")

while True:
    print("What will you do?")
    print("A: Try to get back your own ship.")
    print("B: Try to steal the alien ship.")
    Lvl3_Question_One = input("").capitalize()

    if Lvl3_Question_One == "A":
        print("You go back on the alien ship to get your ship back")
        print("(You just escaped, you really don't know what you want... -_-)")
        break
    elif Lvl3_Question_One == "B":
        print("Jararis: Hmm I feel like I'm forgetting something, but screw that.")
        break


outer_loop = True
while outer_loop:
    if Lvl3_Question_One == "A":
        print("You hop into the vents of the spaceship")
        print("As you're silently crawling through the vents you see a set of lasers moving towards you.")
        print("Probably a defence mechanism designed for sneaky monkeys like you...")
        print("Anyways THINK FAST! You look up and see a box, when you open it you see 4 wires.")
        print("Which wire will you snap in order to stop the lazers from coming towards you?")
        print("A: Red")
        print("B: Green")
        print("C: Blue")
        print("D: Yellow")
        Lvl3_Question_TwoA = input("").capitalize()
        while True:
            if Lvl3_Question_TwoA == "D":
                print("Well aren't you a lucky monkey :D")
                print("The lasers turned off!")
                outer_loop = False
                break
                        
            elif Lvl3_Question_TwoA == "A" or Lvl3_Question_TwoA == "B" or Lvl3_Question_TwoA == "C":
                print("R.I.P. The wires moved even faster and you didn't move in time...")
                print("Try again.")
                break

            else:
                print("Are you even trying to survive?")
                print("Pick between A, B, C OR D!")
                break

    elif Lvl3_Question_One == "B":
        print("You silently sneak over towards the alien ship")
        print("When you get the you see that there is a lock on the ships door")
        print("It seems as if you need to translate their language to yours...")
        print("Language: .. .----. -- / .- / ... - ..- .--. .. -.. / .-.. .. - - .-.. . / -- --- -. -.- . -.-- -.-.--")
        print("Jararis: Hmmm, this sure does look like morse code")
        Lvl3_Question_TwoB = input("Please enter the password: ").upper()
        while True:
            if Lvl3_Question_TwoB == "I'M A STUPID LITTLE MONKEY!":
                print("Nice! The door unlocked and you fly off without any problems!")
                outer_loop = False
                break
            else:
                print("You took too long to unlock the door and got noticed by a guard")
                print("You got shot, and died...")
                break

second_outer_loop = True
while second_outer_loop:
    if Lvl3_Question_TwoB == "I'M A STUPID LITTLE MONKEY!":
        print("Suddenly you get a alarm message on the ships dashboard.")
        print("Jararis: Ah yes I'm flying in a registered ship so I probably need some sort of identification.")
        print("Two messages pop up:")
        print("6x - 8 = 4x + 4")
        Lvl3_Question_ThreeB = input("Please enter the password x = ")
        while True:
            if Lvl3_Question_ThreeB == "6":
                print("Great, those dumb aliens fully believe you're one of them.")
                print("You fly off into outer space...")
                second_outer_loop = False
                break
            
            elif Lvl3_Question_ThreeB < 6 or Lvl3_Question_ThreeB > 6:
                print("Wrong answer")

            else:
                print("Come on this is basic math!")
                print("What did you even do in math class...")

    elif Lvl3_Question_TwoA == "D":
        print("You climb through the vents towards the ships hangar")
        print("You're finally reunited with your ship but see that there is a lock on the ship.")
        print("It seems as if you need to translate their language to yours...")
        print("Language: - ..- .- -. .- / -.- .- -. / -. .. . - / .-. .. .--- -.. . -. / .... .- .... .- -.-.--")
        print("Jararis: Hmmm, this sure does look like morse code")
        Lvl3_Question_ThreeA = input("Please enter the password: ").upper()
        if Lvl3_Question_ThreeA == "TUANA KAN NIET RIJDEN HAHA!":
            print("Jararis: Nice! The door unlocked, that was easier than I thought!")
            print("I do wonder who Tuana is though...")
            print("You fly off into outerspace wondering where else this adventure might lead you to...")
            break
        else:
            print("You took too long to unlock the door and got noticed by a guard")
            print("You got shot, and died...")
            break

#Level 4:Elysium Prime
print("As you're wandering through the vast void of outer space, not knowing where to go all you can think of are bananas...")
print("You're going to have to make a stop very soon as you're running out of food")
print("You check the space map and see your only hope is an interstellar space station called Elysium Prime")
print("You decide to give it a shot as it's your only hope...")

Third_outer_loop = True
while Third_outer_loop:
    print("You've landed and managed to find a restaurant")
    print("You look around and see that the space station is filled with different alien races")
    print("Luckily you stole some money from those alien guards so you've got enough for one meal")
    print("What would you like to eat?")
    print("A: Spicy Banana Soup")
    print("B: Strange looking tentacles")
    print("C: A bowl of spiky looking fruits")
    Lvl4_Question_Food = input("").capitalize()
    while True:
        if Lvl4_Question_Food == "A":
            print("You couldn't resist your monkey urges and obviously picked the Spicy Banana Soup")
            print("You finish the WHOLE bowl in 3 minutes! (It was amazing...)")
            Third_outer_loop = False
            break

        elif Lvl4_Question_Food == "B":
            print("You decided to go for something new huh?")
            print("(How did you not pick the Spicy Banana Soup??? Are you even a real monkey? ._.)")
            print("You finish your plate pretty fast, the food wasn't that bad")
            Third_outer_loop = False
            break

        elif Lvl4_Question_Food == "C":
            print("Why did you pick this, are you trying to starve Jararis?")
            print("Jararis managed to eat some of the food after removing all the spikes")
            print("Jararis: That didn't really taste that good but food is food I guess...")
            Third_outer_loop = False
            break

        else:
            print("Pick between A,B or C")
            print("(Only weirdos don't :D)")

Fourth_outer_loop = True
while Fourth_outer_loop: 
    if Lvl4_Question_Food == "A":
        print("Jararis: I should probably get moving now")
        print("What will you do?")
        print("A: Start looking for usefull things")
        print("B: Stay seated...")
        Lvl4_Question_FoodOne = input("").capitalize()
        while True:
            if Lvl4_Question_FoodOne == "A":
                print("You get up and start exploring the space station")
                Fourth_outer_loop = False
                break

            elif Lvl4_Question_FoodOne == "B":
                print("That ain't going to get you far is it")
                print("Perhaps you should pick a more serious answer :O")
                print("(Seriously, why would you do that to Jararis you monster >:/ )")
                break

    elif Lvl4_Question_Food == "B":
        print("Jararis: I should probably get moving now")
        print("What will you do?")
        print("A: Start looking for usefull things")
        print("B: Stay seated...")
        Lvl4_Question_FoodTwo = input("").capitalize()
        while True:
            if Lvl4_Question_FoodTwo == "A":
                print("You get up and start exploring the space station")
                Fourth_outer_loop = False
                break

            elif Lvl4_Question_FoodTwo == "B":
                print("That ain't going to get you far is it")
                print("Perhaps you should pick a more serious answer :O")
                print("(Seriously, why would you do that to Jararis you monster >:/ )")
                break

    elif Lvl4_Question_Food == "C":
        print("Jararis: I should probably get moving now")
        print("What will you do?")
        print("A: Start looking for usefull things")
        print("B: Stay seated...")
        Lvl4_Question_FoodThree = input("").capitalize()
        while True:
            if Lvl4_Question_FoodThree == "A":
                print("You get up and start exploring the space station")
                Fourth_outer_loop = False
                break

            elif Lvl4_Question_FoodThree == "B":
                print("That ain't going to get you far is it")
                print("Perhaps you should pick a more serious answer :O")
                print("(Seriously, why would you do that to Jararis you monster >:/ )")
                break


        
Fifth_outer_loop = True
while Fifth_outer_loop:
    print("Jararis: This is nice, finally no annoying alien guards that chase me around...")
    print("Suddenly you hear a loud screaming voice behind you")
    print("Alien guard: - .... . .-. . / .... . / .. ... --..-- / --. . - / - .... .- - / ... - ..- .--. .. -.. / -- --- -. -.- . -.-- -.-.--")
    print("Jararis: YOU'VE GOT TO BE KIDDING ME!!! (What is this idiot even saying anyways...)")
    print("The guards start charging towards you, you have to find a hiding spot.")
    print("You have 2 options:")
    print("A: You hide in the toilets")
    print("B: You hide in a big crowd of people")
    Lvl4_Question_One = input("").capitalize()
    while True:
        if Lvl4_Question_One == "A":
            print("You run over to the toilers and quickly lock the door. Not too long after you hear the guards charge in and check if you're there")
            print("Alien Guard: --. --- -.. / .. / .... .- - . / -- --- -. -.- . -.-- ... -.-.--")
            print("Lucky for you, they don't check all the toilets and just leave. (These guards are almost as stupid as you! XD)")
            print("Suddenly you feel your stomach starting to burn like CRAZY")
            if Lvl4_Question_Food == "A":
                print("Jararis: THAT SPICY BANANA SOUP REALLY WASN'T A GREAT IDEA NOW THAT I THINK ABOUT IT")
                print("Jararis now faces his greatest enemy so far on this crazy adventure, The Toilet...")
                print("After fighting like a warrior for 4 HOURS STRAIGHT, Jararis has lost a lot...")
                print("He's thirsty, hungry and last but not least... has no toilet paper")
                Fifth_outer_loop = False
                break

            elif Lvl4_Question_Food == "B":
                print("Jararis: THOSE WEIRD TENTACLES WE'RE A BAD IDEA WHY WOULD I EAT THAT IN THE FIRST PLACE")
                print("Jararis now faces his greatest enemy so far on this crazy adventure, The Toilet...")
                print("After fighting like a warrior for 4 HOURS STRAIGHT, Jararis has lost a lot...")
                print("He's thirsty, hungry and last but not least... has no toilet paper")
                Fifth_outer_loop = False
                break
            
            elif Lvl4_Question_Food == "C":
                print("Jararis: WHY DID I EAT THOSE STUPID SPIKE FRUITS THEY LITERALLY LOOKED LIKE A MORNING STAR")
                print("(Morning star: A club with a heavy spiked head, sometimes attached to the handle by a chain, this weapon was mostly used in medieval times.)")
                print("Jararis now faces his greatest enemy so far on this crazy adventure, The Toilet...")
                print("After fighting like a warrior for 4 HOURS STRAIGHT, Jararis has lost a lot...")
                print("He's thirsty, hungry and last but not least... has no toilet paper")
                Fifth_outer_loop = False
                break

        elif Lvl4_Question_One == "B":
            print("As you're quietly walking with the crowd of people you suddenly get tasered in the back")
            print("You pass out...")
            print("(You will be tortured for the rest of your life, unlucky lol)")
            break

print("After 4 hours someone else finally enters the toilet")
print("Jararis: Hey man could you please hand me some toilet paper?")
print("Stranger: DAMN it smells like a dead body in here!")
print("Jararis (In an ashamed voice): Please just hand me some toilet paper...")
print("You finish all the stinky business on the toilet and open the door")
print("There he was Monkvano, with his deep, soulful eyes and tuft of unruly fur, he looked back at you with a blend of curiosity and amusement.") 
print("He was no ordinary monkey; he was a resident of Elysium Prime, known for his uncanny ability to navigate the city's intricate maze of walkways and rooftops.")
print("Jararis: Y-y-you're like me!?")
print("Monkvano: Y-y-you're like me!?")

Sixth_outer_loop = True
while Sixth_outer_loop: 
    print("Do you ask Monkvano to help you?")
    print("A: Yes")
    print("B: No")
    Lvl4_Question_Two = input("").capitalize()
    while True:
        if Lvl4_Question_Two == "A":
            print("Jararis: Do you know how to get back home? I really need to get back home!")
            print("Monkvano: Of course my fellow monkey brother, we have to help each other out ain't that right")
            print("Jararis: Could you try to keep me out of sight of those scary Alien Guards though, I think they don't really like me...")
            print("Monkvano: Oh yeah same for some reason I've been getting chased around all day")
            print("Monkvano: I think there's a criminal monkey on Elysium Prime which they're trying to catch right now")
            print("Jararis: Yeah let's just make sure we avoid them...")
            Sixth_outer_loop = False
            break

        elif Lvl4_Question_Two == "B":
            print("After a long talk about how tasty bananas en peanuts are you both part ways.")
            print("(You get lost on Elysium Prime and the Alien guards manage to arrest you after a while.)")
            print("(WHY WOULDN'T YOU JUST ASK THAT BEAUTIFUL MONKEY MONKVANO FOR HELP?)")
            break

print("You and Monkvano get to the ship and head into out space again")
print("After flying through space for a while, you and monkvano finally arive 'home'")
print("(You also farted a lot during the trip, smelly little monkey XD)")

#Level 5: Banana Haven
print("You and Monkvano finally landed.")
print("Wow this place looks beautifull. Look at those trees and waterfalls!")
print("But wait...")
print("Are these my...my family???")
print("Jararis: Monkvano where on earth are we?")
print("Monkvano: Earth? This is Banana Haven, Home right?")
print("\nThe locals of Banana Haven seem apprehensive, eyeing you and Monkvano with suspicion.")
print("It appears that they are not thrilled to have outsiders on their beloved planet.")
print("Jararis: Wow Monkvano my home is earth not this planet! And why are all these people looking mad at us?")
print("Monkvano: To be honest with you Jararis, I am exhiled from this planet.")
print("Jararis: Exhiled? What did you do to get exhiled?")
print("Monkvano: My mother is the queen of this planet and yeah...")

while True:
    print("A: We must find your mother, maybe she can help me get off this planet again")
    print("B: What do you mean with yeah?")
    lvl5_question_one = input("").capitalize()

    if lvl5_question_one == "A":
        print("Monkvano: Wowwww are you sure you want to go to her?")
        print("Jararis: Yes because I need to get to earth.")
        break

    elif lvl5_question_one == "B":
        print("Monkvano: yeah she exhiled me for no reason. That is just how she works I guess...")
        print("Jararis: Oh Ok. I need to get of this planet asap.")
        break

print("Monkvano: Well if I get you to her you need to take me with you because I also don't want to stay here.")

while True:
    print("A: Alright we have a deal.")
    print("B: No I am not taking you with me")
    lvl5_question_two = input("").capitalize()

    if lvl5_question_two == "A":
        print("Monkvano: Yes let's go!")
        break

    elif lvl5_question_two == "B":
        print("Monkvano: Then I am not taking you to her.")
        print("Maybe you should help him because he tried to help you.")

print("After a lot of walking and swinging you reached Monkvano's mother. The Monkey Queen.")
print("Monkey Queen: Well well well little Monkvano is back and he brought a little friend with him.")
print("Monkvano: Hello mother. I am not here to make amends.")
print("Monkey Queen: Ok son. What do you want?")
print("Monkvano: Can you help me and Jararis to get to earth.")
print("Monkey Queen: If you want help, your monkey friend must first beat me at coconut throwing.")

while True:
    slow_text_print("A: Let's play Queen")
    slow_text_print("B: No I don't have time for games.")
    lvl5_question_three = input("").capitalize()

    if lvl5_question_three == "A":
        slow_text_print("Monkvano: No we don't have time for that. Spare us for this time.")
        break

    elif lvl5_question_three == "B":
        slow_text_print("Monkvano: Please mother we don't have time for that. Spare us for this time.")
        break

print("Monkey Queen: You are lucky...")
print("Monkey Queen: I dont know how to get to earth but I know someone who does.")
print("Monkey Queen: He lives on Dwarfmania.")

#Level 6: Dwarfmania
print("""Monkvano mother kindly explained that she didn't know where Earth was. However, she mentioned an old monkey  
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

print("Welcome in Bob Monkey trial of death")
print("Survive the parkour and you can enter Bob Monkey's house.")

lvl1_outer_loop = True
while lvl1_outer_loop:
    print("Which parkour will we go?")
    print("A: Dragon slayer")
    print("B: Dwarf  slayer")
    print("C: Seductive slayer")
    print("D: Monkey slayer")
    item_choice = input("Your choice (A, B, C, or D): ").capitalize()

    if item_choice == "A":
        print("\nYou decide to go for the Dragon slayer parkour.")
        print("You walk straight in the parkour you see two paths:")
        print("A: Take left path")
        print("B: Take right path")
        question_toilet = input("Your choice (A or B): ").capitalize()

        if question_toilet == 'A':
            print("\n You see holes on the ground.")
            while True:
                print("A: Run straight as a crazy gorilla")
                print("B: Step back, because you a b*tch")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    print("\nAhhhh, fire came out of the holes!You and monkvano died")
                    print("Try again")
                    continue
                elif closet_choice == 'B':
                    print("\nJararis and Monkvano: yesss we made it across the parkour.")
                    print("Lets goo to Bob fuc***ng Monkey.")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_toilet == 'B':
            print("\nJararis and  monkvano: Blehhhh, you monkeys died of extreme heat")
            print("Try again")
            while True:
                print("A: Take left path")
                print("B: Take right path")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    print("\nYou see holes in the ground!.")
                    while True:
                        print("A: Run straight as a crazy gorilla")
                        print("B: Step back, because you a b*tch")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            print("\n Ahhhh, fire came out of the holes!You and monkvano died")
                            print("Try again")
                            continue
                        elif closet_choice == 'B':
                            print("\n Jararis and Monkvano: yesss we made it across the parkour.")
                            print("Lets goo to Bob fuc***ng Monkey.")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    print("\n Jararis and Monkvano: yesss we made it across the parkour.")
                    print("Lets goo to Bob fuc***ng Monkey.")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            print("Invalid choice. Please select A or B.")

    elif item_choice == "B":
        print("\nYou decide to choose parkour Dwarf slayer.")
        print("Congratulation you chose the save parkour without any danger.")
        print("You can goo freely through the parkour ")
        lvl1_outer_loop = False
        print("Jararis and monkvano:Yeahh baby, We got our lucky pants on.")
        break
    elif item_choice == "C":
        print("\nYou decide to choose the seductive sc"
              "layer parkour.")
        print("You came across two paths with names.")
        print('Each path lead to another way.')
        print("A: Go left for bananas ")
        print("B: Go right for a lady")
        question_glasses = input("Your choice (A or B): ").capitalize()

        if question_glasses == 'A':
            print("\nYou see a bananas on the ground!")
            while True:
                print("A: Eat the banana")
                print("B: Ignore the banana")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    print("\nIt was a trap stupid monkey's.You guys died because of poison!")
                    print("Try again")
                    continue
                elif closet_choice == 'B':
                    print("Nice job, you almost died of poison.")
                    print("Jararis and Monavano: We were to sexy to get seduced. Lets go to the sexy old Bob Monkey")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            print("\nYou guys died. The lady shot two arrows through your hearts.")
            print("Try again")
            while True:
                print("A: Go left for bananas ")
                print("B: Go right for a lady")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    while True:
                        print("A: Go left for bananas ")
                        print("B: Go right for a lady")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            print("\nIt was a trap stupid monkey's.You guys died because of poison!")
                            print("Try again")
                            continue
                        elif closet_choice == 'B':
                            print("Nice job, you almost died of poison")
                            print(
                                "Jararis and Monavano: We were too sexy to get seduced. Let's go to the sexy old Bob "
                                "Monkey")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    print("\nNIce job, you almost died of poison!")
                    print("Jararis and Monavano: We were to sexy to get seduced. Lets go to the sexy old Bob Monkey.")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            print("Invalid choice. Please select A or B.")
    elif item_choice == "D":
        print("\nYou decided for Monkey Slayer parkour.")
        print("While walking in the parkour you read a board congratulation this was the save passage!")
        print("A:Walk past the board")
        print("B:Stand still")
        question_glasses = input("Your choice (A or B): ").capitalize()

        if question_glasses == 'A':
            print("You are know past the board")
            while True:
                print("A: Run straight forward.")
                print("B: Walk slowly the parkour out")
                closet_choice = input("Your choice (A or B): ").capitalize()
                if closet_choice == 'A':
                    print("\nYou activated a motion detector. It was a bait to say this was a free passage.")
                    print("You Monkey's died by a shotgun in the ear")
                    print("Try again")
                    continue
                elif closet_choice == 'B':
                    print("While walking slowly out of the parkour, no motion detector went of.")
                    print("Yararis and Monkvano: Yahhh, lets go to popsy Bob Monkey")
                    lvl1_outer_loop = False
                    break
                break
            break

        elif question_glasses == 'B':
            print("\nThe ground suddenly opened up,  and you Stupid Monkey's felt in large spikes")
            while True:
                print("A:Walk past the board")
                print("B:Stand still")
                table_choice = input("Your choice (A or B): ").capitalize()
                if table_choice == 'A':
                    while True:
                        print("A: Run straight forward.")
                        print("B: Walk slowly the parkour out")
                        closet_choice = input("Your choice (A or B): ").capitalize()
                        if closet_choice == 'A':
                            print("\n You activated a motion detector. It was a bait to say this was a free passage.")
                            print("You Monkey's died by a shotgun in the ear")
                            print("Try again")
                            continue
                        elif closet_choice == 'B':
                            print("While walking slowly out of the parkour, no motion detector went of.")
                            print("Yararis and Monkvano: Yahhh, lets go to popsy Bob Monkey")
                            lvl1_outer_loop = False
                            break
                        break
                    break
                elif table_choice == 'B':
                    print("While walking slowly out of the parkour, no motion detector went of.")
                    print("Yararis and Monkvano: Yahhh, lets go to popsy Bob Monkey")
                    lvl1_outer_loop = False
                    break
                break
            break
        else:
            print("Invalid choice. Please select A or B.\n")

slow_text_print("""After Jararis and Monkvano successfully completed the obstacle course, they arrived at the door of Bob Monkey's house.
They knocked, and they could hear these words: "I'm just a Buffalo Soldier
In the heart of America. Stolen from Africa, brought to America.
Jararis:Hmmm this song sounds familiar.\n 

Jararis then asked, "How can I reach planet Earth?" Bob Monkey explained that he unfortunately couldn't remember the 
coordinates due to his dementia. However, he knew a Jamaican friend: Yara Larissa who might have the information. He offered them a 
submarine and pointed towards the other side of the mountain where a waterfall was located. Bob Monkey advised, 
"Follow the waterfall and the path beyond to reach Aqualandia."
""")

#Level 7: Otoh Gunga 
slow_text_print("""
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
print("After a save landing you have finally arrived back on earth, but it looks a bit weird...")
print("You hear a stranger say: Wagwan bossy. Mi name is Agwe. Yuh luk lose or nuh?")

while True:
    print("A: Yes, where am I?")
    print("B: No, I am good thank you.")
    lvl8_question_one = input("").capitalize()

    if lvl8_question_one == "A":
        print("Djoemma: bommmbaaaclaaaatttt. I will answer fi question if you solve me riddle bossman.")
        print("A: Tell me the riddle")
        print("B: Nevermind I will try to find out my self")
        lvl8_question_two = input("").capitalize()
        
        if lvl8_question_two == "A":
            print("Djoemma: Alright listen here.")
            print("""I'm a legend of music, with rhythm so grand,
                    In Jamaica, my roots firmly stand.
                    I sing of freedom, love, and good vibes,
                    Reggae's the genre where my spirit thrives.
                    Who am I?""")
            
            while True:
                correct_answer = "Bob Marley"
                enter_answer = input("Enter your answer: ")

                if enter_answer == correct_answer:
                    print("You right!")
                    print("Agwe: Ok bossman eff yuh wa fi get home yuh muss follow dis road but watch out it crosses a dangerous neighborhood.")
                    print("You thank Agwe for his help and continue your journey.")
                    print("While you're walking you notice you find yourself in a bad neighbourhood.")
                    print("You hear people yelling and running away.")
                    print("*BAM* *BAM*")
                    print("Jararis: Oh no Monkvano got shot!!!")
                    print("What will you do?")

                    while True:
                        print("A: Try to save Monkvano.")
                        print("B: Run away.")
                        lvl8_question_three =input("").capitalize()

                        if lvl8_question_three == "A":
                            print("Wow are you also trying to get shot???")
                        elif lvl8_question_three == "B":
                            print("You run as fast as you can to not get shot.")
                            break
                    break
                else:
                    print("Wrong answer, try again bloodclat.")
            break

        elif lvl8_question_two == "B":
            print("Djoemma: Nah wrong choice bossy")
            print("*BAM* *BAM*")
            print("Jararis: Oh no Monkvano got shot!!!")
            print("What will you do?")
            while True:
                print("A: Try to save Monkvano.")
                print("B: Run away.")
                lvl8_question_three =input("").capitalize()

                if lvl8_question_three == "A":
                    print("Wow are you also trying to get shot???")
                elif lvl8_question_three == "B":
                    print("You run as fast as you can to not get shot.")
                    break
            break

    elif lvl8_question_one == "B":
        print("Djoemma: Alright bossy.")
        print("While you're walking you notice you find yourself in a bad neighbourhood.")
        print("You hear people yelling and running away.")
        print("*BAM* *BAM*")
        print("Jararis: Oh no Monkvano got shot!!!")
        print("What will you do?")
        while True:
            print("A: Try to save Monkvano.")
            print("B: Run away.")
            lvl8_question_three =input("").capitalize()

            if lvl8_question_three == "A":
                print("Wow are you also trying to get shot???")
            elif lvl8_question_three == "B":
                print("You run as fast as you can to not get shot.")
                break
        break

print("Now you're finally at a safe space.")
print("Jararis: wow my best friend just died and I could not save him. Now I need to finish this mission for him.")
print("Let's go home...Rotterdam...")

#Level 9: Rotterdam
print("You finally arrived in Rotterdam South after a long journey. You are so close to the end")
print("In the distance you see someone walking towards you.")
print("It's 2 euro man!!!")
print("He immediately asked you if you have 2 euros")
while True:
    print("What should I do?")
    print("A: Give him 2 euros.")
    print("B: Say you don't have money.")
    lvl9_question_one = input("").capitalize()

    if lvl9_question_one == "A":
        print("Yes here 2 euro.")
        print("Thank you for the 2 euros. Is there something I can help you with?")
        while True:
            print("A: Yes i need to find a way to get to my base")
            print("B: No I am good.")
            lvl9_question_two = input("").capitalize()

            if lvl9_question_two == "A":
                print("You need to go ask Djoemma.")
                print("While you are walking you suddenly remember something \n Ofcourse I could've asked Djoemma if he knows the way!")
                break
            elif lvl9_question_two == "B":
                print("You continue your journey through Rotterdam South.")
                print("While you are walking you suddenly remember something \n I could ask Djoemma if he knows the way!")
                break
        break
    elif lvl9_question_one == "B":
        print("No sorry I don't have money.")
        print("You continue your journey through Rotterdam South.")
        print("While you are walking you suddenly remember something \n I could ask Djoemma if he knows the way!")
        break

print("You finally found Djoemma, he's chewing on some rat meat.")
print("Hey Djoemma can you help me find the way back to my base?")
print("Djoemma: Hello brother. Ofcourse I can help you but first you need to play rock paper scissors with me until you win.")

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

print("Djoemma: Here a map to your base. Good luck!")

#Level 10: Homebase
print("After a long walk you finally made it to the secret space station base but it looks like you lost the keys.")
print("Luckily you have to option to enter a passcode.")
print("You remember the passcode was four numbers long and was the zonecode for Rotterdam South")

while True:
    correct_passcode = "5314"
    enter_passcode = input("Enter your passcode: ")

    if enter_passcode == correct_passcode:
        print("Access granted!")
        break
    else:
        print("Access denied. Incorrect passcode.")

if Lvl3_Question_One == "A":
    print("""As Jararis returns to the secret space station base and successfully enters the passcode to secure the rock,
          he can't help but feel a sense of relief and accomplishment. The rock, essential for saving humanity, is finally safe and sound. 
          But as he turns to leave the room and go back to his daily monkey business, 
          a loud alarm suddenly blares throughout the base, red warning lights flashing all around him. The base is under attack!

          Jararis is left standing there, clutching the precious rock, as the ground shakes from the impact of the attack. 
          The fate of the base, the rock, and Jararis himself hang in the balance. Will he be able to protect the rock and the base from this unexpected threat? 
          The adventure is far from over, and Jararis faces a new, dangerous challenge.""")
          
elif Lvl3_Question_One == "B":
    print("""As Jararis stands in the secret space station base, relieved that he has secured the rock, he suddenly feels a cold shiver down his spine. 
            His hand, which had been gripping the rock tightly, is now empty. Panic sets in as he frantically searches the room, but the rock is nowhere to be found. It's gone!

            His mind races as he tries to retrace his steps. Could he have dropped it somewhere along the way? Did someone or something steal it? 
            The fate of humanity hangs in the balance, and Jararis is now faced with a gut-wrenching realization - he might have lost the rock on that alien planet.

            Desperation takes over as he contemplates the possibility of having to return to that perilous planet to retrieve the rock. 
            The weight of his failure and the uncertainty of the rock's whereabouts leave him in a state of despair.""")

print("To be continued...")

#The end
print("Thank you for playing Space Monkey! Feel free to play again ;)")
