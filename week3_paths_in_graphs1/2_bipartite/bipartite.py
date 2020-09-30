#Uses python3

import sys
import queue


def dfs(graph, src, color_list):
    # colors: 1, 0       No color: -1
    color_list[src] = 1
    Q = list()
    Q.append(src)

    while Q:
        u = Q.pop()
        for v in graph[u]:
            if color_list[v] == -1:
                # assign 1 or 0
                color_list[v] = 1 - color_list[u]
                Q.append(v)
            elif color_list[v] == color_list[u]:
                return False
    return True


def bipartite(adj):
    # two colors: 0, 1       No color: -1
    color_list = [-1] * len(adj)

    # loop over all vertices if there are multiple components in the graph
    for src in range(len(adj)):
        if color_list[src] == -1:
            if not dfs(adj, src, color_list):
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))

'''
Input:
4 4
1 2
4 1
2 3
3 1
Output:
0
This graph is not bipartite. To see this assume that the vertex 1 is colored white. Then the vertices 2
and 3 should be colored black since the graph contains the edges {1, 2} and {1, 3}. But then the edge
{2, 3} has both endpoints of the same color.

Input:
5 4
5 2
4 2
3 4
1 4
Output:
1
This graph is bipartite: assign the vertices 4 and 5 the white color, assign all the remaining vertices
the black color.

Input:
8 7
5 2
4 2
3 4
1 4
6 7
8 6
7 8

0
There is two SCC (components). The 6-7-8 is not bipartite.
'''