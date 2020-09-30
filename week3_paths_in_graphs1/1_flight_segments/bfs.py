#Uses python3

import sys
import queue


def distance(adj, S, t):
    #write your code here
    dist = [-1] * len(adj)
    dist[S] = 0

    Q = queue.Queue()
    Q.put(S)

    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                Q.put(v)

    return dist[t]


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

'''
Input:
4 4
1 2
4 1
2 3
3 1
2 4
Output:
2
There is a unique shortest path between vertices 2 and 4 in this graph: 2 − 1 − 4.

Input:
5 4
5 2
1 3
3 4
1 4
3 5
Output:
-1
There is no path between vertices 3 and 5 in this graph.
'''