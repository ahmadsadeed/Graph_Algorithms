#Uses python3
import sys
import math


# length of a segment with endpoints (𝑥1, 𝑦1) and (𝑥2, 𝑦2)
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def minimum_distance(x, y):
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
            # add {u, v} to X
            # Union(u, v)
            union = [union[edge[0]] if i == union[edge[1]] else i for i in union]
            result += edge[2]
            # X.append(edge)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

'''
Input:
4
0 0
0 1
1 0
1 1
Output:
3.000000000

Input:
5
0 0
0 2
1 1
3 0
3 2
Output:
7.064495102
'''