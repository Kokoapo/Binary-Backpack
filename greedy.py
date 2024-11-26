def greedy(values, weights, max_weight):                                            # 12n^2 + 15n + 4
    size = len(values)
    indexes = [False] * size                                                            # 3n + 2
    
    total_weight = 0                                                                    # 1
    while True:                                                                         # n + 12n^2 + 11n = 12n^2 + 12n
        max_i = -1                                                                          # 1
        max_v = -1                                                                          # 1

        for i in range(size):                                                               # (2n + 2) + 10n = 12n + 2 
            if not indexes[i]:                                                                  # 2
                if values[i] >= max_v and (weights[i] + total_weight) <= max_weight:            # 5
                    max_i = i                                                                   # 1
                    max_v = values[i]                                                           # 2
        
        if max_i == -1:                                                                     # 1
            break                                                                           # 1
        indexes[max_i] = True                                                               # 2
        total_weight += weights[max_i]                                                      # 3
    
    return indexes                                                                      # 1
