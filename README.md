
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