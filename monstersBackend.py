import requests
import json

print("This script pulls down the monsters from the DnD API.")
print("If you've already generated the monsters data, or if you've got a clean pull of the repo, you shouldn't be running this.")
proceed = input("Do you want to proceed? (y/n):")

if proceed.lower() == 'y':
    print("Proceeding...")
    response = requests.get('https://www.dnd5eapi.co/api/monsters')
    monsters_urls = response.json()['results']

    DND_MONSTERS = {}

    # Fetch details for each monster
    for monster in monsters_urls:
        response = requests.get('https://www.dnd5eapi.co' + monster['url'])
        monster_data = response.json()
        
        DND_MONSTERS[monster_data['name']] = {
            'size': monster_data['size'],
            'type': monster_data['type'],
            'alignment': monster_data['alignment'],
            'armor_class': monster_data['armor_class'],
            'hit_points': monster_data['hit_points'],
            'hit_dice': monster_data['hit_dice'],
            'speed': monster_data['speed'],
            'strength': monster_data['strength'],
            'dexterity': monster_data['dexterity'],
            'constitution': monster_data['constitution'],
            'intelligence': monster_data['intelligence'],
            'wisdom': monster_data['wisdom'],
            'charisma': monster_data['charisma'],
            'proficiencies': monster_data['proficiencies'],
            'damage_vulnerabilities': monster_data['damage_vulnerabilities'],
            'damage_resistances': monster_data['damage_resistances'],
            'damage_immunities': monster_data['damage_immunities'],
            'condition_immunities': monster_data['condition_immunities'],
            'senses': monster_data['senses'],
            'languages': monster_data['languages'],
            'challenge_rating': monster_data['challenge_rating'],
            'xp': monster_data['xp'],
            'special_abilities': monster_data['special_abilities'],
            'actions': monster_data['actions'],
            'legendary_actions': monster_data.get('legendary_actions', []),
        }
        print("Added monster: {}".format(monster_data['name']))

    with open('monsters.json', 'w') as f:
        json.dump(DND_MONSTERS, f)
else:
    print("Aborted.")
