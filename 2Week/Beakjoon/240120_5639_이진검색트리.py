import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

list = []

while True:
    try:
        x = int(input())
        list.append(x)
    except:
        break

def PostorderTraversal(preorderList):
    if len(preorderList) <= 0:
        return
    
    subL, subR = [], []
    topRoot = preorderList[0]
    
    for i in range(1, len(preorderList)):
        if preorderList[i] < topRoot:
            subL.append(preorderList[i])
        else:
            subR.append(preorderList[i])
            
    PostorderTraversal(subL)
    PostorderTraversal(subR)
    print(topRoot)
    
    
PostorderTraversal(list)