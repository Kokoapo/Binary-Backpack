from greedy import greedy
from brute import brute
import matplotlib.pyplot as plt
import os, time

DIR_NAME = 'Mochilas'
MAX_BRUTE_SIZE = 5000

def sort_files_per_sizes(sizes):
    sizes.sort()
    files = []    
    for size in sizes:
        files.append(f'Mochila{size}.txt')
    return files

def get_sizes_per_files(files):
    sizes = []
    for file in files:
        file_size = file.replace('Mochila', '').replace('.txt', '')
        sizes.append(int(file_size))
    return sizes

def read_single_file(filename):
    path = os.path.join(DIR_NAME, filename)
    with open(path, 'r') as f:
        data = f.read()

    splits = data.split('\n')
    max_weight = int(splits[0])
    
    values = []
    for value in splits[1].split('\t'):
        if len(value) > 0:
            values.append(int(value))
    
    weights = []
    for weight in splits[2].split('\t'):
        if len(weight) > 0:
            weights.append(int(weight))

    return max_weight, values, weights

def save_backup_file(greedies_time, brutes_time):
    with open('backup.txt', 'w') as f:
        for g_time, b_time in zip(greedies_time, brutes_time):
            line = f'{g_time}\t{b_time}\n'
            f.write(line)

if __name__ == '__main__':
    greedies_time, brutes_time = [], []

    files = os.listdir(DIR_NAME)
    sizes = get_sizes_per_files(files)
    files = sort_files_per_sizes(sizes)

    for file, size in zip(files, sizes):
        max_weight, values, weights = read_single_file(file)
        
        s_time = time.time()
        g_indexes = greedy(values, weights, max_weight)
        g_time = time.time() - s_time

        b_time = None
        if (size <= MAX_BRUTE_SIZE):   
            s_time = time.time()
            b_indexes = brute(values, weights, max_weight)
            b_time = time.time() - s_time

        greedies_time.append(g_time)
        brutes_time.append(b_time)

        print(f'Size {len(values)} Completed    Greedy Time: {g_time}   Brute Time: {b_time}')

    save_backup_file(greedies_time, brutes_time)
    