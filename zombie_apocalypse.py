#Import Random and Time
import random
import time
#Introduction
print(
"Welcome to Zombie Apocalypse. Written in Python3 by Ahnaf on Arch Linux.Code might be broken. I programmed it in less than 2 hours and also I used some weird code formatter!")
name = input("Hello, who are you?: ")
sick_students = random.randint(6, 700)
days = random.randint(2, 14)
print(f"{sick_students} students got sick from eating the cafeteria food!")
print(f"Later on those students became zombies after {days} days")
#Level 1 Hospital
print("Level 1 The Hospital")
score = 0
location = input(
    "Where do want to go? Choose from in lowercase 'Reception' 'Operating Theater' 'Cafe' If there is two words type the second! "
)
if location == 'reception':
    print("Going to the reception area")
elif location == 'theater':
    print("Going to the operating theater")
elif location == 'cafe':
    print("Going to the Cafe!")
else:
    print("Error")
while score < 100:
    zombies_encountered = random.randint(3, 4)
    print(f"You have encountered {zombies_encountered} zombies")
    weapon = input(
        "Pick a weapon to kill them with in lowercase 'Grenade' 'Knife' 'AK-47' 'Kung Fu' 'Bat' "
    )
    if weapon != 'knife':
        print(
            "You died because you have none of those weapons except for the knife and you don't know how to do Kung Fu!"
        )
    elif weapon == 'knife':
        print("Clean that knife!")
        score = score + 25
    zombies_encountered = zombies_encountered - 1
#Level 2 Downtown
print("Level 2 Downtown!")
location = input(
    "Now where do you want to go to escape the zombies 'Town Hall' 'Store ' 'Bank'"
)
print(f"Going to the {location}!")
zombies = random.randint(1, 69)
while score < 200:
    guess = random.randint(1, 2000)
    answer = int(
        input(
            "Guess a number between 1 and 2000 to prove you are not a idiot!"))
    if answer == guess:
        score = score + 1
        print(f"Your a genius and your score is {score}!")
    else:
        print("Sorry you are wrong!")
        score = score - 26
print(f"{zombies}zombies captured you!")
#Level 3 Prision
print(
    f"{name}, you just woke up in a prison cell and relized it all was a dream!"
)
print("Do you want to go to the cafeteria? We will take it as a yes!")
print(
    f"That was a big mistake. You are the feast because you IQ is at least {score-34/13*100}"
)
#End
if score >= 1000:
    print("You got a good score!")
else:
    print("Your score sucks!")
final_score == score**2 / 100
if final_score >= score * 4:
    print(f"Your final score is {final_score} and you got a good one! ")
else:
    print(f"Your final score is {final_score} and you got a bad one! ")
