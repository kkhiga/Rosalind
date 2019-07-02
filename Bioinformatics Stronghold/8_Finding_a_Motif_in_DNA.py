#%%
%reset
from timeit import default_timer as timer
start = timer()

# Parse the two input DNA strings
s = t = ''
with open('rosalind_subs.txt') as dataset:
    dataset = dataset.read().splitlines()
    s = dataset[0]
    t = dataset[1]
t_index = 0
new_index = 0
t_locations = []

while new_index >= 0:
    print('substring: ', s[t_index:])
    new_index = s[t_index:].find(t) 
    t_index += new_index + 1
    print('new_index: ', new_index)
    if new_index >= 0:
        t_locations.append(str(t_index))
    print('t_index: ', t_index)

with open('rosalind_subs_out.txt', 'w') as output:
    output.write(' '.join(t_locations))

end = timer()
print("Time Elapsed: " + str(end - start) + " seconds")
#%%
