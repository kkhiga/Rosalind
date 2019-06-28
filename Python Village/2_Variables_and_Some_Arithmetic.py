#%%
with open('rosalind_ini2.txt') as dataset:
    line = dataset.readline().split(' ')
# a^2 + b^2 = c^2
a = int(line[0])
b = int(line[1])

hypotenuse_squared = (a ** 2 + b ** 2)
print(str(hypotenuse_squared))