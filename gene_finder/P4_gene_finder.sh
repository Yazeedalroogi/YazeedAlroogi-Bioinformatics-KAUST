#!/bin/bash

echo > P4_gene_finder_result.txt
for file in $(find ../../ncbi_dataset/data/ -name 'GCA*fna')
do
    echo $file
    echo $file >> P4_gene_finder_result.txt
    python gene_finder.py $file >> P4_gene_finder_result.txt
done
