#%%
%reset
from timeit import default_timer as timer
start = timer()

with open('rosalind_fib.txt') as dataset:
    dataset = dataset.readline().strip().split(' ')
    months = int(dataset[0])
    liter_size = int(dataset[1])
    i = 1
    births_each_month = [1]

    while i < months:
        mature_rabbits = sum(births_each_month[0:i-1])
        births = mature_rabbits * liter_size
        births_each_month.append(births)
        i += 1

    total_rabbits = sum(births_each_month)

    with open('rosalind_fib_out.txt', 'w') as output:
        output.write(str(total_rabbits))
        
end = timer()
print("Time Elapsed: " + str(end - start) + " seconds")
