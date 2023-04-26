name = str(input("Enter name for the file : \n"))
seq_space = open('path_here/seq_space' + f'{name}' + '.txt', 'w')

k = int(input('Enter the length of the sequence : \n'))
def seq_space_gen(k):
	set = ['A', 'T', 'G', 'C']
	n = 4 
	genseq(set, "", n, k)

def genseq(set, prefix, n, k):
	if (k == 0) :
		seq = prefix
		seq_space.write(f"{seq}\n")
		return

	for i in range(n):
		newPrefix = prefix + set[i]
		genseq(set, newPrefix, n, k - 1)

	return seq_space

seq_space_gen(k)
seq_space.close()