#Uses python3

import sys


def explore(adj, x, visited):
    for u in adj[x]:
        if not visited[u]:
            visited[u] = True
            explore(adj, u, visited)
    return


def acyclic(adj):
    for u in range(len(adj)):
        visited = [False] * len(adj)
        explore(adj, u, visited)
        if visited[u]:
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

'''
Input:
4 4
1 2
4 1
2 3
3 1
Output:
1
This graph contains a cycle: 3 → 1 → 2 → 3.

Input:
5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5
Output:
0

'''