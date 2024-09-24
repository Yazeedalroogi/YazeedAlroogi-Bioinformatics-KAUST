from Bio.Seq import Seq
from Bio.SeqUtils import GC, nt_search
from Bio import SeqIO
import sys

def reverse_complement(dna):
    rev_comp = ""

    for nuc in dna:
        if nuc == "A":
            rev_comp += "T"

        if nuc == "T":
            rev_comp += "A"

        if nuc == "C":
            rev_comp += "G"

        if nuc == "G":
            rev_comp += "C"

    return rev_comp


input_file = sys.argv[1]
def gene_finder(file):
    with open(file) as f:
        dna = ""
        for record in SeqIO.parse(f, "fasta"):
            dna += record.seq


        rev_comp = reverse_complement(dna)
            
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


        text_ind = 0
        while text_ind < len(rev_comp) - codonL:
            if rev_comp[text_ind:text_ind+codonL] == start_codon:
                curr_start = text_ind
                for i in range(curr_start+codonL, len(rev_comp), 3):
                    if rev_comp[i:i+codonL] in stop_codons:
                        curr_stop = i+codonL
                        genes.append(rev_comp[curr_start:curr_stop])
                        text_ind = curr_stop
                        break

            text_ind += 1

        return genes


all_genes = gene_finder(input_file)
print(all_genes, len(all_genes))        
