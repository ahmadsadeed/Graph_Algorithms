#Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs(adj, visited, stack, x):
    visited[x] = 1

    for i in adj[x]:
        if not visited[i]:
            dfs(adj, visited, stack, i)

    # track post-order of visited vertices
    stack.append(x)


def reverse_G(adj):
    # reverse the graph
    rev_adj = [[] for _ in range(len(adj))]

    for u in range(len(adj)):
        for v in adj[u]:
            rev_adj[v].append(u)
    return rev_adj


def number_of_strongly_connected_components(adj):
    visited = [0] * len(adj)
    result = 0
    # track the post-order
    stack = []

    # populate the stack order
    for i in range(len(adj)):
        if not visited[i]:
            dfs(adj, visited, stack, i)

    rev_adj = reverse_G(adj)
    visited = [0] * len(adj)

    while stack:
        u = stack.pop()
        if not visited[u]:
            dfs(rev_adj, visited, [], u)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))

'''
Input:
4 4
1 2
4 1
2 3
3 1
Output:
2
This graph has two strongly connected components: {1, 3, 2}, {4}.

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
5
This graph has five strongly connected components: {1}, {2}, {3}, {4}, {5}.
'''