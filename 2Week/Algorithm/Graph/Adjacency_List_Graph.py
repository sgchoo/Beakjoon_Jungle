import sys
input = sys.stdin.readline

vertex, edge = map(int, input().split())

adj = [ [] for _ in range(vertex)]

for _ in range(edge):
    src, dest = map(int, input().split())
    adj[src].append(dest)
    adj[dest].append(src)