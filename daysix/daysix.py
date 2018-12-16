def calc_taxicab(coord1, coord2):
	x = abs(coord1[0] - coord2[0])
	y = abs(coord1[1] - coord2[1])

	return (x + y)

def main():
	all_coords = list()
	matrix = [[list() for _ in range(400)] for _ in range(400)]
	index = 1
	low_x = 1000
	low_y = 1000
	max_x = 0
	max_y = 0
	score = dict()

	with open('input.txt') as f:
		for line in f:
			coords = line.replace(' ', '').split(',')
			coords[0] = int(coords[0])
			coords[1] = int(coords[1])

			if coords[0] > max_x:
				max_x = coords[0]

			if coords[1] > max_y:
				max_y = coords[1]

			if coords[0] < low_x:
				low_x = coords[0]

			if coords[1] < low_y:
				low_y = coords[1]

			matrix[coords[1]][coords[0]] = index
			score[index] = 1

			all_coords.append(coords)
			index = index + 1

	print(max_x)
	print(max_y)
	print(low_x)
	print(low_y)

	lowest_taxicab = [1, 400]
	equidistant = False

	for x in range(400):
		for y in range(400):
			if x > (max_x + 1) or y > (max_y + 1):
				continue

			if [x, y] in all_coords:
				continue

			matrix_coord = [x, y]
			index = 1
			lowest_taxicab = [1, 400]
			lowest_taxicab_set = False
			equidistant = False

			for entry in all_coords:
				txi = calc_taxicab(matrix_coord, entry)

				if txi != -1:
					if txi == lowest_taxicab[1]:
						equidistant = True
					elif txi < lowest_taxicab[1]:
						lowest_taxicab_set = True
						equidistant = False
						lowest_taxicab = [index, txi]

				index = index + 1

			if lowest_taxicab_set == True and equidistant == False:
				matrix[y][x] = lowest_taxicab[0]

				score[lowest_taxicab[0]] = score[lowest_taxicab[0]] + 1

	for x in range(400):
		for y in range(400):
			if isinstance(matrix[x][y], int):
				continue

			if len(matrix[x][y]) == 0:
				matrix[x][y] = ' '

	index = 0

	for entry in score.keys():
		if all_coords[index][0] == max_x or all_coords[index][0] == low_x or all_coords[index][1] == max_y or all_coords[index][1] == low_y:
			score[entry] = 0
		index = index + 1

	for x in range(400):
		print(matrix[x])

	print(score)
	print(max(score.values()))

main()