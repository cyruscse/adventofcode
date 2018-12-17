class child(object):
	__slots__ = ['num_children', 'metadata_len']

def main():
	license = ""
	metadata = 0

	with open('input.txt') as f:
		for line in f:
			license = line

	license = list(map(int, license.split()))
	nodes = list()
	idx = 0

	while idx < (len(license) - 2):
		if license[idx] > 0:
			node = child()
			node.metadata_len = license[idx + 1]
			node.num_children = license[idx]

			print('pushing idx ' + str(idx) + ' with metadata_len ' + str(node.metadata_len) + ' and #children ' + str(node.num_children))

			nodes.append(node)

			idx = idx + 2

		if license[idx] == 0:
			lidx = idx + 2

			print('summing up idx ' + str(idx))
			while lidx < (idx + 2 + license[idx + 1]):
				metadata = metadata + license[lidx]
				lidx = lidx + 1

			print('metadata is now ' + str(metadata))

			idx = lidx

			nodes[-1].num_children = nodes[-1].num_children - 1

			while nodes[-1].num_children == 0:
				node = nodes.pop()
				lidx = idx

				print('summing up metalen ' + str(node.metadata_len))
				while lidx < (idx + node.metadata_len):
					metadata = metadata + license[lidx]
					lidx = lidx + 1

				print('metadata is now ' + str(metadata))

				if len(nodes) == 0:
					print('final metadata: ' + str(metadata))
					return

				nodes[-1].num_children = nodes[-1].num_children - 1

				idx = lidx
main()