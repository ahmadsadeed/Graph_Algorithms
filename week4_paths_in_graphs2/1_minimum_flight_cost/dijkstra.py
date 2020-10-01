# Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    dist[s] = 0

    Q = queue.PriorityQueue()
    Q.put(s)

    while not Q.empty():
        # ExtractMin
        u = Q.get()
        for (idx, v) in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][idx]:
                dist[v] = dist[u] + cost[u][idx]
                Q.put(v)

    return dist[t] if dist[t] != float('inf') else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

'''
Input:
4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3
one line: 4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3
Output:
3
There is a unique shortest path from vertex 1 to vertex 3 in this 
graph (1 → 2 → 3), and it has weight 3.

Input:
5 9
1 2 4
1 3 2
2 3 2
3 2 1
2 4 2
3 5 4
5 4 1
2 5 3
3 4 4
1 5
one line: 5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5

Output:
6
There are two paths from 1 to 5 of total weight 6: 1 → 3 → 5 and 1 → 3 → 2 → 5.

Input:
3 3
1 2 7
1 3 5
2 3 2
3 2
One-line: 3 3 1 2 7 1 3 5 2 3 2 3 2
Output:
-1

'''
