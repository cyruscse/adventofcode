def main():
	reqs = dict()
	letters = set()
	order = list()
	letter_value = dict()
	second = 0
	workers = dict()
	workers_letters = dict()
	num_workers = 5
	moves = list()
	working = False

	with open('input.txt') as f:
		for line in f:
			instruction = line.replace('Step ', '').replace(' must be finished before step ', ' ').replace(' can begin.', '').split()

			letters.add(instruction[0])
			letters.add(instruction[1])

			if instruction[0] not in letter_value:
				letter_value[instruction[0]] = (ord(instruction[0]) - 64) + 60

			if instruction[1] not in letter_value:
				letter_value[instruction[1]] = (ord(instruction[1]) - 64) + 60
			
			if instruction[1] not in reqs:
				reqs[instruction[1]] = list()

			reqs[instruction[1]].append(instruction[0])

	idx = 0

	while idx < num_workers:
		workers[idx] = 0
		workers_letters[idx] = ''
		idx = idx + 1

	while len(reqs.keys()) > 0 or working == True:
		for worker in workers.keys():
			if workers[worker] > 0 or workers_letters[worker] == '':
				continue

			order.append(workers_letters[worker])

			for letter in letters:
				if letter not in reqs.keys():
					continue

				if workers_letters[worker] in reqs[letter]:
					reqs[letter].remove(workers_letters[worker])

					if len(reqs[letter]) is 0:
						del reqs[letter]

			workers_letters[worker] = ''

			working = False
			for w2 in workers.keys():
				if workers[w2] > 0:
					working = True
					break

		if len(moves) == 0:
			for letter in letters:
				if letter not in reqs.keys() and letter not in order and letter not in workers_letters.values():
					moves.append(letter)

			moves = sorted(moves)

		for worker in workers.keys():
			if workers[worker] > 0 or len(moves) == 0:
				continue

			workers_letters[worker] = moves[0]
			workers[worker] = letter_value[moves.pop(0)]
			working = True

		for worker in workers.keys():
			if workers[worker] == 0:
				continue

			workers[worker] = workers[worker] - 1


		second = second + 1
		#print(workers)
		#print(workers_letters)

	print(order)
	print(second - 1)

main()