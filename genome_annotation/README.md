LOG FOR GENOME ANNOTATION


1) The peptide KVRMFTSELDIMLSVNGPADQIKYFCRHWT* includes 31 amino acids exclusing the start and stop codon. If the start codon is considered, then the number would be 32. This can be confirmed using BASH bu running the command "echo "KVRMFTSELDIMLSVNGPADQIKYFCRHWT" | wc -c" which outputs 31.

The open reading frame includes codons for the 31 amino acids as well as a start codon and a stop codon, thus it has a total of 33 codons. Since each codon is made up of 3 bases, the open reading frame contains 99 bases on a single strand. 


2) I ran prodigal to output a .fna file on the "GCA_000008525.1_ASM852v1_genomic" genome. The command I used was:
prodigal -i GCA_000008525.1_ASM852v1_genomic.fna -d fna_prodigal_results1.fna

Then I used grep to count the annotated genes. Since a .fna files srarts with a ">" for each gene entry, I levarged this using Regex and grep to count the number of genes using the following command:
grep -c "^>" fna_prodigal_results1.fna > fna_prodigal_count.txt

The output number of genes was 1579.

The prodigal output and the count are saved on GitHub under "P2_fna_prodigal_results.fna" and "P2_fna_prodigal_count.txt" respectively.


3) I ran a bash script on all GCA .fna files from the 14 genomes we downloaded. First, the script creates a .tsv file with two columns: File name, and Gene count. Then a for loop runs on each file, where ot first runs prodigal on the file, then saves the results in a temporary .fna file. Then, I run a grep command to count all instances of ">" at the start if a line, which corresponds to the number of genes in .fna file. To save everything to the .tsv file, I run the following command:
echo -e "$file\t$(grep -c "^>" temp.fna)" >> prodigal_results.tsv

Finally, I run the following command to sort through the gene counts, and find the file with the highest gene count:
cat prodigal_results.tsv | tail -n +2 | sort -nr -k 2 | head -n 1 > highest_genes.txt

Here, I first remove the .tsv headers through the tail function. Then, I sort based on column two (the column with gene counts) using the -k flag for sort. Finally, I get the file with the highest gene count using head and save it to a .txt file.
The result of running this bash script is the following:
../../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna    3594

Indicating that GCA_000006745.1_ASM674v1 has the highest gene count of 3594 genes.

The script is saved on GitHub under "prodigal_script.sh", the results under "prodigal_results.tsv", and the highest gene count under "highest_genes.txt"