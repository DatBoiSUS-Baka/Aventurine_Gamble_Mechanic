# 22 April 2024
# An attempt to recreate Boss Aventurine gamble mechanics

import random


# Python is EZ

# Party data
party = [
    {'name': 'Tingyun', 'spd': 150, 'cEnergy': 0, 'mEnergy': 130},
    {'name': 'Ruan Mei', 'spd': 134, 'cEnergy': 0, 'mEnergy': 130},
    {'name': 'Aventurine', 'spd': 134, 'cEnergy': 0, 'mEnergy': 110},
    {'name': 'Yanqing', 'spd': 143, 'cEnergy': 0, 'mEnergy': 140}
]
# Determining the turn order of the party
def turnOrder(party):
    return party['spd']
party.sort(reverse=True, key=turnOrder) #Sort spd by decsending

def avenGamble(party):
    dice = 0
    charPoint = 0
    target = random.choice(party)
    print(f"{target["name"]} is selected!")
    gamblePoint = random.randrange(1, 9)
    while (cycle < 1):
        charAction = input('What will you Choose? 1 / 2: ') #Input of what the player will choose (1 = basic attack, 2 = skill)
        print(gamblePoint)
        if (charAction == 1):
            dice = random.randrange(1, 9)
            charPoint = charPoint + dice
        elif (charAction == 2):
            print("No charPoint gained this round..")
        if charPoint >= gamblePoint:
            print(f"{target["name"]} has higher points, ultimate is activated!")
            target["cEnergy"] = target["mEnergy"]
        else:
            print(f"{target["name"]} has lower points, energy is drained!")
            print(charPoint)
            target["cEnergy"] = 0
        cycle += 1
# Cycle count
cycle = 0

print("Let the game begin!")
choice = input('Y/N: ')
if choice == 'Y':
    while (cycle < 10):
        avenGamble(party)
        
elif choice == 'N':
    pass
else:
    print("Aventurine gambles all by himself..\n")
    