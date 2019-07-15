import argparse


def get_args():
	parser = argparse.ArgumentParser(
		description="Given a lattice, basis and optional additional arguments " +
		"will generate a structure file suitable for loading into PGMC."
	)

	parser.add_argument(
		'-o', '--output-file', dest='output_file_path', type=str, 
		required=True, help='Where to write the output file.'
	)

	parser.add_argument(
		'-e', '--elements', dest='element_names', type=str, required=True, 
		nargs='*', help='The element to use. If the mass is already known, ' +
		'you don\'t need to enter it.'
	)

	parser.add_argument(
		'-m', '--mass', dest='element_names', type=str, default=[], 
		nargs='*', metavar='element mass', help='The mass of each element.'
	)

	parser.add_argument(
		'-r', '--repetitions', dest='repetitions', type=float, required=True, 
		nargs=3, metavar=('x_rep', 'y_rep', 'z_rep'),
		help='The number of repetitions of the structure in each direction.'
	)

	parser.add_argument(
		'--fcc', dest='fcc_a', type=float, default=0.0,
		help='Create a face centered cubic structure with this parameter.'
	)

	parser.add_argument(
		'--bcc', dest='bcc_a', type=float, default=0.0,
		help='Create a body centered cubic structure with this parameter.'
	)

	parser.add_argument(
		'--hcp', dest='hcp_a', type=float, default=0.0,
		help='Create a hexagonal closed packed structure with this parameter.'
	)

	parser.add_argument(
		'--dc', dest='dc_a', type=float, default=0.0,
		help='Create an diamond cubic structure with this parameter.'
	)

	parser.add_argument(
		'-lc', '--lattice-cubic', dest='lattice_cubic_size', type=float, 
		default=0.0, help='Use a cubic lattice with this parameter.'
	)

	parser.add_argument(
		'-l1', '--lattice-vec-1', dest='lattice01', metavar=('x', 'y', 'z'), 
		type=float, nargs=3, help='First lattice vector.'
	)

	parser.add_argument(
		'-l2', '--lattice-vec-2', dest='lattice02', metavar=('x', 'y', 'z'), 
		type=float, nargs=3, help='Second lattice vector.'
	)

	parser.add_argument(
		'-l3', '--lattice-vec-3', dest='lattice03', metavar=('x', 'y', 'z'), 
		type=float, nargs=3, help='Third lattice vector.'
	)

	parser.add_argument(
		'-b', '--basis-vecs', dest='basis_vectors', type=float, nargs='*', 
		metavar='x y z element',
		help='All of the basis vectors for the structure.'
	)

	return parser.parse_args()

def val_args(args):
	if args.fcc_a != 0.0:
		print("--fcc is not implemented.")

	if args.bcc_a != 0.0:
		print("--bcc is not implemented.")

	if args.hcp_a != 0.0:
		print("--hcp is not implemented.")

	if args.dc_a != 0.0:
		print("--dc is not implemented.")

	# Make sure that the element has a known mass.
	lowercased = []
	for element in args.element_names:
		lowercased.append(element.lower())
		if element.lower() not in elements:
			print("The element %s is not in the list of known masses."%element)
			print("Please use ")

elements = {
	'cu' : 63.546,
	'si' : 28.0855,
	'al' : 26.9815384
}


if __name__ == '__main__':
	args = get_args()