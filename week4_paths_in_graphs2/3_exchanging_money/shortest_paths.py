#Uses python3

import sys
import queue


def shortest_paths(adj, cost, s, dist, reachable, shortest):
    dist[s] = 0
    reachable[s] = 1
    cycle = queue.Queue()
    visited = [False] * len(adj)

    # Run |V| iterations
    for i in range(len(adj)):
        for u in range(len(adj)):
            for (idx, v) in enumerate(adj[u]):
                if distance[u] != 10**19 and dist[v] > dist[u] + cost[u][idx]:
                    dist[v] = dist[u] + cost[u][idx]
                    reachable[v] = 1
                    # if there is change in last iteration:
                    if i == len(adj) - 1:
                        cycle.put(v)

    while not cycle.empty():
        u = cycle.get()
        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if not visited[v]:
                cycle.put(v)


if __name__ == '__main__':
    input = sys.stdin.read()
    # input = "4 5 1 2 100 1 3 100 3 4 -1 4 3 -1 4 2 100 2"
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

'''
Input:
6 7
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1
1
Output:
0
10
-
-
-
*

Input:
5 4
1 2 1
4 1 2
2 3 2
3 1 -5
4
Output:
-
-
-
0
*

Input:
4 5
1 2 100
1 3 100
3 4 -1
4 3 -1
4 2 100
2

Out: 
*
0
*
*
'''
