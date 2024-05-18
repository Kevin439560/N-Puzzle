# N-Puzzle Solver

Este é um solucionador de N-Puzzle que utiliza diversos algoritmos de busca para resolver o quebra-cabeça. Os algoritmos implementados são:

- Busca em Largura (BFS)
- Busca em Profundidade Iterativa (IDS)
- A* com Heurística de Peças Erradas
- A* com Heurística de Manhattan

## Índice

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Uso](#uso)
- [Algoritmos Implementados](#algoritmos-implementados)
  - [Busca em Largura (BFS)](#busca-em-largura-bfs)
  - [Busca em Profundidade Iterativa (IDS)](#busca-em-profundidade-iterativa-ids)
  - [A* com Heurística de Peças Erradas](#a-com-heurística-de-peças-erradas)
  - [A* com Heurística de Manhattan](#a-com-heurística-de-manhattan)
- [Contribuições](#contribuições)
- [Feito por](#feito-por)

## Introdução

O N-Puzzle é um quebra-cabeça deslizante que consiste em um quadro de peças numeradas em ordem aleatória com uma peça faltando. O objetivo do jogo é mover as peças para restaurar a ordem correta. Este programa resolve o N-Puzzle utilizando diferentes algoritmos de busca.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/Kevin439560/N-Puzzle.git
    cd N-Puzzle
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Para iniciar o programa, execute:
    ```bash
    python3 main.py #No Windows: python main.py
    ```
2. Escolha o algoritmo de busca:
    (1): Busca em largura
    (2): Busca em profundidade iterativa
    (3): Busca A* com heurística de quantidade de peças erradas
    (4): Busca A* com heurística de distância de Manhattan

3. Escolha o tamanho do quebra-cabeça (N), onde o tamanho do tabuleiro será sqrt(N+1)Xsqrt(N+1).
    -------------------------------------------------------------------
    Escolha um algoritmo: 

4. O programa irá resolver o quebra-cabeça e exibir o caminho até a solução.

## Algoritmos Implementados

### Busca em Largura (BFS)

A Busca em Largura explora todos os nós em um nível antes de passar para o próximo nível. Este algoritmo é completo e encontra a solução mínima, mas pode ser lento para quebra-cabeças grandes.

### Busca em Profundidade Iterativa (IDS)

A Busca em Profundidade Iterativa combina a busca em profundidade e a busca em largura. Ela realiza buscas em profundidade limitadas e incrementa a profundidade limite a cada iteração.

### A* com Heurística de Peças Erradas

O algoritmo A* utiliza uma função heurística para guiar a busca. A heurística de peças erradas conta o número de peças fora de lugar.

### A* com Heurística de Manhattan

A heurística de Manhattan soma as distâncias de cada peça desde sua posição atual até sua posição final, considerando apenas movimentos horizontais e verticais.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Feito por

Áquilas Rodrigues Jucá: GitHub(https://github.com/aquilasjuca)

Kevin de Freitas Sales: GitHub(https://github.com/Kevin439560)

Thomas Henrique Carvalho Pinheiro: GitHub(https://github.com/Thomashq)
