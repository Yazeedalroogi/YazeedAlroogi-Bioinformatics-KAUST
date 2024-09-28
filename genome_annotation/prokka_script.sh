#!/bin/bash

echo -e "File Name\tNumber of Genes" > prokka_results.tsv
counter=1
for file in $(find ../../ncbi_dataset/data/ -name 'GCA*fna')
do
    echo $counter
    echo $file
    prokka --quiet $file --outdir prokka_raw_$counter
    grep_file=$(find prokka_raw_$counter -name '*.tsv')
    echo $grep_file
    echo -e "$file\t$(grep -c "CDS" $grep_file)" >> prokka_results.tsv
    counter=$((counter+1))
done


