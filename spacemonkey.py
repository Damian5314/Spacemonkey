print("Welcome to Space Monkey")
print("")
print("Jararis was a special trained monkey that can talk and who was trained to go to space. One day he was needed for a space mission to save humanity but his ship crashed down.")

max_fuel = 100
max_health = 100

fuel = max_fuel
health = max_health

#Level 1: 
while True:
    print("What should I do?")
    print("A: Get out the ship.")
    print("B: Sit down.")
    question_one = input("").capitalize()

    if question_one == "A":
        print("You got out of the ship.")
        break
    elif question_one == "B":
        print("I wont get anywhere if i sit down.")

print("You look around and see that you're on a different planet.")
print("Your rocket is also broken and you must find a way to fix it.")

while True:
    print("Which way should I go?")
    print("A: Let's check out the forest.")
    print("B: Let's walk around the beach.")
    question_two = input("").capitalize()

    if question_two == "A":
        print("You went to check in the forest.") 
        break
    elif question_two == "B":
        print("I don't like sand. It's coarse and rough and irritating and it gets everywhere.")

#Level 2: Alien ship

#Level 3: Alien planet
print("You have succesfully escaped the alien spaceship but you are now on their planet.")
print("You quickly go hiding because the whole planet is filled with the hostile aliens.")
print("Your ship is still on the big alien ship but there is also an other alien ship in sight.")

while True:
    print("What will you do?")
    print("A: Try to get back your own ship.")
    print("B: Try to steal the alien ship.")
    question_ = input("").capitalize()

    if question_ == "A":
        print()
        break
    elif question_ == "B":
        print()
        break
#Level 4:

#Level 5: Banana Haven
print("Wow this planet looks beautifull. Look at those trees and waterfalls!")
print("But wait...")
print("Are these my...my family???")


#Level 6:

#Level 7:

#Level 8: Jamaica
print("After a save landing you have finally arrived back on earth, but it looks a bit weird...")
print("You hear a stranger say: Wagwan bossy Yuh luk lose or nuh?")

while True:
    print("A: Yes, where am I?")
    print("B: No, I am good thank you.")
    question_ = input("").capitalize()

    if question_ == "A":
        print("bommmbaaaclaaaatttt. I will answer that question if you solve this riddle bossman.")
        print("A: Tell me the riddle")
        print("B: Nevermind I will try to find out my self")
        question_ = input("").capitalize()
        
        if question_ == "A":
            print("")
            break
        elif question_ == "B":
            print("Alright bossy")
            break
    elif question_ == "B":
        print("Alright bossy.")
        break

#Level 9: Rotterdam
print("You are coming closer to the base but first you need to go trough Rotterdam South")

#Level 10: 
print("You finally made it to the secret space station base but it looks like you lost the keys.")
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

#The end
print("The end. Thank you for playing Space Monkey!")
