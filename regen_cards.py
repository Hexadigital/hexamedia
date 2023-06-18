import datetime
import json

with open('database.json') as lb_file:
	lb = json.load(lb_file)
	users = lb['id_to_username'].copy()

print("Regenerating cards...")
for user_id in users.keys():
    user_name = users[user_id]
    with open('./content/pages/cards/%s.md' % user_id, 'w') as out_file:
        # Add page header
        page = "Title: %s's Card Collection\nSummary: See all of the cards that %s has collected!\nCategory: Cards\nSlug: cards/%s\nStatus: Hidden\n\ntest\n\n---\ntest" % (user_name, user_name, user_name.lower())
        out_file.write(page)
