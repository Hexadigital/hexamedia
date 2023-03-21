import json, os

with open('leaderboard.json') as lb_file:
	lb = json.load(lb_file)

files = os.listdir('../../Desktop/twitch/redeems/checkin/')

for file in files:
	#print(file)
	with open('../../Desktop/twitch/redeems/checkin/' + file, 'r') as in_file:
		jdata = json.load(in_file)
	un = jdata['data']['redemption']['user']['display_name']
	uid = str(jdata['data']['redemption']['user']['id'])
	print(uid, un)
	lb["id_to_username"][uid] = un
	if uid in lb['ranks'].keys():
		lb['ranks'][uid] += 1
	else:
		lb['ranks'][uid] = 1
	if uid in lb['points'].keys():
		lb['points'][uid] += 1
	else:
		lb['points'][uid] = 1
	
	os.remove('../../Desktop/twitch/redeems/checkin/' + file)

with open('leaderboard.json', 'w') as out_file:
	out_file.write(json.dumps(lb, indent=4))
