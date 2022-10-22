import datetime

# TODO: replace with non-hardcoded list
users = {
	'armadevil': 14,
	'doctagon': 24,
	'glyx0': 1,
	'hell_errol': 46,
	'jimmy_mapp': 49,
	'LordLiquidBaconII': 25,
	'Mi5KL_': 26,
	'MoodyPresence_': 31,
	'nabunan': 6,
	'Nanodan_': 62,
	'Ratyyy': 33,
	'Rezuul': 1,
	'peteshroon': 11,
	'ResidentRising': 5,
	'SilasWisterum': 3,
	'SlimRindy': 5,
	'srdoes': 1,
	'sudowoodoaapp2': 1,
	'SwooshyCueb': 6,
	'TheGenieA1': 6,
	'Weiss_Hikari': 10,
	'Wishengrad': 56,
}

points = {
	'armadevil': 14,
	'doctagon': 24,
	'glyx0': 1,
	'hell_errol': 46,
	'jimmy_mapp': 49,
	'LordLiquidBaconII': 25,
	'Mi5KL_': 26,
	'MoodyPresence_': 31,
	'nabunan': 6,
	'Nanodan_': 62,
	'Ratyyy': 33,
	'Rezuul': 1,
	'peteshroon': 11,
	'ResidentRising': 5,
	'SilasWisterum': 3,
	'SlimRindy': 5,
	'srdoes': 1,
	'sudowoodoaapp2': 1,
	'SwooshyCueb': 6,
	'TheGenieA1': 6,
	'Weiss_Hikari': 10,
	'Wishengrad': 56,
}

print("Regenerating leaderboard...")
with open('./content/pages/leaderboard.md', 'w') as out_file:
	# Add page header
	page = "Title: Twitch Leaderboard\nSummary: See who has attended the most Twitch streams.\nStatus: Hidden\n\nAre you missing from this list? Purchase the Stream Check-In reward during [my streams](https://twitch.tv/hexadigital) and you'll be added next time this is updated.\n\n---\n\nRewards: (subject to approval)  \n10p: Pick a transparent image and I'll put it on my stream for an entire week!  \n25p: Pick a game for me to play and I'll play it for around 30min during a Sunday stream!  \n50p: I'll do a rough pencil sketch of your choice!  \n100p: Make a custom request!  \n---\n\nLast Updated: "
	# Add timestamp
	page += datetime.datetime.now().strftime('%Y-%m-%d, %H:%M Eastern')
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
