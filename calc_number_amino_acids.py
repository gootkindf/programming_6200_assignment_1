"""
File   : calc_number_amino_acids.py
History: 25-Sep-2021

This program takes input in the form of a sequence name and its length. If the sequence is not
divisible by 3 it returns an error. It then returns the length of the sequence, the length of the
decoded protein, and the average weight of the resulting protein.
"""

import sys

def main():
	"""Input accepting function"""
	seq = input('Please enter a name for the DNA sequence: ')
	print('Your sequence name is: {}'.format(seq))
	length = int(input('Please enter the length of the sequence: '))
	if length % 3 != 0:
		print("\n\nError: the DNA sequence is not a multiple of 3!", file=sys.stderr)
		# print to STDERR
		sys.exit(1)
	print('The length of DNA sequence is: {}'.format(length))
	print('The length of the decoded protein is: {}'.format(length / 3))
	print('The average weight of the protein sequence is: {}'.format((length / 3) * .110))

if __name__ == '__main__':
	main()
