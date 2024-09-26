from Bio.Seq import Seq
from Bio.SeqUtils import GC, nt_search
from Bio import SeqIO
import sys

input_file = sys.argv[1]

try:
    codon_min = int(sys.argv[2])

except:
    codon_min = 100

try:
    shine_range = int(sys.argv[3])

except:
    shine_range = 20


if codon_min == 0:
    codon_min = 1
    
def gene_finder(file, codon_min, shine_range):
    with open(file) as f:
        dna = ""
        for record in SeqIO.parse(f, "fasta"):
            dna += record.seq


        rev_comp = str(Seq(dna).reverse_complement())
            
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]
        shine_delgarno = "AGGAGG"
        shine_length = 6
        
        codonL = 3
        frame = 0

        genes = []

        curr_start = -1
        curr_stop  = -1


        text_ind = shine_length - 1
        while text_ind < len(dna) - codonL:
            if dna[text_ind:text_ind+codonL] == start_codon:
                shineExists = False
                
                curr_start = text_ind
                
                if text_ind < shine_range:
                    shine_start = 0

                else:
                    shine_start = text_ind - shine_range


                while shine_start != text_ind:
                    if dna[shine_start:shine_start+shine_length] == shine_delgarno:
                        shineExists = True
                        break

                    shine_start += 1
                    

                if shineExists:
                    for i in range(curr_start+codonL, len(dna), 3):
                        if dna[i:i+codonL] in stop_codons:
                            curr_stop = i+codonL

                            if ((curr_stop - curr_start)/codonL) >= (codon_min):
                                genes.append(dna[curr_start:curr_stop])
                                text_ind = curr_start + codonL
                                break

            text_ind += 1


        text_ind = shine_length - 1
        while text_ind < len(rev_comp) - codonL:
            if rev_comp[text_ind:text_ind+codonL] == start_codon:
                shineExists = False
                
                curr_start = text_ind
                
                if text_ind < shine_range:
                    shine_start = 0

                else:
                    shine_start = text_ind - shine_range


                while shine_start != text_ind:
                    if rev_comp[shine_start:shine_start+shine_length] == shine_delgarno:
                        shineExists = True
                        break

                    shine_start += 1
                    

                if shineExists:
                    for i in range(curr_start+codonL, len(rev_comp), 3):
                        if rev_comp[i:i+codonL] in stop_codons:
                            curr_stop = i+codonL

                            if ((curr_stop - curr_start)/codonL) >= (codon_min):
                                genes.append(rev_comp[curr_start:curr_stop])
                                text_ind = curr_start + codonL
                                break

            text_ind += 1

        proteins = []
        for gene in genes:
            rna = Seq(gene[:-3]).transcribe()
            proteins.append(str(rna.translate()))

        return genes, list(set(proteins))


all_genes = gene_finder(input_file, codon_min, shine_range)
print(all_genes)        
