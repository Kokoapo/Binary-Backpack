def cvt_int_list(bit, size):                                                # 12n + 5 
    indexes = [False] * size                                                    # 3n + 2

    for i in range(size):                                                       # (2n + 2) + 7n = 9n + 2
        aux = bit & 1                                                               # 2
        if aux == 1:                                                                # 1
            indexes[i] = True                                                       # 2
        bit >>= 1                                                                   # 2

    return indexes                                                              # 1

def brute(values, weights, max_weight):                                     # 13 * 2^n + 19 * 2^n + 6
    size = len(values)                                                          # 1
    exp = 2 ** size                                                             # 2

    final_value = 0                                                             # 1
    bit = 0                                                                     # 1
    while bit < exp:                                                            # 2^n + (12 * 2^n) + (19n * 2^n) = 13 * 2^n + 19 * 2^n
        indexes = cvt_int_list(bit, size)                                           # 12n + 5 

        current_value = 0                                                           # 1
        current_weight = 0                                                          # 1
        for value, weight, index in zip(values, weights, indexes):                  # (2n + 2) + 5n = 7n + 2
            if index:                                                                   # 1
                current_value += value                                                  # 2
                current_weight += weight                                                # 2
        
        if final_value < current_value and current_weight <= max_weight:            # 2
            final_indexes = indexes                                                 # 1

        bit += 1                                                                    # 2
    
    return final_indexes                                                        # 1