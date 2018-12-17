class child(object):
	__slots__ = ['num_children', 'metadata_len', 'children', 'metadata']

def main():
	license = ""

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
			node.children = list()
			node.metadata = 0

			print('pushing idx ' + str(idx) + ' with metadata_len ' + str(node.metadata_len) + ' and #children ' + str(node.num_children))

			if (len(nodes) > 0):
				nodes[-1].children.append(node)

			nodes.append(node)

			idx = idx + 2

		if license[idx] == 0:
			lidx = idx + 2
			chnode = child()

			chnode.num_children = 0
			chnode.metadata_len = 0
			chnode.metadata = 0

			print('summing up idx ' + str(idx))
			while lidx < (idx + 2 + license[idx + 1]):
				chnode.metadata = chnode.metadata + license[lidx]
				lidx = lidx + 1

			print('metadata is now ' + str(chnode.metadata))

			nodes[-1].children.append(chnode)

			idx = lidx

			nodes[-1].num_children = nodes[-1].num_children - 1

			while nodes[-1].num_children == 0:
				node = nodes.pop()
				lidx = idx

				print('summing up metalen ' + str(node.metadata_len))
				#print(len(node.children))
				while lidx < (idx + node.metadata_len):
					#print(license[lidx])
					if (license[lidx] - 1) <= (len(node.children) - 1):
						print('meta + ' + str(node.children[license[lidx] - 1].metadata))
						node.metadata = node.metadata + node.children[license[lidx] - 1].metadata
					lidx = lidx + 1

				#print('metadata is now ' + str(metadata))

				if len(nodes) == 0:
					print('final metadata: ' + str(node.metadata))
					return

				nodes[-1].num_children = nodes[-1].num_children - 1

				idx = lidx
main()