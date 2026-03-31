import random
import json

def main():

    with open('monsters.json') as file:
        monsters = json.load(file)
        print(monsters)


main()