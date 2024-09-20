
PROBLEM 3)
Largest: 4033464
Command: cut -f 11 data_summary.tsv | grep -o "[0-9]*" | sort -r | head -n 1

Smallest: 1042519
Command: cut -f 11 data_summary.tsv | grep -o "[0-9]*" | sort | head -n 1

PROBLEM 4)
Number of genomes that contain at least 2 "c" in the species name: 14
Command: cut -f 1 data_summary.tsv | tail -n +2 | grep -o ".*[c,C].*[c,C]"
-- Question: Should we account of C and c or just c? --

Genomes woth 2 or more "c" but no coccus in the name: 10
Command: cut -f 1 data_summary.tsv | tail -n +2 | grep -v "coccus" | grep -i -c ".*[c].*[c]"

PROBLEM 5)
Files greater than 3 Mb:
GCA_000006745.1_ASM674v1_genomic.fna
GCA_000008565.1_ASM856v1_genomic.fna
GCF_000006745.1_ASM674v1_genomic.fna
GCF_000008565.1_ASM856v1_genomic.fna
GCA_000007125.1_ASM712v1_genomic.fna
GCF_000007125.1_ASM712v1_genomic.fna

Command: find -size +3M