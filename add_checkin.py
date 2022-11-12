import json

with open('leaderboard.json') as lb_file:
	lb = json.load(lb_file)

usernames = [x.strip() for x in input("Usernames, space separated: ").split(" ")]

for un in usernames:
	if un in lb['ranks'].keys():
		lb['ranks'][un] += 1
	else:
		lb['ranks'][un] = 1
	if un in lb['points'].keys():
		lb['points'][un] += 1
	else:
		lb['points'][un] = 1

with open('leaderboard.json', 'w') as out_file:
	out_file.write(json.dumps(lb, indent=4))