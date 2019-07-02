#%%
%reset
from timeit import default_timer as timer
start = timer()

CODON_LENGTH = 3
# Parse the RNA Codon Table into a dict, rna_codons
rna_codons = {}
with open('rosalind_rna_codon_table.txt') as table:
    codon_pairs = table.read().split()
    i = 0
    while i < len(codon_pairs):
        # Assign each pair as a key, value in dict
        rna_codons[codon_pairs[i]] = codon_pairs[i + 1]
        i += 2

mrna_sequence = ''
# Parse the RNA sequence and use the rna_codons to translate
with open('rosalind_prot.txt') as dataset:
    rna_sequence = dataset.readline().strip()
    i = 0
    while i < len(rna_sequence) - 2:
        # Get the next codon in the sequence
        codon = rna_sequence[i:i + CODON_LENGTH]
        # Add to the mRNA sequence if the codon is not a 'Stop'
        mrna_sequence += rna_codons[codon] if rna_codons[codon] != 'Stop' else ''
        i += CODON_LENGTH

# Write result to a file, 'rosalind_prot_out.txt'
with open('rosalind_prot_out.txt', 'w') as output:
    output.write(mrna_sequence)

end = timer()
print("Time Elapsed: " + str(end - start) + " seconds")
