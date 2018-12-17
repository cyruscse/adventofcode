def main():
	rule = ""
	players = 0
	marbles = 0
	game = list()
	player_scores = dict()
	current_player = 2
	game_idx = 2
	current_marble_idx = 1
	high_score = 0

	with open('input.txt') as f:
		for line in f:
			rule = line

	rule = rule.split()

	players = int(rule[0])
	marbles = int(rule[len(rule) - 2])

	game.append(0)
	game.append(1)

	while game_idx != marbles:
		play_index = current_marble_idx

		if (play_index + 2) >= (len(game) + 1):
			play_index = 1
		else:
			play_index = play_index + 2

		if game_idx % 23 == 0:
			if current_marble_idx < 7:
				current_marble_idx = len(game) - (7 - current_marble_idx)
			else:
				current_marble_idx = current_marble_idx - 7

			score = game_idx + game.pop(current_marble_idx)
			
			if current_player not in player_scores.keys():
				player_scores[current_player] = score
			else:
				player_scores[current_player] = player_scores[current_player] + score

			if player_scores[current_player] > high_score:
				high_score = player_scores[current_player]
		else:
			game.insert(play_index, game_idx)
			current_marble_idx = play_index
		
		game_idx = game_idx + 1
		current_player = current_player + 1

		if current_player > players:
			current_player = 1

	print(high_score)
main()