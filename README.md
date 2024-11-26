# Binary-Backpack

## Grupo 
- Caio Hideki Gomes Shimohiro
- Gustavo Alberto Ohse Hanke
- Vinicius Visconsini Diniz

## Objetivo

Aplicar e corroborar conceitos adquiridos sobre tecnicas de projeto do grupo Estratégia Gulosa. Para tanto, deverao ser implementadas duas soluções para o problema da mochila.

Na primeira solução, que chamaremos de “BinGreedy”, os itens presentes no conjunto de entrada nao podem ser fracionados, ou seja, trata-se da Mochila Binária. Além disso, os itens não podem ser pré ordenados. Para esta solução será empregado o algoritmo guloso visto em sala.

Já para a segunda solução, “FB”, deverá ser implementada uma abordagem do tipo Força Bruta. Nela todas as possíveis combinações de itens devem ser testadas para descobrir qual delas trará o maior benefício.

## Criterios de avaliação

Para realizar a comparação dos métodos deverão ser feitas duas análises:

1. Na primeira, teórica, deverão ser obtidos os polinômios de custo assintótico das duas soluções; 

2. Na segunda avaliação, prática, deverão ser comparados os tempos cronológicos de execução das soluções;

3. Para a avaliação prática, será necessária a execução de 6 repetições para cada estrategia. Das 6 execuções a primeira será descartada. A ideia é que o comparativo seja feito a partir do tempo medio das 5 execuções restantes. Assim, o gráfico de comparação Tamanho vs Tempo apresentará os valores médios das duas soluções implementadas.

## Como

- A linguagem utilizada no desenvolvimento é de vossa escolha, desde seja uma das seguintes linguagens: C, C++, Python ou Java. Contudo, a mesma linguagem deve ser adotada para ambos os métodos. Além disso, deve-se empregar as mesmas estratégias para a realização do trabalho. Por exemplo, empregar soluções recursivas para todos ou para nenhum deles;
- A forma com que os métodos serão implementados é determinada pelo grupo;
- A entrada dos dados deve ser feita com base nos arquivos texto disponíveis na pasta Mochilas;