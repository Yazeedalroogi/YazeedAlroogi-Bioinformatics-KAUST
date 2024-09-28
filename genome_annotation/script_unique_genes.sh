#!/bin/bash

echo > unique_genes.txt
counter=1
for file in $(find -name 'prokka_raw_*')
do
    echo $counter
    echo $file
    grep_file=$(find $file -name "*.tsv")
    cut -f 4 $grep_file | grep -o ".*" >> unique_genes.txt
    counter=$((counter+1))
done

cat unique_genes.txt | grep -v "gene" | tail -n +2| sort -u > filtered_unique_genes.txt
wc -l filtered_unique_genes.txt > count_unique_genes.txt
head -n 5 filtered_unique_genes.txt > first_five_unique_genes.txt
