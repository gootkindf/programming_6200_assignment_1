"""
File   : calc_daltons.py
History: 25-Sep-2021

Takes a .txt file containing a protein sequence and returns its length and weight
"""

def main():
	"""Opens .txt and reads, then prints points of interest"""
	text = open('r_norvegicus_PKC_Beta_1.txt', 'r') # opening sequence file

	seq = text.read() # setting to read mode

	seq = seq.replace('\r', '').replace('\n', '').replace(' ', '') # removing all exraneous characters

	for character in seq: # removing all digits
		if character.isdigit():
			seq = seq.replace(character, '')

	weight = len(seq) * .110 # getting molecular weight

	print('The length of "Protein kinase c beta type" is: {}'.format(len(seq))) # printing results
	print('The average wieght of this protein sequence in kilodaltons is: {}'.format(weight))

if __name__ == "__main__":
	main()
