import math

def calculate_tip(people, bill, percent):
    tip = bill * percent
    total = bill + tip
    return round(total/people, 2)

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
print("Each person should pay: $" + str(calculate_tip(people, bill, percent)))
