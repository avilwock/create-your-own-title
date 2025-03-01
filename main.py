# The Goal of this project is to create an adventure title generator
print("Welcome to the Adventure Title Generator!\n")

color = input("Choose your favorite color ").capitalize()
mythical_creature = input("Select a mythical creature ").capitalize()
adjective = input("Select an adjective to describe a magical place ").capitalize()
place = input("Select a place where magic would happen ").capitalize()

print(f"The title of your book will be 'The {color} {mythical_creature} of the {adjective} {place}'!")