import sys
input = sys.stdin.readline

# solution

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = (left, right)
  
def PreorderTraversal(root):
    if root != '.':
        print(root, end='')
        PreorderTraversal(tree[root][0])
        PreorderTraversal(tree[root][1])
    
def InorderTraversal(root):
    if root != '.':
        InorderTraversal(tree[root][0])
        print(root, end='')
        InorderTraversal(tree[root][1])
    
def PostOrderTraversal(root):
    if root != '.':
        PostOrderTraversal(tree[root][0])
        PostOrderTraversal(tree[root][1])
        print(root, end='')
    
PreorderTraversal('A')
print()
InorderTraversal('A')
print()
PostOrderTraversal('A')


# -----------------------------------------------------------------

# 시간 초과

# n = int(input())
# list = [list(map(str, input().split())) for _ in range(n)]
# que = deque()

# def Preorder_Traversal(input):
#     for i in range(n):
#         for j in range(len(list[i])):
#             if que.__contains__(input[i][j]) or input[i][j] == '.':
#                 continue
#             que.append(input[i][j])
     
# Preorder_Traversal(list)     
# print(que)