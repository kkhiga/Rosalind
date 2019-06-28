with open('rosalind_ini5.txt') as dataset:
    parsed_line = dataset.readline().strip('\n').split(' ')
    word_counts = {}
    for word in parsed_line:
        if str(word) in word_counts:
            word_counts[str(word)] += 1
        else:
            word_counts[str(word)] = 1
    
    for key, value in word_counts.items():
        print(key + ' ' + str(value))