LOG FOR GENE FINDER


1) Made a gene finder to read a fasta/fna file and find all genes in all reading frames ignoring reverse complements. The algorithm does not consider overlapping genes. That is, if there's a start codon between an upstream start codon and a downstream stop codon, it is ignored and not considered.

The code for the implementation is found below:

from Bio.Seq import Seq
from Bio.SeqUtils import GC, nt_search
from Bio import SeqIO
import sys

input_file = sys.argv[1]
def gene_finder(file):
    with open(file) as f:
        dna = ""
        for record in SeqIO.parse(f, "fasta"):
            dna += record.seq

        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]

        codonL = 3
        frame = 0

        genes = []

        curr_start = -1
        curr_stop  = -1
        text_ind = 0
        while text_ind < len(dna) - codonL:
            if dna[text_ind:text_ind+codonL] == start_codon:
                curr_start = text_ind
                for i in range(curr_start+codonL, len(dna), 3):
                    if dna[i:i+codonL] in stop_codons:
                        curr_stop = i+codonL
                        genes.append(dna[curr_start:curr_stop])
                        text_ind = curr_stop
                        break

            text_ind += 1

        return genes


all_genes = gene_finder(input_file)
print(all_genes, len(all_genes))