DNA_Nucleotides = ['A', 'T', 'G', 'C']
RNA_Nucleotides = ['A', 'U', 'G', 'C']
codon_dict = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'U', 'ACC':'U', 'ACG':'U', 'ACU':'U',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                 
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    }
reverse_complement_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
RNA_dict = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}

#validates DNA or RNA sequence
def validate_seq(seq):
	seq = seq.upper()
	for i in seq:
		if i not in DNA_Nucleotides or RNA_Nucleotides:
			return False
		else:
			return seq

#generate random sequence
def gen_DNAseq():
	n = int(input('Enter the length of the sequence :'))
	import random
	random_seq = ''.join([random.choice(DNA_Nucleotides)
		for i in range(n) ])
	return random_seq

def gen_RNAseq():
	n = int(input('Enter the length of the sequence :'))
	import random
	random_seq = ''.join([random.choice(RNA_Nucleotides)
		for i in range(n) ])
	return random_seq

#gives seq info and GC content
def seq_info(seq):
	n_dict = {'A':0, 'T':0, 'C':0, 'G':0}
	for i in seq:
		n_dict[i] +=1
	return n_dict

#computes GC content
def gc_count(seq):
	gc_content = n_dict['G'] + n_dict['C']/len(seq)*100
	return gc_content

#converts DNA sequence to RNA sequence
def transcription(seq):
	return ''.join([RNA_dict[i] for i in seq])[::-1]

#converts RNA sequence to list of amino acids in the protein
def translate(seq, init_pos=0):
	init_pos = seq.index('AUG')
	print('Index of start codon:', init_pos)
	return [codon_dict[seq[i:i+3]] for i in range(init_pos, len(seq), 3)]

#Reverse compliment
def reverse_comp(seq):
  return ''.join([rever_complement_dict[i] for i in seq])[::-1]

# DNA pattern
def DNA_pattern(seq):
	print("5'", seq, "3'")
	print(f"   {''.join(['|' for i in range(len(seq))])}")
	print("3'",reverse_comp(seq), "5'" )
 
seq = gen_DNAseq()
print(seq_info(seq), '\n')

DNA_pattern(seq)
print(' \n Reverse complement :', reverse_comp(seq), '\n')

RNA_seq = transcription(seq)
print('5  ', RNA_seq, '\n')

protein = translate(RNA_seq)
print(protein)


