# import random as rnd
# import pandas as pd

# Time for a refresh: we'll have every genre in a seperate file. The user will state their mood and the program will
# then choose which file to pick the anime from based on the stated mood.

# Menu setup and input: should make this a loop later
print("Welcome.Here are the options:", '\n')
print("1. Action")
print("2. Romance")
print("3. Slice of life")
print("4. Psychological")
val = input("So,what kind of mood are you in? ")
val = val.lower()

# Opening files based on the selected mood
if val == "action":
    open("rndslctr-anime-action.txt")
elif val == "romance":
    open("rndslctr-anime-romance.txt")
elif val == "slice of life":
    open("rndslctr-anime-sol.txt")
elif val == "psychological":
    open("rndslctr-anime-psycho.txt")
else:
    print("That's not one of the moods, quitting program.")
    quit()
