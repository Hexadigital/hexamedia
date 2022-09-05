import datetime

# TODO: replace with non-hardcoded list
users = {
	'armadevil': 10,
	'doctagon': 11,
	'glyx0': 1,
	'hell_errol': 20,
	'jimmy_mapp': 22,
	'LordLiquidBaconII': 1,
	'Mi5KL_': 13,
	'MoodyPresence_': 9,
	'nabunan': 1,
	'Nanodan_': 29,
	'Ratyyy': 16,
	'Rezuul': 1,
	'peteshroon': 1,
	'SilasWisterum': 1,
	'srdoes': 1,
	'sudowoodoaapp2': 1,
	'SwooshyCueb': 5,
	'TheGenieA1': 1,
	'Weiss_Hikari': 5,
	'Wishengrad': 25,
}

print("Regenerating leaderboard...")
with open('./content/pages/leaderboard.md', 'w') as out_file:
	# Add page header
	page = "Title: Twitch Leaderboard\nSummary: See who has attended the most Twitch streams.\nStatus: Hidden\n\nAre you missing from this list? Purchase the Stream Check-In reward during [my streams](https://twitch.tv/hexadigital) and you'll be added next time this is updated.\n\nLast Updated: "
	# Add timestamp
	page += datetime.datetime.now().strftime('%Y-%m-%d, %H:%M Eastern')
	# Add table header
	page += '\n\n<table class="table">\n  <thead>\n    <tr>\n      <th scope="col">Rank</th>\n      <th scope="col">Username</th>\n      <th scope="col">Visits</th>\n    </tr>\n  </thead>\n  <tbody>\n'
	# Group by points
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
			page += '    <tr>\n      <th scope="row">%s</th>\n      <td><a href="https://www.twitch.tv/%s">%s</a></td>\n      <td>%s</td>\n    </tr>\n' % (rank, user.lower(), user, point)
		rank += 1
	page += '  </tbody>\n</table>'
	out_file.write(page)
