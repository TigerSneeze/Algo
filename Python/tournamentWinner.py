"""
find the winner

example:
competiions = [[a, b], [c, a], [c, b]]
results = [0,0,1]

1 - home team win     0 - away team win
[home, away]
"""

def tournamentWinner(competitions, results):
    # Write your code here.
	teams = []
	for c in competitions:
		for t in c:
			if t not in teams:
				teams.append(t)
	scores = [0] * len(teams)
	
	for i in range(len(results)):
		if results[i] == 0:
			r_win = teams.index(competitions[i][1])
			scores[r_win] += 1
		if results[i] == 1:
			r_win = teams.index(competitions[i][0])
			scores[r_win] += 1
	
    return teams[scores.index(max(scores))]
