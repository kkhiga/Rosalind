#%%
%reset
from timeit import default_timer as timer
start = timer()

with open('rosalind_revc.txt') as dataset:
    dna_sequence = dataset.readline().strip()
    complement = ''
    i = len(dna_sequence) - 1
    while i >= 0:
        if dna_sequence[i] == 'A':
            complement += 'T'
        if dna_sequence[i] == 'T':
            complement += 'A'
        if dna_sequence[i] == 'G':
            complement += 'C'
        if dna_sequence[i] == 'C':
            complement += 'G'
        i -= 1
    with open('rosalind_revc_out.txt', 'w') as output:
        output.write(complement)

end = timer()
print("Time Elapsed: " + str(end - start) + " seconds")