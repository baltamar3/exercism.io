def to_rna(dna_strand):
    rna = ""
    for nucleotid in dna_strand:
        if nucleotid is "C": rna+="G"
        elif nucleotid is "G": rna+="C"
        elif nucleotid is "T": rna+="A"
        elif nucleotid is "A": rna+="U"
    return rna
