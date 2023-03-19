import json, os

with open('leaderboard.json') as lb_file:
	lb = json.load(lb_file)

files = os.listdir('/home/scuttlest/Desktop/twitch/redeems/checkin/')

for file in files:
	print(file)
	with open('/home/scuttlest/Desktop/twitch/redeems/checkin/' + file, 'r') as in_file:
		jdata = json.load(in_file)
	un = jdata['data']['redemption']['user']['display_name']
	print(un)
	if un in lb['ranks'].keys():
		lb['ranks'][un] += 1
	else:
		lb['ranks'][un] = 1
	if un in lb['points'].keys():
		lb['points'][un] += 1
	else:
		lb['points'][un] = 1
	
	os.remove('/home/scuttlest/Desktop/twitch/redeems/checkin/' + file)

with open('leaderboard.json', 'w') as out_file:
	out_file.write(json.dumps(lb, indent=4))
