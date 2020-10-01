#Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [-1] * len(adj)
    dist[0] = 0

    # Run |V| iterations of Bellman–Ford algorithm
    for i in range(len(adj)):
        for u in range(len(adj)):
            for (idx, v) in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][idx]:
                    dist[v] = dist[u] + cost[u][idx]
                    # if there is change in last iteration:
                    if i == len(adj) - 1:
                        return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
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
    print(negative_cycle(adj, cost))

'''
Input:
4 4 1 2 -5 4 1 2 2 3 2 3 1 1
Output:
1
The weight of the cycle 1 → 2 → 3 is equal to −2, that is, negative

Input:
6 7
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1

Out: 
1
'''