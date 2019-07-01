#%%
# from timeit import default_timer as timer
# start = timer()

%reset
# Parse the two input DNA strings
s = t = ''
with open('rosalind_subs.txt') as dataset:
    dataset = dataset.read().splitlines()
    s = dataset[0]
    t = dataset[1]
    print(t)
t_index = 0
t_locations = []
while t_index >= 0:
    print(s[t_index:])
    t_index = s[t_index:].find(t)
    print(t_index)
    t_locations.append(t_index)
    t_index += 1

# end = timer()
# print("Time Elapsed: " + str(end - start) + " seconds")


#%%
