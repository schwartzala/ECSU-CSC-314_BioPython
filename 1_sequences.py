#########################################################
# Biopython is a set of Python tools for biological
# computation
# for download instructions and an excellent tutorial,
# see: http://biopython.org/wiki/Main_Page)
#########################################################

from Bio.Seq import Seq        # for Seq
from Bio.Alphabet import IUPAC # for alphabet

## sequence with generic alphabet ##
my_seq = Seq("AGTACACTGGT")
print "sequence = ", my_seq
print "alphabet = ", my_seq.alphabet
print

## DNA sequence ##
dna = Seq("ATGACACTGTAGGAA", IUPAC.unambiguous_dna)
print "sequence = ", dna
print "alphabet type = ", dna.alphabet
print "DNA nucleotides = ", dna.alphabet.letters
print

# print DNA complement
print "complement = ", dna.complement()
print

# trascribe from DNA (sense strand) to RNA
rna =dna.transcribe()
print "rna = ", rna
print

# translate from RNA to protein
protein1 = rna.translate()  # dna.translate() also works
print "protein = ", protein1

protein = rna.translate(to_stop = True)
print "protein = ", protein