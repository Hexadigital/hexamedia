import datetime
import json

with open('leaderboard.json') as lb_file:
	lb = json.load(lb_file)
	users = lb['ranks']
	points = lb['points']

print("Regenerating leaderboard...")
with open('./content/pages/leaderboard.md', 'w') as out_file:
	# Add page header
	page = "Title: Twitch Leaderboard\nSummary: See who has attended the most Twitch streams.\nStatus: Hidden\n\nAre you missing from this list? Purchase the Stream Check-In reward during [my streams](https://twitch.tv/hexadigital) and you'll be added next time this is updated.\n\n---\n\nRewards: (subject to approval)  \n10p: Pick a transparent image and I'll put it on my stream for an entire week!  \n25p: Pick a game for me to play and I'll play it for around 30min during a Sunday stream!  \n50p: I'll do a rough sketch of your choice! (may take quite a while)  \n100p: Make a custom request!  \nTo redeem a reward, send me a message on Twitch or Discord!  \n---\nCurrent drawing queue:  \n1. Anya (NovaPantsu), test drawing  \n2. Hex (similar to given reference), requested by hell_errol  \n---"
	# Add table header
	page += '\n\n<table class="table">\n  <thead>\n    <tr>\n      <th scope="col">Rank</th>\n      <th scope="col">Username</th>\n      <th scope="col">Visits</th>\n      <th scope="col">Points</th>\n    </tr>\n  </thead>\n  <tbody>\n'
	# Group by visits
	sorted_leaderboard = {}
	for user in users:
		if users[user] in sorted_leaderboard.keys():
			sorted_leaderboard[users[user]].append(user)
		else:
			sorted_leaderboard[users[user]] = [user]
	# Create leaderboard
	rank = 1
	for point in sorted(sorted_leaderboard.keys(), reverse=True):
		# Sort alphabetically
		point_users = sorted(sorted_leaderboard[point], key=str.casefold)
		for user in point_users:
			page += '    <tr>\n      <th scope="row">%s</th>\n      <td><a href="https://www.twitch.tv/%s">%s</a></td>\n      <td>%s</td>\n      <td>%s</td>\n    </tr>\n' % (rank, user.lower(), user, point, points[user])
		rank += 1
	page += '  </tbody>\n</table>'
	out_file.write(page)
