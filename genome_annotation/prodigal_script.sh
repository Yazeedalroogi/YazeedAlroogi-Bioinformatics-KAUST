#!/bin/bash

echo -e "File Name\tNumber of Genes" > prodigal_results.tsv

for file in $(find ../../ncbi_dataset/data/ -name 'GCA*fna')
do
    echo $file
    prodigal -i $file -d temp.fna
    echo -e "$file\t$(grep -c "^>" temp.fna)" >> prodigal_results.tsv
done

cat prodigal_results.tsv | tail -n +2 | sort -nr -k 2 | head -n 1 > highest_genes.txt
