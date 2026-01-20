print ("DISCLAIMER: MUST COMPLETE ALL FIELDS IN ORDER TO SAVE YOUR DATA PROPERLY")
print ("Use only after your first test and not before or after multiple tests.")
print ("This is to make sure that the average grades are accurate.")

##IMPORTANT VARIABLES TO ADD TO THE JSON
## yearlevel, subjects, grades"

## MATH 0 SCIENCE 1 ENGLISH 2 GEO 3 CHINESE 4

## USE DEFINED VARIABLES TO APPEND TO JSON LATER


import json
import os
from datetime import datetime

def load_data():
    if os.path.exists('grade_data.json'):
        with open('grade_data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
    return data

yearlevel = int(input("Enter your year level (1-12): "))
if yearlevel < 1 or yearlevel > 12:
    print("Invalid year level. Please enter a number between 1 and 12.")
    exit()
subjects = ["Math", "Science", "English", "Geo", "Chinese"]
print("Basic subjects: Math, Science, English, Geo, Chinese")

subjects = ["Math", "Science", "English", "Geo", "Chinese"]
tgrades = []
agrades = []
test = 0
for subject in subjects:
    while True:
        try:
            singlegrade = float(input(f"Enter your {subjects[test]} grade goal (0-100): "))
            if 0 <= singlegrade <= 100:
                tgrades.append(singlegrade)
                print ("____________________________________________________________")
                test += 1
                break
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")
print ("____________________________________________________________")
print (tgrades)
test = 0
for subject in subjects:
    while True:
        print (f"Current {subjects[test]} grade goal: {tgrades[test]}")
        test += 1
        break
test = 0
print ("____________________________________________________________")

for subject in subjects:
    while True:
        try:
            singlegrade = float(input(f"Enter your {subjects[test]} average grade now (0-100): "))
            if 0 <= singlegrade <= 100:
                agrades.append(singlegrade)
                test += 1
                break
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")
test = 0
for subject in subjects:
    while True:
        print (f"Current {subjects[test]} average grade now: {agrades[test]}")
        test += 1
        break
print ("____________________________________________________________")
test = 0
for subject in subjects:
    while True:
        print (f"Your {subjects[test]} grade goal is {tgrades[test]} and your current average is {agrades[test]}")
        avgrade = (tgrades[test] - agrades [test])
        if avgrade > 0:
            print (f"You need to improve your {subjects[test]} grade by {avgrade} points to reach your goal.")
            print ("__________")
            test += 1
            break
        elif avgrade < 0:
            print (f"You have already surpassed your {subjects[test]} grade goal by {-avgrade} points. Great job!")
            print ("__________")
            test += 1
            break
        else:
            print (f"You have already met your {subjects[test]} grade goal. Keep it up!")
            print ("__________")
            test += 1
            break
print ("____________________________________________________________")
test = 0
for subject in subjects:
    while True:
        print (f"Summary for {subjects[test]}:")
        print (f"Grade Goal: {tgrades[test]}")
        print (f"Current Average: {agrades [test]}")
        avgrade = (tgrades[test] - agrades [test])
        if avgrade > 0:
            print (f"Points needed to reach goal: {avgrade}")
            test += 1
            print ("__________")
            break
        elif avgrade < 0:
            print (f"You have surpassed your goal by {-avgrade} points.")
            print ("__________")
            test += 1
            break
        else:
            print (f"You have met your goal exactly.")
            print ("__________")
            test += 1
            break
print ("____________________________________________________________")
print ("All data has been recorded. Thank you!")

