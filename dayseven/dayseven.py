def main():
	reqs = dict()
	letters = set()
	order = list()

	with open('input.txt') as f:
		for line in f:
			instruction = line.replace('Step ', '').replace(' must be finished before step ', ' ').replace(' can begin.', '').split()

			letters.add(instruction[0])
			letters.add(instruction[1])
			
			if instruction[1] not in reqs:
				reqs[instruction[1]] = list()

			reqs[instruction[1]].append(instruction[0])

	while len(reqs.keys()) > 0:
		moves = list()

		for letter in letters:
			if letter not in reqs.keys() and letter not in order:
				moves.append(letter)

		moves = sorted(moves)
		move = moves[0]

		order.append(move)

		for letter in letters:
			if letter not in reqs.keys():
				continue

			if move in reqs[letter]:
				reqs[letter].remove(move)

			if len(reqs[letter]) is 0:
				del reqs[letter]

		#print(reqs.keys())
		#print(order)
		#print(reqs)
		#print(move)

	for letter in order:
		print(letter, end='')
	print(order)
	print(reqs.keys())

main()