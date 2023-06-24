import datetime
import json
import os
from decimal import Decimal
from cards import *

with open('database.json') as db_file:
	db = json.load(db_file)
	users = db['id_to_username'].copy()

# Handle new cards
files = os.listdir('../../Desktop/twitch/redeems/cardgacha/')
for file in files:
    with open('../../Desktop/twitch/redeems/cardgacha/' + file, 'r') as in_file:
        jdata = json.load(in_file)
    if jdata['User'] not in db['cards'].keys():
        db['cards'][jdata['User']] = {'collection':{}}
    card_id = jdata['Card']['ID']
    if card_id in db['cards'][jdata['User']]['collection'].keys():
        db['cards'][jdata['User']]['collection'][card_id] += 1
    else:
        db['cards'][jdata['User']]['collection'][card_id] = 1
    os.remove('../../Desktop/twitch/redeems/cardgacha/' + file)

# Calculate card stats...
card_stats = {}
for set_name in cards.keys():
    card_stats[set_name] = {}
    card_count = 0
    true_card_count = 0
    for card in cards[set_name]:
        card_stats[set_name][card['ID']] = {}
        card_stats[set_name][card['ID']]['Collected By'] = 0
        for user_id in users.keys():
            # Handle users with no cards
            if user_id not in db['cards'].keys():
                continue
            if card['ID'] in db['cards'][user_id]['collection'].keys():
                card_stats[set_name][card['ID']]['Collected By'] += 1
        true_card_count += 1
        if card['Rarity'] != 'Secret Rare':
            card_count += 1
    card_stats[set_name]['Count'] = card_count
    card_stats[set_name]['True Count'] = true_card_count

event_stats = {}
for card in event_cards:
    event_stats[card['ID']] = {}
    event_stats[card['ID']]['Collected By'] = 0
    for user_id in users.keys():
        # Handle users with no cards
        if user_id not in db['cards'].keys():
            continue
        if card['ID'] in db['cards'][user_id]['collection'].keys():
            event_stats[card['ID']]['Collected By'] += 1

print("Regenerating card pages...")
for set_name in cards.keys():
    for card in cards[set_name]:
        with open('./content/pages/cards/%s.md' % card['ID'], 'w') as out_file:
            page = "Title: %s\nSummary: View the details for the %s card from the %s!\nCategory: Cards\nSlug: card/%s\nStatus: Hidden\n\n" % (card['Name'], card['Name'], set_name, card['ID'])
            page += "<center><a href='/images/cards/" + card['ID'] + ".png'><img src='/images/cards/" + card['ID'] + ".png' width='50%'></a>\n\n"
            got_percent = round((Decimal(card_stats[set_name][card['ID']]['Collected By']) / Decimal(len(users.keys()))) * 100, 2)
            page += "Rarity: %s\n\nCollected by %s/%s users (%s)\n\nDrawn by <a href='%s'>%s</a></center>\n" % (card['Rarity'], card_stats[set_name][card['ID']]['Collected By'], 
                                                                                                          len(users.keys()), str(got_percent) + '%', card['Artist Link'], card['Artist'])
            out_file.write(page)

for card in event_cards:
    with open('./content/pages/cards/%s.md' % card['ID'], 'w') as out_file:
        page = "Title: %s\nSummary: View the details for the %s card from the %s!\nCategory: Cards\nSlug: card/%s\nStatus: Hidden\n\n" % (card['Name'], card['Name'], set_name, card['ID'])
        page += "<center><a href='/images/cards/" + card['ID'] + ".png'><img src='/images/cards/" + card['ID'] + ".png' width='50%'></a>\n\n"
        got_percent = round((Decimal(event_stats[card['ID']]['Collected By']) / Decimal(len(users.keys()))) * 100, 2)
        page += "%s\n\nCollected by %s/%s users (%s)\n\nDrawn by <a href='%s'>%s</a></center>\n" % (card['Description'], event_stats[card['ID']]['Collected By'], 
                                                                                                      len(users.keys()), str(got_percent) + '%', card['Artist Link'], card['Artist'])
        out_file.write(page)

print("Regenerating user collections...")
for user_id in users.keys():
    user_name = users[user_id]
    # Handle users with no cards
    if user_id not in db['cards'].keys():
        continue
    # Calculate user stats...
    user_stats = {}
    user_stats['Event Count'] = 0
    for set_name in cards.keys():
        user_stats[set_name] = {}
        user_stats[set_name]['Count'] = 0
        for card in cards[set_name]:
            if card['ID'] in db['cards'][user_id]['collection'].keys():
                user_stats[set_name]['Count'] += 1
    for card in event_cards:
        if card['ID'] in db['cards'][user_id]['collection'].keys():
            user_stats['Event Count'] += 1
        
    with open('./content/pages/binders/%s.md' % user_id, 'w') as out_file:
        # Add page header
        page = "Title: %s's Card Collection\nSummary: See all of the cards that %s has collected!\nCategory: Cards\nSlug: binder/%s\nStatus: Hidden\n\n" % (user_name, user_name, user_name.lower())
        for set_name in cards.keys():
            page += '<center>%s (%s/%s)</center>\n' % (set_name, user_stats[set_name]['Count'], card_stats[set_name]['Count'])
            page += '---\n'
            for card in cards[set_name][:-1]:
                if card['ID'] in db['cards'][user_id]['collection'].keys():
                    page += "<a href='/card/" + card['ID'] + "/'><img src='/images/cards/" + card['ID'] + "-small.png' width='20%'></a>"
                else:
                    page += "<img src='/images/cards/back-small.png' width='20%'>"
            # Check for secret rare
            if cards[set_name][-1]['ID'] in db['cards'][user_id]['collection'].keys():
                    page += "<a href='/card/" + cards[set_name][-1]['ID'] + "/'><img src='/images/cards/" + cards[set_name][-1]['ID'] + "-small.png' width='20%'></a>"
        # Add event cards
        event_card_count = 0
        for card in event_cards:
            if card['ID'] in db['cards'][user_id]['collection'].keys():
                event_card_count += 1
        page += '\n---\n<center><h2>Event Cards (%s)</h2></center>\n---\n<center>' % user_stats['Event Count']
        for card in event_cards:
            if card['ID'] in db['cards'][user_id]['collection'].keys():
                page += "<a href='/card/" + card['ID'] + "/'><img src='/images/cards/" + card['ID'] + "-small.png' width='20%'></a>"
        page += '</center>'
        out_file.write(page)

text_db = json.dumps(db, indent=4)
with open('database.json', 'w') as out_file:
	out_file.write(text_db)
