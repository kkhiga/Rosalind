with open('rosalind_ini4.txt') as dataset:
    ints = dataset.readline().split(' ')
    a = int(ints[0])
    b = int(ints[1])
    sum = 0
    while a <= b:
        if a % 2 == 1:
            sum += a
        a += 1
    print(sum)