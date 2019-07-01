#%%
with open('rosalind_rna.txt') as dataset:
    dna_sequence = dataset.readline().strip()
    rna_sequence = ''

    for symbol in dna_sequence:
        if symbol == 'T':
            rna_sequence += 'U'
        else:
            rna_sequence += symbol
    with open('rosalind_rna_out.txt', 'w') as output:
        output.write(rna_sequence)