#! /bin/bash
#make 3 directories ligands outputs and logs
for f in ligand_folder/*.pdbqt; do
    b=`basename $f .pdbqt`
    echo Processing ligand $b
    vina --config conf.txt --ligand $f --out outputs/${b}out.pdbqt --log logs/${b}log.txt
done