#%%
with open('rosalind_iprb.txt') as dataset:
    dataset = dataset.readline().strip().split(' ')
    # Homozygous Dominant (AA)
    k = int(dataset[0])
    # Heterozygous (Aa)
    m = int(dataset[1])
    # Homozygous Recessive (aa)
    n = int(dataset[2])

    num_organisms = k + m + n

    # Calculate first pick
    # prob_K = k/num_organisms <- irrelevant
    prob_M = m/num_organisms
    prob_N = n/num_organisms

    # Calculate second picks
    prob_MM = prob_M * (m - 1)/(num_organisms - 1)
    prob_MN = prob_M * n/(num_organisms - 1)
    prob_NM = prob_N * m/(num_organisms - 1)
    prob_NN = prob_N * (n - 1)/(num_organisms - 1)

    # Calculate probablity of recessive phenotype for each combo
    prob_MM_rec = prob_MM * (1/4)
    prob_MN_rec = (prob_MN + prob_NM) * (1/2)

    # Calculate overall probability of recessive phenotype
    prob_rec = prob_NN + prob_MM_rec + prob_MN_rec
    # Inverse is the probability of dominant phenotype
    prob_dom = 1 - prob_rec

    with open('rosalind_irpb_out.txt', 'w') as output: 
        output.write(str(prob_dom))
