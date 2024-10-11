#include "stdlib.h"

int * greedy(int * values, int * weights, int size, int max_weight) {
    int * indexes = (int *) malloc(size * sizeof(int));
    for (int i = 0; i < size; i++)
        indexes[i] = 0;

    int weight = 0;
    while (1) {
        int max_i = -1;
        int max_v = -1;
        
        for(int i = 0; i < size; i++) {
            if (!indexes[i]) {
                if (values[i] >= max_v && (weights[i] + weight) <= max_weight) {
                    max_i = i;
                    max_v = values[i];
                }
            }
        }

        if (max_i == -1)
            break;
        indexes[max_i] = 1;
        weight += weights[max_i];
    }

    return indexes;
}