def greedy(values, weights, max_weight):                                            # 19n^2 + 15n + 6
    worth = []                                                                          # 7n + 2
    for v, w in zip(values, weights):
        worth.append(v/w)
    
    size = len(values)                                                                  # 2
    indexes = [False] * size                                                            # 3n + 2
    
    total_weight = 0                                                                    # 1
    while True:                                                                         # n + 12n^2 + 11n = 12n^2 + 12n
        max_i = -1                                                                          # 1
        max_v = -1                                                                          # 1

        for i in range(size):                                                               # (2n + 2) + 10n = 12n + 2 
            if not indexes[i]:                                                                  # 2
                if worth[i] >= max_v and (weights[i] + total_weight) <= max_weight:            # 5
                    max_i = i                                                                   # 1
                    max_v = worth[i]                                                            # 2
        
        if max_i == -1:                                                                     # 1
            break                                                                           # 1
        indexes[max_i] = True                                                               # 2
        total_weight += weights[max_i]                                                      # 3
    
    return indexes                                                                      # 1
