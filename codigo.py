from dis import dis
from xmlrpc.client import Boolean, boolean
import numpy as np
import re


## undirected graph ##


def gerar_tabela_dist_dir(G):
    Dims = re.findall("(\d+)\s+(\d+)",  G.readline())
    Grafo = - np.ones((int(Dims[0][0]), int(Dims[0][0])))
    for i in range(len(Grafo)):
        Grafo[i][i] = 0
    distances = re.findall("(\d+)\s+(\d+)\s+(\d+)", G.read())
    for Edges in distances:
        Grafo[int(Edges[0])-1][int(Edges[1])-1] = Edges[2]
        Grafo[int(Edges[1])-1][int(Edges[0])-1] = Edges[2]

    return Grafo

## directed graph ##


def gerar_tabela_dist(G):

    Dims = re.findall("(\d+)\s+(\d+)",  G.readline())
    Grafo = - np.ones((int(Dims[0][0]), int(Dims[0][0])))
    for i in range(len(Grafo)):
        Grafo[i][i] = 0
    distances = re.findall("(\d+)\s+(\d+)\s+(\d+)", G.read())
    for Edges in distances:
        Grafo[int(Edges[0])-1][int(Edges[1])-1] = Edges[2]
    return Grafo


def dijkstra(D, Source):

    distances = np.zeros(D.shape[0])
    for i in range(len(D)):
        distances[i] = 9999
    vis = np.zeros(D.shape[0])

    distances[Source] = 0
    fila = []
    fila.append(Source)
    while len(fila) > 0:
        atual = fila.pop(0)
        if vis[atual] != 1:

            vis[atual] = 1

            for i in range(len(D)):
                v = i
                if D[atual][v] == -1:
                    continue
                cost = D[atual][v]

                if distances[v] > distances[atual] + cost:
                    distances[v] = distances[atual] + cost
                    fila.append(v)
    sum = 0
    for v in distances:
        sum = sum+v
    Greater = 0
    for v in distances:
        if Greater < v:
            Greater = v
    return (sum, Greater)


def central_dist(dists, max_dist_vec):
    central = 0
    Min = np.inf
    for v in range(len(dists)):
        if dists[v] < Min:
            Min = dists[v]
            central = v
        elif dists[v] == Min:
            if max_dist_vec[central] > max_dist_vec[v]:
                Min = dists[v]
                central = v
    return central


def dist_sum_vec(D):
    dist_vec = np.zeros(D.shape[0])
    # Faça o código aqui
    for i in range(len(D)):
        result = dijkstra(D, i)
        dist_vec[i] = result[0]
    #print(result[0])
    return dist_vec


def max_dist_vec(D):
    max_vec = np.zeros(D.shape[0])
  # Faça o código aqui
    for i in range(len(D)):
        result = dijkstra(D, i)
        max_vec[i] = result[1]
    return max_vec

G = open("grafo01.txt", "r")

i = int(input("Choose the graph type:\n1 - Undirected\n2- Directed\n”))

if i == 1:
    D = gerar_tabela_dist_dir(G)
elif i == 2:
    D = gerar_tabela_dist(G)

print(D)

dist_vec = dist_sum_vec(D)
max_vec = max_dist_vec(D)

print(dist_vec)
print(max_vec)

central = central_dist(dist_vec, max_vec)

print("\nGRAPH'S CENTRAL\n:", central)
