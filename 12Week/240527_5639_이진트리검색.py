import sys
input = sys.stdin.readline

nodes = []
tree = {}

while True:
    try:
        num = int(input())
        nodes.append(num)
        tree[num] = [0, 0]
    except:
        break

def MakeTree(list: list):
    for i in range(1, len(list)):
        root = list[0]
        while True:
            if list[i] > root and tree[root][1] == 0:
                tree[root][1] = list[i]
                break
            elif list[i] < root and tree[root][0] == 0:
                tree[root][0] = list[i]
                break
            elif list[i] > root and tree[root][1] != 0:
                root = tree[root][1]
            elif list[i] < root and tree[root][0] != 0:
                root = tree[root][0]
                
def PostOrder(root: int):
    if root != 0:
        PostOrder(tree[root][0])
        PostOrder(tree[root][1])
        print(root)
        
MakeTree(nodes)
PostOrder(nodes[0])
