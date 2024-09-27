#!/bin/bash

echo  > P6_gene_finder_no_codonMin_results.txt
echo  > P6_gene_finder_100_codonMin_results.txt
for file in $(find ../../ncbi_dataset/data/ -name 'GCA*fna')
do
    echo $file
    echo $file >> P6_gene_finder_no_codonMin_results.txt
    python P6_gene_finder.py $file 1 >> P6_gene_finder_no_codonMin_results.txt

    echo $file >> P6_gene_finder_100_codonMin_results.txt
    python P6_gene_finder.py $file 100 >> P6_gene_finder_100_codonMin_results.txt
done
