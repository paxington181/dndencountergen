import random
import json

def main():

    all_monsters = set()
    all_types = set()
    all_terrain = set()
    all_books = set()

    with open('monsters.json') as file:
        monsters = json.load(file)

    for monster_name, monster in monsters.items():
        all_monsters.add(monster_name)
        all_types.add(monster["type"])    
        all_books.add(monster["book"])
        for terrain in monster["terrain"]:
            all_terrain.add(terrain)
        
    print(all_monsters)
    print(all_types)
    print(all_terrain)
    print(all_books)

main()