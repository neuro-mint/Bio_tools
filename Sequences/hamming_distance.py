seq1 ='GCTGCTATCAGACACTCTTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT'
seq2 ='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

def hamming_dist(seq1, seq2):

	dist = 0
	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			dist +=0
		else:
			dist +=1 

	return dist

hd = hamming_dist(seq1, seq2)
print(hd)
