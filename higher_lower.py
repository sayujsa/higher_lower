from art1 import logo, vs
from game_data import data
from replit import clear
import random

score = 0
personA = random.choice(data)
personB = random.choice(data)
while personA == personB:
    personB = random.choice(data)

if personA['follower_count'] > personB['follower_count']:
    a_or_b = "A"
else:
    a_or_b = "B"

while True:
    print(logo + "\n")
    if score != 0:
        print(f"Your score is {score}, keep going!")
        if a_or_b == 'B':
            personA = personB.copy()
            personB = random.choice(data)
            while personA == personB:
                personB = random.choice(data)
        else:
            personB = random.choice(data)
            while personA == personB:
                personB = random.choice(data)
    if personA['follower_count'] > personB['follower_count']:
        a_or_b = "A"
    else:
        a_or_b = "B"

    print(f"Compare A : {personA['name']}, a {personA['description']} from {personA['country']}")
    print(vs)
    print(f"With B : {personB['name']}, a {personB['description']} from {personB['country']}")

    guess = input("Who has more followers? A or B : ").upper()

    if guess != a_or_b:
        break
    else:
        score += 1
    clear()

print(f"\nYour score is {score}")

