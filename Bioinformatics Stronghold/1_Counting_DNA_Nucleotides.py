#%%
%reset
from timeit import default_timer as timer
start = timer()

with open('rosalind_DNA.txt') as dataset:
    sequence = dataset.readline().strip()

    A_count = C_count = G_count = T_count = 0

    for symbol in sequence:
        if symbol == 'A':
            A_count += 1
        if symbol == 'C':
            C_count += 1
        if symbol == 'G':
            G_count += 1
        if symbol == 'T':
            T_count += 1

    with open('rosalind_dna_out.txt', 'w') as output:
        output.write(str(A_count) + ' ' + str(C_count) + ' ' + str(G_count) + ' ' + str(T_count))

end = timer()
print("Time Elapsed: " + str(end - start) + " seconds")
