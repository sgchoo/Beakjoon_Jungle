import sys
input = sys.stdin.readline

vertex, edge = map(int, input().split())

adj = [[0 for _ in range(vertex)] for _ in range(vertex)]

for _ in range(edge):
    src, dest = map(int, input().split())
    adj[src][dest] = 1
    adj[dest][src] = 1