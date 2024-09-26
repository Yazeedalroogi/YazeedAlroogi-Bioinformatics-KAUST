LOG FOR GENE FINDER


1) Made a gene finder to read a fasta/fna file and find all genes in all reading frames ignoring reverse complements. The algorithm does considers overlapping genes. Thus, any region between a start and a stop codon is registered as a gene. I initially tried to ignore start codons in the middle of an ORF, but the Rosalind problem (problem 72) seemed to require consideration of ALL regions between a start and stop codon. The algorithm first records the provided genome, then through a while loop, the program looks at every nucleotide in the sequence searching for a start codon. If a start codon is found, its position is saved in a variable and another while loop is started from that start codon until a stop codon is found. The second while loop increments by values of 3 to maintain the reading frame between the start and stop codons. But the first while loop increments by values of 1 to find start codons in any reading frame.

The code for this problem is saved on GitHub under "P1_gene_finder.py"


2) Added the reverse complement to the same algorithm from above. First the reverse complement is found using BioPython. Then the same approach from Problem 1 is repeated for both the sequence and its reverse complement.

The code for this problem is saved on GitHub under "P2_gene_finder.py"


3) After performing the algorithm from problems 2, the genes found are converted to proteins by using BioPython functions to first transcribe each gene and then translate it. To handle repeated proteins, the output protein list is converted to a set and then back to a list.

The code for this problem is saved on GitHub under "P3_gene_finder.py"



4) Ran the algorithm on the 14 bacteria genomes using the bash for loop, and saved each one to the same .txt file. To distinguish between each genome, the file name is first appeneded to the .txt file and then its associated analysis.

The code for this problem is saved on GitHub under "P4_gene_finder.sh", and the output file is under "P4_gene_finder_result.txt"


5) Added a minimum codon parameter. The parameter is optional and its default value is 100. This is done through a try except block that checks if the user inputted a second parameter (codon minimum) or not and either assigns the input value or the default value.

The code for this problem is saved on GitHub under "P5_gene_finder.py"



6) Added a filter for the Shine-Dalgarno sequence, which searches for the Shine-Dalgarno sequence upstream of the start codon. How far the algorithm searches is 20bp by default, but can be specificed by the user as a parameter. In this implementation, 20bp away means that the algorithm looks at the 20bps upstream of a start codon and searches for the Shine-Dalgarno sequence in those 20bps. For efficiency, this step is performed immediately after finding a start codon. If the Shine-Dalgarno sequence exists, then the algorithm searches for the stop codon. But if the sequence does not exist, the programs skips to looking for the next start codon.

The code for this problem is saved on GitHub under "P6_gene_finder.py"