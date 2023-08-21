import json
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

DND_MONSTERS = {}
with open('monsters.json', 'r') as f:
    DND_MONSTERS = json.load(f)

@app.route('/')
def home():
    return render_template('monsterSearch.html')

@app.route('/api/monster', methods=['GET'])
def get_monster_info():
    monster_name = request.args.get('monster_name', None)
    size = request.args.get('size', None)
    type = request.args.get('type', None)
    alignment = request.args.get('alignment', None)
    armor_class = request.args.get('armor_class', None)
    hit_points = request.args.get('hit_points', None)

    results = {}
    for name, data in DND_MONSTERS.items():
        if (monster_name.lower() in name.lower() or not monster_name) and \
            (data.get('size') == size or not size) and \
            (data.get('type') == type or not type) and \
            (data.get('alignment') == alignment or not alignment):
            results[name] = data

    return jsonify(results), 200

@app.route('/api/all-monsters', methods=['GET'])
def get_all_monsters():
    return jsonify(DND_MONSTERS), 200

@app.route('/api/specific-monster', methods=['GET'])
def get_specific_monster_info():
    # Show all monsters with the correct size and type
    monster_size = request.args.get('size', None)
    monster_type = request.args.get('type', None)
    results = {}
    for name, data in DND_MONSTERS.items():
        if data.get('size') == monster_size and \
            data.get('type') == monster_type:
            results[name] = data

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)
