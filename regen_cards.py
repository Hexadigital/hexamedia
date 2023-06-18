import datetime
import json
from decimal import Decimal

cards = {
    'Clover Power Set': [
        {
            'ID':'21237ee9b3ca1',
            'Name': 'Sticker Hex',
            'Number': '1',
            'Rarity':'Common',
            'Artist': 'torisanOwO',
            'Artist Link': 'https://twitter.com/torisanOwO',
            'Source': 'https://skeb.jp/@torisanOwO/works/18'
        },
        {
            'ID':'7cc1d724b2621',
            'Name': '',
            'Number': '2',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'547c93afbd692',
            'Name': '',
            'Number': '3',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'fc19809dc9183',
            'Name': '',
            'Number': '4',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'5728258ed23d4',
            'Name': '',
            'Number': '5',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'282f0b71360a5',
            'Name': '',
            'Number': '6',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'c4ce84b15fed7',
            'Name': '',
            'Number': '7',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'b92b48f7f5e28',
            'Name': '',
            'Number': '8',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'96487ec96fb09',
            'Name': '',
            'Number': '9',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'9489c9ff45ad10',
            'Name': '',
            'Number': '10',
            'Image':'',
            'Rarity':'Common',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'7698bc91a42511',
            'Name': '',
            'Number': '11',
            'Image':'',
            'Rarity':'Uncommon',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'d7064d6712ea12',
            'Name': '',
            'Number': '12',
            'Image':'',
            'Rarity':'Uncommon',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'d72e35b107d113',
            'Name': '',
            'Number': '13',
            'Image':'',
            'Rarity':'Uncommon',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'e5208a7c3e7e14',
            'Name': '',
            'Number': '14',
            'Image':'',
            'Rarity':'Uncommon',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'8afda7024ce515',
            'Name': '',
            'Number': '15',
            'Image':'',
            'Rarity':'Uncommon',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'47e418648ab716',
            'Name': '',
            'Number': '16',
            'Image':'',
            'Rarity':'Rare',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'6bbd232a253317',
            'Name': '',
            'Number': '17',
            'Image':'',
            'Rarity':'Rare',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'19d6ffca4e1818',
            'Name': '',
            'Number': '18',
            'Image':'',
            'Rarity':'Rare',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'b85133aeee1f19',
            'Name': '',
            'Number': '19',
            'Image':'',
            'Rarity':'Ultra Rare',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'24baab34ee5420',
            'Name': '',
            'Number': '20',
            'Image':'',
            'Rarity':'Ultra Rare',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
        {
            'ID':'6ffc23234e8b21',
            'Name': '',
            'Number': '21',
            'Image':'',
            'Rarity':'Secret Rare',
            'Artist': '',
            'Artist Link': '',
            'Source': ''
        },
    ],
}

event_cards = [
    {
        'ID':'b8ad08aca188',
        'Name': 'One Year',
        'Number': '1',
        'Rarity':'Common',
        'Artist': 'soratukiame',
        'Artist Link': 'https://twitter.com/soratukiame',
        'Source': 'https://skeb.jp/@soratukiame/works/1',
        'Description': 'Rewarded on check-in from 2023-06-23 to 2023-06-29.'
    }
]

with open('database.json') as db_file:
	db = json.load(db_file)
	users = db['id_to_username'].copy()

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
                    page += "<img src='/images/cards/" + cards[set_name][-1]['ID'] + "-small.png' width='20%'>"
        # Add event cards
        event_card_count = 0
        for card in event_cards:
            if card['ID'] in db['cards'][user_id]['collection'].keys():
                event_card_count += 1
        page += '\n---\n<center><h2>Event Cards (%s)</h2></center>' % user_stats['Event Count']
        out_file.write(page)
        
