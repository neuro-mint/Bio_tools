import sys
import glob

def filter_res():
    f_names = glob.glob("path_to_outputs_dir/*.pdbqt")
    energy = -3
    hits = []

    for f in f_names:
        with open(f) as file:
            lines = file.readlines()[1]
            res = float(lines.split(':')[1].split()[0])
            if res <= energy: hits.append([res, f])
    
    hits.sort()
    for i in hitsb: print(i)
    print(f"Number of top hits: {len(hits)}")

filter_res()
