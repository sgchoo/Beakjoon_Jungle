# # -----------beakjoon 11866(요세푸스 문제0)-----------------
# from typing import Any
# import sys
# input=sys.stdin.readline

# class Queue:

#     def __init__(self, capacity: int) -> None:
#        self.no = 0
#        self.front = 0
#        self.rear = 0
#        self.capacity = capacity
#        self.que = [None] * self.capacity
       
#     def __len__(self) -> int:
#         return self.no
    
#     def enque(self, number) -> None:
#         self.que[self.rear] = number
#         self.no += 1
#         self.rear += 1
#         if self.rear == self.capacity:
#             self.rear = 0
            
#     def deque(self) -> Any:
#         value = self.que[self.front]
#         self.no -= 1
#         self.front += 1
        
#         if self.front == self.capacity:
#             self.front = 0
#         return value
#     def is_empty(self) -> bool:
#         return self.no <= 0
        
# n, k = map(int, input().split())
# que = Queue(n)
# result = []

# for i in range(1, n+1):
#     que.enque(i)
    
# while que:
#     temp = 0
#     for i in range(k):
#         temp = que.deque()
#         if i < k-1:
#             que.enque(temp)
#     result.append(temp)

# print('<', end='')
# for i in range(len(result)-1):
#     print(f'{result[i]}, ', end='')
# print(f'{result[len(result)-1]}>')

# # --------------beakjoon 11279(최대 힙)-----------------
# import heapq
# import sys
# input=sys.stdin.readline

# heap = []

# n = int(input())
# for _ in range(n):
#     order = int(input())
    
#     if order <= 0:
#         if len(heap) <= 0:
#             print(0)
#         else:
#             print(heapq.heappop(heap)[1])
        
#     else:
#         heapq.heappush(heap, (-order, order))
#         continue


# # ----------------beakjoon 18258(큐 2)---------------------
# class Queue:
#     def __init__(self, capacity: int) -> None:
#         self.no = 0
#         self.front = 0
#         self.rear = 0
#         self.capacity = capacity
#         self.que = [None] * self.capacity
        
#     def __len__(self) -> int:
#         return self.no
    
#     def empty(self) -> int:
#         if self.no <= 0:
#             return 1
#         else:
#             return 0
        
#     def enque(self, number) -> None:
#         self.que[self.rear] = number
#         self.rear += 1
#         self.no += 1
#         if self.rear == self.capacity:
#             self.rear = 0
            
#     def deque(self) -> int:
#         if self.no <= 0:
#             return -1
        
#         value = self.que[self.front]
#         self.no -= 1
#         self.front += 1
#         if self.front == self.capacity:
#             self.front = 0
#         return value
    
# import sys
# input=sys.stdin.readline

# n = int(input())
# que = Queue(n)

# for _ in range(n):
#     order = input().split()
    
#     if order[0] == 'push':
#         que.enque(int(order[1]))
        
#     elif order[0] == 'pop':
#         print(que.deque())
    
#     elif order[0] == 'size':
#         print(que.no)
    
#     elif order[0] == 'empty':
#         print(que.empty())
        
#     elif order[0] == 'front':
#         if que.no <= 0:
#             print(-1)
#             continue
#         print(que.que[que.front])
        
#     elif order[0] == 'back':
#         if que.no <= 0:
#             print(-1)
#             continue
#         print(que.que[que.rear-1])

# # --------------beakjoon 10971(외판원 순회2)---------------
# import sys
# input = sys.stdin.readline

# def GetCost(start, cost, count):
#     global result
    
#     if count == n-1 and cityList[start][0] != 0:
#         result = min(result, cost+cityList[start][0])
#         return
    
#     for i in range(n):
#         if visited[i] == False and cityList[start][i] != 0:
#             visited[i] = True
#             GetCost(i, cost+cityList[start][i], count+1)
#             visited[i] = False
    
    
    
# n = int(input())
# cityList = [list(map(int, input().split())) for _ in range(n)]

# visited = [False] * n
# visited[0] = True
# result = int(1e9)

# GetCost(0, 0, 0)
# print(result)

# # ---------------beakjoon 2805(나무 자르기)------------------------
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# trees = list(map(int, input().split()))

# left, right = 0, max(trees)

# while left <= right:
#     mid = (left + right) // 2
#     total = 0

#     for tree in trees:
#         if tree >= mid:
#             total += tree - mid

#     if total >= M:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(right)

