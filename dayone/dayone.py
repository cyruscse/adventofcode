import fileinput

def main():
	sum = 0
	sum_memory = set()

	while 1:
		pass
		with fileinput.input(files=('input.txt')) as f:
			for line in f:
				num = int(line[1:])

				if line[0] is '+':
					sum += num
				else:
					sum -= num

				if sum in sum_memory:
					print(sum)
					return

				sum_memory.add(sum)


main()