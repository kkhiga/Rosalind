#%%
%reset
from timeit import default_timer as timer
start = timer()

def calc_GC(sequence):
    GC_count = 0
    for symbol in sequence:
        if symbol == 'G' or symbol == 'C':
            GC_count += 1
    GC_content = (GC_count / (len(sequence))) * 100
    return GC_content


with open('rosalind_gc.txt') as dataset:
    highest_GC = 0
    sequence_id = ''
    lines = dataset.read().replace('\n', '').strip().split('>')
    for line in lines:
        if line:
            name = line[0:13]
            # Parse the sequence after the sequence ID
            sequence = line[13:]
            # Calculate the GC content
            GC_content = calc_GC(sequence)
            if GC_content > highest_GC:
                highest_GC = GC_content
                sequence_id = line[0:13]

    with open('rosalind_gc_out.txt', 'w') as output:
        output.write('%s\n%s' % (sequence_id, highest_GC))
                    
end = timer()
print("Time Elapsed: " + str(end - start) + " seconds")