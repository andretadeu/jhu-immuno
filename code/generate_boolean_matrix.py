import itertools

letters = ['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']

# generates a matrix from all peptides and saves to CSV
def generateBooleanMatrix(peptides):
	# generate header  ------
	peptide_length = 9
	aa_list = ['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']

	positions = []
	for i in xrange(1, peptide_length + 1):
		positions.append("Pos%(i)s" % vars())

	tuples = [e for e in itertools.product(positions, ''.join(aa_list))]

	header = ['peptide']
	for i in xrange(len(tuples)):
		header.append(''.join(tuples[i]))

	# initialize master matrix and add header as a row	
	matrix = []
	matrix.append(header)

	# generate array for each peptide and concatenate -----
	for peptide in peptides:
		print 'Peptide:'	# for testing
		print peptide 		# for testing
		amino_acids = list(peptide)

		peptide_positions = [peptide]
		# create subarray for each position and concatenate
		for i in xrange(len(peptide)):
			subarr = []
			
			# create subarray with boolean values for amino acid presence based on order of aa_list array
			for j in xrange(len(aa_list)):
				if peptide[i] == aa_list[j]:
					subarr += [1]
				else:
					subarr += [0]

			# add extra zeroes if peptide length < maximum peptide length
			if len(amino_acids) < peptide_length:
				for k in xrange(peptide_length - len(aa_list), max_length):
					subarr += [0]

			# concatenate booleans for one position to list
			peptide_positions += subarr
		# add peptide row to master matrix
		matrix.append(peptide_positions)

	return matrix
	
	# save to CSV -------