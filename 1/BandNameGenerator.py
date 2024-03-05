repeat = True
while(repeat):
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    print(f"Your band name could be {city} {pet_name}")

    response = input("Repeat? Y/N: ")
    if(response == "N" or response == "n"):
        repeat = False


