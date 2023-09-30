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

max_fuel = 100
max_health = 100

fuel = max_fuel
health = max_health

#Level 1: Unknown planet
print(
    """Jararis was a special trained monkey that can talk and who was trained to go to space.
    One day he was needed for a space mission to get a special rock to save humanity but when he finally got the item,
    A astroid hit his ship and he crashed down.\n""")
print("""Jararis: Huh, where am I? 
My head is pounding, and my vision is blurry. I recall flashes of alarm signals and sudden turbulence. 
The last memory I have is looking out the window of my spaceship as I crashed. 
Now I lie here, surrounded by lush green leaves and the sweet scent of tropical flowers.
This is not a place I am familiar with. It's as if I've landed on an entirely different world.
I hear the sounds of unfamiliar creatures and see strange, colorful birds high in the trees. 
Adrenaline rushes through me as I realize I am stranded on this mysterious tropical planet. 
Survival is now my priority.
I must find ways to protect myself and explore what this new world has to offer.
I need to go as soon as possible from this planet to save humanity!!.
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
        print("Grrr I'm hungry, sitting down wont get me anywhere.")

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
        print("Yararis:I don't like sand. It's coarse , irritating and it gets everywhere.")
        
print("When entering the forest , there was a bord that Jararis did not see : Forest of riddles!")
print("""Jararis:The forest is like a giant playground filled with towering trees, so tall they seem to touch the sky.
It smells like wet earth after rain, a refreshing scent. 
There are flowers everywhere, some as big as my head! 
There are flowers of all colors—red, yellow, blue—all over the place. It's like a rainbow on the ground.
\n""")

print("""Jararis: As I ventured through the lush forest, my eyes were drawn to a towering banana tree.
Its slender trunk reached up into the sky, and at the top, a cluster of banana hung. 
These bananas were enormous, larger than any I had ever come across in my life.                       
I felt a mix of excitement and hunger.
I wanted to taste the delicious banana and savor the sweet taste of it. 
However, the bananas seemed unreachable, swaying high above the ground.\n""")

print("""Beside the tree, I noticed a weathered wooden sign. 
It was weathered and had some faded writing.
I strained my eyes to read: "If you wish to feast on bananas delights, solve the puzzle and prove your might."
 """)

print("Answer at least two questions correctly to make the bananas fall!")

play_count = 0

while play_count < 4:
    question_1 = ("Isabella needs 22 cartons of space-milk from the space-market."
                  " She can only carry 4 cartons at a time.\nHow many trips does she need to make to the space-market?")
    answer_1 = "6"

    question_2 = ("Fernando is twelve years old, and he is three times as old as his brother. "
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

        if correct_answers >= 2:
            print("\nCongratulations! You answered at least two questions correctly.")
            print("Bananas fall from the tree!")
            print("""The correct answers were: q1: 6, q2: 8, and q3: egg, grenade, glow stick, seal, save, crust, seed, rule,
                          word, dream, solution, trust, horse, code, habit, bar.""")
            bananas_fallen = True
            break
        else:
            print("\nUnfortunately, you didn't answer at least two questions correctly. Try again.")
            play_count += 1

    if bananas_fallen:
        print("You now have enough food to last for a while on this planet.")
        print("Jararis: Yeah, I did it! Bananas are coming to me, baby!!")
        break

    if play_count >= 4:
        print("Unfortunately, you tried too many times. The answers were:")
        print('q1: 6, q2: 8, q3: egg')
        print('Lararis: Ahh i am so hungry')
       
   
print("")

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
                print("You succesfully choke him to death,\nAllowing you to grab his keys and silently sneak of the Ship")
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
                print("Well arent you a lucky monkey :D")
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
            print("Monkvano: Of course my fellow monkey brother, we have to help eachother out ain't that right")
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

print("")

#Level 6: Dwarfmania

#Level 7: Otoh Gunga 
print("As you are going deeper and deeper into the ocean you start to see some lights down there.")

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
print("You finally arived in Rotterdam South after a long journey. You are so close to the end")
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
