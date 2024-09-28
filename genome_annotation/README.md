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


4) I ran a bash script on all GCA .fna files from the 14 genomes we downloaded. The script first intitiates a .tsv file with a column for file name and column for gene count. Then, using a for loop, I ran prokka on each file. To count the instances of CDS in each genome, I ran a grep command on the .tsv files output by prokka: "grep -c 'CDS' filename.tsv". Finally, I recorded the numbers in the .tsv file mentioned above. To systematically save each prokka analysis, I defined a counter variable, and save each prokka analysis in a directory named "prokka_raw_counter" using this command:
"prokka --quiet $file --outdir prokka_raw_$counter"

Then, I ran this command to find the .tsv file output by prokka:
"grep_file=$(find prokka_raw_$counter -name '*.tsv')"

Finally, I ran this command to save the grep result in my .tsv file:
"echo -e "$file\t$(grep -c "CDS" $grep_file)" >> prokka_results.tsv"


Comparing the prokka CDS counts with the prodigal counts, there are slight differences. Across the board, prodigal had either an equal or higher number of genes for each genomes. I think the reason behind this is that prodigal does not specif the gene type, while prokka labels each genes as either CDS or tRNA (and maybe other labels as well) in the .tsv file under the ftype column. Thus, looking at only CDS genes from prokka will always result in one of two cases. a) Prokka only found CDS genes, and thus has an equal number of CDS genes to the genes found by prodigal. b) Prokka found more than one type of gene, and thus has a smaller number of CDS genes to the genes found by prodigal.

The script file is available on Github under "prokka_script.sh", and the results are under "prokka_results.tsv"  


5) I ran bash script on all .tsv files output from prokka. I first cut the fourth column of the .tsv which includes gene names. Then, I added all gene names from all .tsv files into one .txt file through a for loop. Finally, I ran a command to find all unique gene names. However, since uniq onnly filteres adjacent lines, I had to use sort -u to find unique gene names. This is the command I used:
cat unique_genes.txt | grep -v "gene" | tail -n +2| sort -u > filtered_unique_genes.txt

Then to count the number of unique genes, I used this command:
wc -l filtered_unique_genes.txt > count_unique_genes.txt
head -n 5 filtered_unique_genes.txt > first_five_unique_genes.txt

This resulted in 5726 unique genes, and the first five are:
aaaT
aaeA
aaeA_1
aaeA_2
aaeB


The script is available on GitHub under the name "script_unique_genes.sh", the list of all unique genes is under "filtered_unique_genes.txt", the count of unique genes is under "count_unique_genes.txt", and the first five unique genes is under "first_five_unique_genes.txt" 
