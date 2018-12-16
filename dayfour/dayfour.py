def main():
	events = list()
	minutes = [[] for _ in range(59)]
	score = dict()

	with open('input.txt') as f:
		for line in f:
			args = line.split('-', 1)[-1].strip('[').replace(']', '').split(' ', 2)
			events.append(args)

	events.sort(key = lambda x: (x[0], x[1]))

	guard_id = -1
	asleep_start = -1

	for entry in events:
		minute = int(entry[1].split(':')[1])

		if '#' in entry[2]:
			guard_id = int(entry[2].split()[1].strip('#'))

		if "falls" in entry[2]:
			asleep_start = int(minute)
		elif "wakes" in entry[2]:
			while asleep_start < minute:
				minutes[asleep_start].append(guard_id)
				asleep_start = asleep_start + 1
			asleep_start = -1

	index = 0

	for minute in minutes:
		for guard in minute:
			if guard in score:
				score[guard] += 1
			else:
				score[guard] = 1

	sleepiest = max(score, key=score.get)
	sleepiest_minute = -1
	sleepiest_count = 0
	index = 0

	for minute in minutes:
		if minute.count(sleepiest) > sleepiest_count:
			sleepiest_count = minute.count(sleepiest)
			sleepiest_minute = index
		index = index + 1

	print(sleepiest)
	print(sleepiest_minute)
main()