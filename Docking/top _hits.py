import os
import glob

def filter_res():
    energy = -5
    f_names = glob.glob('*.pdbqt')
    all = []
    
    for f in f_names:
        files = open(f)
        lines = files.readlines()
        files.close()

        lines = lines[1]
        res = float(lines.split(':')[1].split()[0])
        all.append([res, f])
    
    neg = []
    for i in all:
        if i[0]<-energy:
            neg.append(i)
        else:
            pass
    
    for i in range(len(neg)):
        print(neg[i])
    return neg

filter_res()
