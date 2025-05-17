import random
import sys

# List of Grades.
grade_list = ["High Grade", "Real Grade", "Master Grade", "Perfect Grade"]

# Lists of kits.
hg_list = ["Command [Q]ant Desert", "G Self Perfect Pack", "Schwarzette"]
rg_list = ["Unicorn Perfectibility", "Zeong", "Wing TV Ver.", "Astray Red Frame", "GP-01", "GP-01 FB", "Sazabi", "Sword Impulse Spec II"]
mg_list = ["Sinanju Stein Nar. Ver. Ka.", "Kyrios", "Dynames", "Mobile Ginn", "Strike Freedom", "RX-78-4", "Unicorn OVA", "Vidar", "V2 Ver. Ka."]
pg_list = ["RX-78-2"]

print("Would you like to roll the dice for a grade?")

while True:
    answer = input("Yes or No?\n").lower() # User inputs yes or no to roll for a kit grade.
    if answer == "yes":
        print("OK! Rolling the dice.\n") # Rolls the dice and selects a random grade from grade_list.
        random_grade = random.choice(grade_list)
        print(f"Random Grade: {random_grade}\n")

        answer = input("Would you like to roll again for a kit?\n").lower() # Asks the user if they would like to roll for a specific kit from the grade.
        if answer == "yes":
            print("OK! Rolling for a kit.\n")

            if random_grade == "High Grade": # If High Grade is chosen, selects from that list.
                kit = random.choice(hg_list)
            elif random_grade == "Real Grade": # If Real Grade is chosen, selects from that list.
                kit = random.choice(rg_list)
            elif random_grade == "Master Grade": # If Master Grade is chosen, selects from that list.
                kit = random.choice(mg_list)
            elif random_grade == "Perfect Grade": # If Perfect Grade is chosen, selects from that list.
                kit = random.choice(pg_list)
            else:
                kit = "No kits for this grade"
            print(f"Here you go: {kit}")
            break # Ends the loop

        elif answer == "no": # If the user does not want a specific kit, the game will end.
            print("OK! Quitting the game.\n")
            break # Ends the loop.
        else:
            print("Please enter Yes or No.\n") # Asks for "yes" or "no" if the user does not input one of the options.

    elif answer == "no": # Ends the game if the user does not want a specific grade.
        print("OK! Quitting the game.\n")
        sys.exit()
    else: # Asks for "yes" or "no" if the user does not input one of the options.
        print("Please enter Yes or No.\n")



