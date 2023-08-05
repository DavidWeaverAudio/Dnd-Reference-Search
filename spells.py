import json
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

DND_SKILLS_SPELLS = {}
with open('spells.json', 'r') as f:
        DND_SKILLS_SPELLS = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/spell', methods=['GET'])
def get_spell_info():
    spell_name = request.args.get('spell_name', None)
    level = request.args.get('level', None)
    school = request.args.get('school', None)

    results = {}
    for name, data in DND_SKILLS_SPELLS.items():
        if (spell_name.lower() in name.lower() or not spell_name) and \
            (str(data.get('level')) == level or not level) and \
            (data.get('school') == school or not school):
            results[name] = data

    return jsonify(results), 200

@app.route('/api/all-spells', methods=['GET'])
def get_all_spells():
    return jsonify(DND_SKILLS_SPELLS), 200

@app.route('/api/specific-spell', methods=['GET'])
def get_specific_spell_info():
    #show all spells with the correct level and school
    spell_level = request.args.get('level', None)
    spell_school = request.args.get('school', None)
    results = {}
    for name, data in DND_SKILLS_SPELLS.items():
        if str(data.get('level')) == spell_level and \
            data.get('school') == spell_school:
            results[name] = data

    return jsonify(results), 200
if __name__ == '__main__':
    app.run(debug=True)