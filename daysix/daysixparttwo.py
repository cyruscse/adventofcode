def calc_taxicab(coord1, coord2):
	x = abs(coord1[0] - coord2[0])
	y = abs(coord1[1] - coord2[1])

	return (x + y)

def main():
	all_coords = list()
	matrix = [[list() for _ in range(400)] for _ in range(400)]
	index = 0

	with open('input.txt') as f:
		for line in f:
			coords = line.replace(' ', '').split(',')
			coords[0] = int(coords[0])
			coords[1] = int(coords[1])

			all_coords.append(coords)
			matrix[coords[1]][coords[0]] = index
			index = index + 1

	count = 0
 
	for x in range(400):
		for y in range(400):
			coord = [x, y]
			good = True
			sum = 0

			for coords in all_coords:
				sum = sum + calc_taxicab(coord, coords)

				if sum >= 10000:
					good = False
					break

			if good == True:
				count = count + 1

	print(count)
main()