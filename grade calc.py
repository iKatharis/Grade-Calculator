print("------------------Calculator for your grades------------------")

yearlevel = int(input("Enter your year level (1-12): "))
if yearlevel < 1 or yearlevel > 12:
    print("Invalid year level. Please enter a number between 1 and 12.")
    exit()
subjects = ["Math", "Science", "English, Geo, Chinese"]
print("Basic subjects: Math, Science, English, Geo, Chinese")
try:
    with open(f"{yearlevel} grade.txt",) as file:
        content = file.read()
    print(f"Previous grade goals for year level {yearlevel}:\n{content}")
except FileNotFoundError:
    print(f"No previous grade goals found for year level {yearlevel}.")
else:
    print("Proceeding to enter new grade goals.")



mathgrade = float(input("Enter your Math grade goal: "))
sciencegrade = float(input("Enter your Science grade goal: "))
englishgrade = float(input("Enter your English grade goal: "))
geograde = float(input("Enter your Geo grade goal: "))
chinesegrade = float(input("Enter your Chinese grade goal: "))
if mathgrade < 0 or mathgrade > 100 or sciencegrade < 0 or sciencegrade > 100 or englishgrade < 0 or englishgrade > 100 or geograde < 0 or geograde > 100 or chinesegrade < 0 or chinesegrade > 100:
    print("Invalid grade input. Please enter grades between 0 and 100.")
    exit()

averagegrade = (mathgrade + sciencegrade + englishgrade + geograde + chinesegrade) / 5
print(f"Your average grade goal for year level {yearlevel} is: {averagegrade}%")

with open(f"{yearlevel} grade.txt", "a") as file:  # "a" = append mode
    file.write(f"Year Level: {yearlevel}\n")
    file.write(f"Math grade goal: {mathgrade}\n")
    file.write(f"Science grade goal: {sciencegrade}\n")
    file.write(f"English grade goal: {englishgrade}\n")
    file.write(f"Geo grade goal: {geograde}\n")
    file.write(f"Chinese grade goal: {chinesegrade}\n")
    file.write(f"Average grade goal: {averagegrade}%\n")