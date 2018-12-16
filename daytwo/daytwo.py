import fileinput

def main():
	two_count = 0
	three_count = 0
	occurrences = 1
	index = 1
	checked_chars = list()
	two_checked = False
	three_checked = False

	with fileinput.input(files=('input.txt')) as f:
		for line in f:
			for char in line:
				if char in checked_chars:
					index = index + 1
					continue
				for charloop in line[index:]:
					if charloop == char:
						occurrences = occurrences + 1

				checked_chars.append(char)

				if occurrences == 2 and two_checked == False:
					two_count = two_count + 1
					two_checked = True
				elif occurrences == 3 and three_checked == False:
					three_count = three_count + 1
					three_checked = True

				occurrences = 1
				index = index + 1
			index = 1
			checked_chars = list()
			two_checked = False
			three_checked = False

	print(two_count)
	print(three_count)
	print(two_count * three_count)

main()