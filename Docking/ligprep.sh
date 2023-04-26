#! /bin/bash
# this shel script utilized the ligand_prep4.py script in autodocktools
# modify the path for as per your location of mgltools
export PATH=/path/mgltools_x86_64Linux2_1.5.7p1/mgltools_x86_64Linux2_1.5.7/bin:$PATH
cd path_to_folder_with_ligands
for f in *.pdb; do
    b=`basename $f .pdb`
    echo Converting ligand to PDBQT $b
    pythonsh /your_path/mgltools_x86_64Linux2_1.5.7p1/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -l path_to_ligands_folder/$f -o path_to_output_folder/$b.pdbqt -A hydrogens 
done
# add a Z flag to keep the ligads rigid
