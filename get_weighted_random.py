import json
import random

with open('./content/js/seeded.js') as in_file:
    raw = in_file.read().replace('var jsonArray = ', '')
    games = json.loads(raw)

choices = []

for game in games:
    if game['votes'] >= 0:
        for x in range(0, game['votes'] + 1):
            choices.append(game)

random.shuffle(choices)
random.shuffle(choices)
random.shuffle(choices)
print(random.choice(choices))
