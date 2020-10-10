#Uses python3
import sys
import math


# length of a segment with endpoints (𝑥1, 𝑦1) and (𝑥2, 𝑦2)
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def clustering(x, y, k):
    result = 0.

    # calculate distances between edges and sort based on distance (weight)
    edges = []
    for u in range(len(x)):
        for v in range(len(x)):
            if u != v:
                dist = distance(x[u], y[u], x[v], y[v])
                edges.append([u, v, dist])

    edges = sorted(edges, key=lambda edge: edge[2])

    # use disjoint sets data structure
    # initially, each vertex lies in a separate set
    # X = []
    union = range(n)

    for edge in edges:
        # if Find(u)  != Find(v), if sets are not joined
        if union[edge[0]] != union[edge[1]]:
            # break after k sets to return weight of the last edge
            if len(set(union)) == k:
                result = edge
                break
            # Union(u, v)
            union = [union[edge[0]] if i == union[edge[1]] else i for i in union]
    return result[2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

'''
Input:
12
7 6
4 3
5 1
1 7
2 7
5 7
3 3
7 8
2 8
4 4
6 7
2 6
3
Output:
2.828427124746

Input:
8
3 1
1 2
4 6
9 8
9 9
8 9
3 11
4 12
4
Output:
5.000000000
'''