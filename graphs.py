import matplotlib.pyplot as plt

brute = {}
greedy = {}

for i in range(1, 7, 1):
    with open(f'brute{i}.txt') as file:
        line = None
        while True:
            line = file.readline()
            if line == '':
                break

            n, r = line.split()
            n = int(n)
            r = float(r)
            if n in brute.keys():
                brute[n] += r
            else:
                brute[n] = r
    with open(f'greedy{i}.txt') as file:
        line = None
        while True:
            line = file.readline()
            if line == '':
                break

            n, r = line.split()
            n = int(n)
            r = float(r)
            if n in greedy.keys():
                greedy[n] += r
            else:
                greedy[n] = r

brute_values = []
brute_keys = []
greedy_values = []
greedy_keys = []

for k in brute.keys():
    brute[k] /= 6
    brute_values.append(brute[k])
    brute_keys.append(k)

for k in greedy.keys():
    greedy[k] /= 6
    greedy_values.append(greedy[k])
    greedy_keys.append(k)

plt.plot(brute_keys, brute_values)
plt.title('Desempenho da Força Bruta')
plt.xlabel('Número de Elementos')
plt.ylabel('Tempo de Execução')
plt.savefig('brutes.png')

plt.cla()

plt.plot(greedy_keys, greedy_values)
plt.title('Desempenho da Estratégia Gulosa')
plt.xlabel('Número de Elementos')
plt.ylabel('Tempo de Execução')
plt.savefig('greedies.png')