def main():
	w, h = 1000, 1000
	elfs = set()

	matrix = [[list() for x in range(w)] for y in range(h)]

	with open('input.txt') as f:
		for line in f:
			args = line.split()
			elf = int(args[0].strip("#"))
			coords = list(map(int, args[2].strip(":").split(",")))
			dim = list(map(int, args[3].split("x")))
			xidx = int(coords[0])
			yidx = int(coords[1])

			while xidx < (coords[0] + dim[0]):
				yidx = int(coords[1])
				while yidx < (coords[1] + dim[1]):
					matrix[xidx][yidx].append(elf)
					yidx = yidx + 1
				xidx = xidx + 1
			elfs.add(elf)

		count = 0
		check_elves = set()
		for x in matrix:
			for y in x:
				if (len(y) > 1):
					for loopelf in y:
						check_elves.add(loopelf)
					count = count + 1

		print(len(elfs))
		print(len(check_elves))
		print(elfs - check_elves)
		#print(matrix)
		print(count)
main()