# # ----------------beakjoon 1629(곱셈)-----------------
# import sys
# input = sys.stdin.readline

# def Mult(list, start, end):
#     middle = (start + end) // 2
#     global c
#     if middle == start:
#         return ((list[start])*(list[end])) % c
#     elif start == end:
#         return list[start]
#     else:
#         return ((Mult(list, start, middle))*(Mult(list, middle+1, end))) % c
        
# a, b, c = map(int, input().split())

# tempList = [a] * b

# print(Mult(tempList, 0, len(tempList)-1))

# import sys
# input = sys.stdin.readline

# a, b, c = map(int, input().split())

# def Mult(num, e):
#     if e == 1:
#         return num % c
    
#     else:
#         func = Mult(num, e//2)
#         if e % 2 == 0:
#             return (func * func) % c
#         else:
#             return (func * func * a) % c

# print(Mult(a, b))

# # ----------------- beakjoon 2493(탑)------------------
# import sys
# input = sys.stdin.readline

# a = int(input())

# list = list(map(int, input().split()))
# result = [0] * a
# tempList = [(0, list[0])]

# for i in range(1, len(list)):
#     for j in range(len(tempList)-1, -1, -1):
#         if tempList[j][1] < list[i]:
#             tempList.pop()
#         else:
#             result[i] += tempList[j][0]+1
#             tempList.append((i, list[i]))
#             break
#     if len(tempList) <= 0:
#         tempList.append((i, list[i]))
        
# print(" ".join(map(str, result)))

# # ---------------beakjoon 1655(가운데를 말해요)-----------------
# import heapq
# import sys
# input = sys.stdin.readline
# n = int(input())
# lList = []
# rList = []
# temp = []

# for i in range(n):
#     value = int(input())
#     if len(lList) == len(rList):
#         heapq.heappush(lList, -value)
#     else:
#         heapq.heappush(rList, value)
        
#     if rList and rList[0] < -lList[0]:
#         lValue = heapq.heappop(lList)
#         rValue = heapq.heappop(rList)
#         heapq.heappush(lList, -rValue)
#         heapq.heappush(rList, -lValue)
#     print(-lList[0])

# # ------------------------------------------------------
# import sys 
# input = sys.stdin.readline

# originNum = int(input())
# if originNum < 10:
#     originNum *= 10
    
# first = originNum//10
# last = originNum%10
# targetNum = (last * 10) + ((first+last)%10)    

# count = 1
# while targetNum != originNum:
#     if targetNum <= 0:
#         print(count)
#         break
    
#     num10 = targetNum // 10
#     num1 = targetNum % 10
#     targetNum = (num1 * 10) + ((num10 + num1)%10)
#     count +=1
    
# print(count)

# def Sum(list, start1, start2, curValue):
#     global count
#     value = curValue
    
#     if value < minNum or value > maxNum:
#         return
#     if value == K:
#         count += 1
#         return
    
#     for i in range(start1, len(list)):
#         for j in range(start2, len(list)):
#             # if i == j:
#             #     continue
#             Sum(i, j, value + list[j])
            
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# list = list(map(int, input().split()))
# minNum = min(list)
# maxNum = max(list)
# list = []
# count = 0

# Sum(0, 0, 0)
# print(count)

# ---------------------동민님 코드-------------------
# import sys
# input = sys.stdin.readline

# N, S = list(map(int, input().split()))

# arr = list(map(int, input().split()))

# ans = 0
# def sol(n, total):
# 	global N
# 	global S
# 	global ans
# 	if n == N:
# 		print(total)
# 		if total == S:
# 			ans += 1
# 		return
# 	sol(n + 1, total + arr[n])
# 	sol(n + 1, total)

# sol(0, 0)
# if S == 0:
# 	ans -= 1

# print(ans)

# -------------------------------------
import sys
input = sys.stdin.readline

n = int(input())

arr = [list(input()) for _ in range(n)]

ans = []

def compare(n, x, y):
	for i in range(n):
		for j in range(n):
			if arr[i + y][j + x] != arr[y][x]:
				return 0
	return 1

def sol(n, x, y):
	if compare(n, x, y):
		ans.append(arr[y][x])
	else:
		n //= 2
		ans.append('(')
		sol(n, x, y)
		sol(n, x + n, y)
		sol(n, x, y + n)
		sol(n, x + n, y + n)
		ans.append(')')

sol(n, 0, 0)

print("".join(ans))