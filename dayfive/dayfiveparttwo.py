def main():
	real_input = ""
	tested = dict()

	with open('input.txt') as f:
		for line in f:
			real_input = line

	char_index = 0
	index = 0

	while len(tested) < 26:
		char = real_input[char_index].upper()

		if char in tested:
			char_index = char_index + 1
			continue

		index = 0
		input = real_input.replace(char, '')
		input = input.replace(char.lower(), '')

		while 1:
			if (index + 1) == len(input):
				break

			if (input[index] != input[index + 1]) and (input[index].upper() == input[index + 1].upper()):
				input = input[:index] + input[index + 2:]

				if index > 10:
					index = index - 10
				else:
					index = 0
				continue
			index = index + 1

		tested[char] = len(input)
		char_index = char_index + 1

	print(min(tested.values()))

main()