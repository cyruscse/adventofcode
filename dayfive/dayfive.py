def main():
	input = ""

	with open('input.txt') as f:
		for line in f:
			input = line

	index = 0
	while 1:
		if (index + 1) == len(input):
			continue

		if (input[index] != input[index + 1]) and (input[index].upper() == input[index + 1].upper()):
			input = input[:index] + input[index + 2:]

			if index > 10:
				index = index - 10
			else:
				index = 0
			continue
		index = index + 1

	print(len(input))

main()
