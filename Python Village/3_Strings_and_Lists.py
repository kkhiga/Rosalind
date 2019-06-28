with open('rosalind_ini3.txt') as dataset:
    s = dataset.readline()
    splice_ints = dataset.readline()
    
    line_parsed = splice_ints.split(' ')
    a = int(line_parsed[0])
    b = int(line_parsed[1])
    c = int(line_parsed[2])
    d = int(line_parsed[3])
    
    string_splice = s[a:b+1] + ' ' + s[c:d+1]
    print(string_splice)