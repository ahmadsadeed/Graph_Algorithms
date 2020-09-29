#Uses python3

import sys


def dfs(adj, visited, order, x):
    visited[x] = 1

    for i in adj[x]:
        if not visited[i]:
            dfs(adj, visited, order, i)

    order.append(x)
    return


def toposort(adj):
    visited = [0] * len(adj)
    order = []

    for i in range(len(adj)):
        if not visited[i]:
            dfs(adj, visited, order, i)

    order.reverse()
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

'''
Input:
4 3
1 2
4 1
3 1
Output:
4 3 1 2


Input:
5 7
2 1
3 2
3 1
4 3
4 1
5 2
5 3
Output:
5 4 3 2 1
'''
