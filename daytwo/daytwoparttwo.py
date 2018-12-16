def main():
	index = 1
	charidx = 0
	diffs = 0
	fp = open('input.txt')

	with open('input.txt') as f:
		for line in f:
			fp = open('input.txt')
			for i, check_line in enumerate(fp):
				if i >= index:
					for char in line:
						if check_line[charidx] != char:
							diffs = diffs + 1

						charidx = charidx + 1

					if diffs == 1:
						print(line)
						print(check_line)
						print("succ")
						return

					diffs = 0
					charidx = 0
			index = index + 1

main()