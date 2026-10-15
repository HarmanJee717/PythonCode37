name = input("What is your name: ")

mood = input(
    "How are you feeling today? "
    "happy/sad/tired/stressed/excited: "
).lower()

energy = int(input("Enter your energy level from 1 to 10: "))

if energy < 3:
    print("Alert: Your energy seems low today. "
          "Take some rest and drink water if needed.")

if energy >= 5:
    print("Come on! You have energy to do something productive today!")
else:
    print("Take it slow and easy today and do something relaxing.")

if mood == "happy":
    advice = "Keep spreading your positive energy!"
elif mood == "sad":
    advice = "Talk to someone you trust about how you feel."
elif mood == "tired":
    advice = "Drink water and do something relaxing."
elif mood == "stressed":
    advice = "Try deep breathing to help you relax."
elif mood == "excited":
    advice = "Nice! Use your excitement for something creative!"
else:
    advice = "Take care of yourself today!"

print(name + ", " + advice)

import datetime

today = datetime.datetime.now()
print("Today's date and time:", today)