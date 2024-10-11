#include "stdio.h"
#include "./greedy.c"

int main(int argc, char const *argv[]) {
    int values[] = {3, 42, 5, 48, 42, 13, 3, 20, 12, 37};
    int weights[] = {2, 35, 13, 29, 9, 25, 2, 14, 4, 17};
    int size = 10;
    int max_weight = 105;

    int * indexes = greedy(values, weights, size, max_weight);

    int total_value = 0;
    int total_weight = 0;
    printf("Selected Elements:\nIndex\tValue\tWeight\n");
    for (int i = 0; i < size; i++) {
        if (indexes[i]) {
            total_value += values[i];
            total_weight += weights[i];
            printf("%d\t%d\t%d\n", i, values[i], weights[i]);
        } 
    }
    printf("Total Value = %d\n", total_value);
    printf("Total Weight = %d\n", total_weight);

    free(indexes);
    return 0;
}
