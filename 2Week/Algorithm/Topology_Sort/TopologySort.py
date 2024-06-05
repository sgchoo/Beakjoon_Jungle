# Queue를 이용한 위상 정렬
import sys
from collections import deque
input = sys.stdin.readline

v, e = map(int, input().split())        # 정점의 갯수와 간선의 갯수를 입력 받기

inDegree = [0] * (v+1)                  # 모든 정점에 대한 진입 차수는 0으로 초기화
graph = [[] for _ in range(v+1)]        # 각 정점에 연결된 간선 정보를 달기 위한 연결 리스트 초기화

# 방향 그래프의 모든 간선 정보를 입력 받기
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)                  # 정점 A에서 B로 이동 가능
    inDegree[b] += 1                    # 진입 차수를 1 증가
    
# 위상 정렬 함수
def TopologySort():
    result = []                         # 알고리즘 수행 결과를 담을 리스트
    queue = deque()                     # 쿠 기능을 위한 deque 라이브러리 사용
    
    for i in range(1, v+1):             # 첫 시작때 진입 차수가 0인 정점을 큐에 삽입
        if inDegree[i] == 0:        
            queue.append(i)
            
    while queue:                        # 큐가 빌 때까지 반복
        current = queue.popleft()       # 큐에서 원소 꺼내기
        result.append(current)          
        
        for i in graph[current]:        # 해당 원소와 연결된 정점들의 진입 차수 1 빼기
            inDegree[i] -= 1
            if inDegree[i] == 0:        # 새롭게 진입 차수가 0이 되는 정점을 큐에 삽입
                queue.append(i)
                
    for i in result:
        print(i, end='')
            
TopologySort()

# 인접 리스트 형태의 그래프 위상 정렬

import queue

adj_list = {0:[2, 3], 1:[3, 4], 2:[3, 5], 3:[5], 4:[5], 5:[]}

def TopologicalSort(list):
    myQue = queue.Queue()
    inDegree = [0] * len(list)
    answer = []
    
    for i in range(len(list)):
        for j in range(len(list)):
            temp = list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    inDegree[i] += 1
                    
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            myQue.put(i)
            
    while not myQue.empty():
        node = myQue.get()
        answer.append(node)
        
        for i in range(len(list[node])):
            idx = list[node][i]
            inDegree[idx] -= 1
            if inDegree[idx] == 0:
                myQue.put(idx)
                    
    return answer
                    
print(TopologicalSort(adj_list))

# 인접 행렬 형태의 그래프 위상 정렬
from collections import deque

adj_mat = [[0, 0, 1, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0]]

def TopologicalSort(matrix):
    inDegree = []
    que = deque()
    answer = []

    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
        inDegree.append(temp)
        
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            que.append(i)
            
    while que:
        node = que.popleft()
        answer.append(node)
        
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    que.append(i)
    
    return answer

print(TopologicalSort(adj_mat))                    
