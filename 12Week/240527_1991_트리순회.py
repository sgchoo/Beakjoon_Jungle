import sys
input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def PreorderTraversal(rootNode: str):
    if rootNode != '.':
        print(rootNode, end='')
        PreorderTraversal(tree[rootNode][0])
        PreorderTraversal(tree[rootNode][1])

def InorderTraversal(rootNode: str):
    if rootNode != '.':
        InorderTraversal(tree[rootNode][0])
        print(rootNode, end='')
        InorderTraversal(tree[rootNode][1])

def PostorderTraversal(rootNode: str):
    if rootNode != '.':
        PostorderTraversal(tree[rootNode][0])
        PostorderTraversal(tree[rootNode][1])
        print(rootNode, end='')

PreorderTraversal('A')
print(' ')
InorderTraversal('A')
print(' ')
PostorderTraversal('A')