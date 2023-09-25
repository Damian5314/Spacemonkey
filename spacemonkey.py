print("Welcome to Space Monkey")
print("")
print("Jararis was a special trained monkey who was trained to go to space. One day he was needed for a space mission to save humanity but his ship crashed down.")

max_fuel= 100
max_health= 100

fuel= max_fuel
health= max_health


while True:
    question_one=input("What should I do? ").capitalize()
    print("A: Get out the ship.")
    print("B: Sit down.")

    if question_one=="A":
        print("You got out of the ship.")
        break

    elif question_one=="B":
        print("I wont get anywhere if i sit down.")

print("You look around and see that you're on a different planet.")
print("Your rocket is also broken and you must find a way to fix it.")

while True:
    question_two=input("Which way should I go? ").capitalize()
    print("A: Let's check out the forest.")
    print("B: Let's walk around the beach.")

    if question_two=="A":
        print("You went to check in the forest.") 
        break
    elif question_two=="B":
        print("I don't like sand. It's coarse and rough and irritating and it gets everywhere.")

