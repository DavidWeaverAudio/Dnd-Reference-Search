import requests
import json

print("This script pulls down the spells from the DnD API.")
print("If you've already generated the spells data, you shouldn't be running this.")
proceed = input("Do you want to proceed? (y/n): ")

if proceed.lower() == 'y':
    print("Proceeding...")
    # Fetch spell list
    response = requests.get('https://www.dnd5eapi.co/api/spells')
    spell_urls = response.json()['results']

    DND_SKILLS_SPELLS = {}

    # Fetch details for each spell
    for spell in spell_urls:
        response = requests.get('https://www.dnd5eapi.co' + spell['url'])
        spell_data = response.json()
        try:
            spell_data['material']
        except KeyError:
            spell_data['material'] = None
        DND_SKILLS_SPELLS[spell_data['name']] = {
            'description': ' '.join(spell_data['desc']),
            'casting_requirements': ', '.join(spell_data['components']),
            'casting_time': spell_data['casting_time'],
            'duration': spell_data['duration'],
            'level': spell_data['level'],
            'range': spell_data['range'],
            'school': spell_data['school']['name'],
            'classes': spell_data['classes'],
            'higher_level': spell_data['higher_level'],
            'material': spell_data['material'], 
            'ritual': spell_data['ritual'],
            'concentration': spell_data['concentration'],
        }
        print("Added spell: {}".format(spell_data['name']))

        with open('spells.json', 'w') as f:
            json.dump(DND_SKILLS_SPELLS, f)
    else:
        print("Aborted.")