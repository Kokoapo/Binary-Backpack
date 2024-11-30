from greedy import greedy
from brute import brute
import matplotlib.pyplot as plt
import os, time
run_what = "g"
DIR_NAME = 'Mochilas'
MAX_BRUTE_SIZE = 5000

def validate_data(values, weights):
    filtered = [(v, w) for v, w in zip(values, weights) if v > 0 and w > 0]
    return [v for v, w in filtered], [w for v, w in filtered]
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
    values, weights = validate_data(values, weights)
    return max_weight, values, weights

def save_backup_file(name, sizes, durations):
    with open(name+'.txt', 'w') as f:
        for size, duration in zip(sizes, durations):
            line = f'{size}\t{duration}\n'
            f.write(line)

def run_greedy(max_weight, values, weights):
    duration = None
    s_time = time.time()
    greedy(values, weights, max_weight)
    duration = time.time() - s_time
    print(f"Greedy: size={len(weights)}, runtime={duration}")
    return len(weights), duration
def run_brute(max_weight, values, weights):
    duration = None
    s_time = time.time()
    brute(values, weights, max_weight)
    duration = time.time() - s_time
    if(duration>900):
        global MAX_BRUTE_SIZE
        MAX_BRUTE_SIZE=len(weights)
    print(f"Brute: size={len(weights)}, runtime={duration}")
    return len(weights), duration
if __name__ == '__main__':
    real_sizes, durations = [], []

    files = os.listdir(DIR_NAME)
    sizes = get_sizes_per_files(files)
    files = sort_files_per_sizes(sizes)

    for file, size in zip(files, sizes):
        max_weight, values, weights = read_single_file(file)
        if run_what=="g":
            size, duration = run_greedy(max_weight, values, weights)
            real_sizes.append(size)
            durations.append(duration)
        if run_what=="b":
            if (len(weights) <= MAX_BRUTE_SIZE):
                size, duration=run_brute(max_weight, values, weights)
                real_sizes.append(size)
                durations.append(duration)
    save_backup_file("greedy" if run_what=="g" else "brute" if run_what=="b" else "?", real_sizes, durations)