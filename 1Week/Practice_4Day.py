# 힙 정렬
def DownHeap(list, left, right):
    temp = list[left]
    
    parent = left
    while parent < (right + 1) // 2:
        cl = parent*2 + 1
        cr = cl + 1
        child = cr if cr <= right and list[cr] > list[cl] else cl
        
        if temp >= list[child]:
            break
        list[parent] = list[child]
        parent = child
    list[parent] = temp
    
list = [6, 3, 4, 7, 1, 9, 8]

for i in range((len(list)-1) // 2, -1, -1):
    DownHeap(list, i, len(list) - 1)
    
for i in range(len(list)-1, 0, -1):
    list[0], list[i] = list[i], list[0]
    DownHeap(list, 0, i-1)
    
print(list)


# # 선형 검색
# def Search(list1, list2):
    
#     for i in range(len(list2)):
#         key = list2[i]
#         for j in range(len(list1)):
#             if list1[j] == key:
#                 print(1)
#                 break
#             if j == len(list1) - 1:
#                 print(0)
            
# a = int(input())
# list1 = list(map(int, input().split()))

# b = int(input())
# list2 = list(map(int, input().split()))
    
# Search(list1, list2)

# # 해시법
# from __future__ import annotations
# from typing import Any, Type
# import hashlib

# class Node:
    
#     def __init__(self, key: Any, value: Any, next: Node) -> None:
#         self.key = key      # Key
#         self.value = value  # Value
#         self.next = next    # Successor Node(뒤쪽 노드 참조)
        
# class ChainedHash:
#     def __init__(self, capacity: int) -> None:
#         self.capacity = capacity
#         self.table = [None] * self.capacity
        
#     def hash_value(self, key: Any) -> int:
#         if isinstance(key, int):
#             return key % self.capacity
#         return (int(hashlib.sha512(str(key).encode()).hexdigest(), 16) % self.capacity)
    
#     def search(self, key: Any) -> Any:
#         hash = self.hash_value(key)
#         p = self.table[hash]
        
#         while p is not None:
#             if p.key == key:
#                 return p.value
#             p = p.next
            
#         return None
    
#     def add(self, key: Any, value: Any) -> bool:
#         hash = self.hash_value(key)
#         p = self.table[hash]
        
#         while p is not None:
#             if p.key == key:
#                 return False
#             p = p.next
            
#         temp = Node(key, value, self.table[hash])
#         self.table[hash] = temp
#         return True
    
#     def remove(self, key: Any) -> bool:
#         hash = self.hash_value(key)
#         p = self.table[hash]
#         pp = None
        
#         while p is not None:
#             if p.key == key:
#                 if pp is None:
#                     self.table[hash] = p.next
#                 else:
#                     pp.next = p.next
#                 return True
            
#             pp = p
#             p = p.next
#         return False
        
#     def dump(self) -> None:
#         for i in range(self.capacity):
#             p = self.table[i]
#             print(i, end='')
#             while p is not None:
#                 print(f'  >> {p.key} ({p.value})', end='')
#                 p = p.next
#             print()

# # ------------------beakjoon 9663(N-Queen)----------------------------
# def IsPossible(x):
#     for i in range(x):
#         if board[x] == board[i] or abs(x - i) == abs(board[x] - board[i]):
#             return False
        
#     return True

# def NQueen(x):
#     global count
#     if x == n:
#         count += 1
#         return
    
#     for i in range(n):
#         board[x] = i
#         if IsPossible(x):
#             NQueen(x + 1)

# n = int(input())
# board = [0] * n
# count = 0
            
# NQueen(0)
# print(count)


# ----------------쪽지 시험(피보나치)----------------------

# # for문
# def Fibonacci(n):
#     if n == 0:
#         return []
#     elif n == 1:
#         return [1]
#     elif n == 2:
#         return [1, 1]
    
#     list = [1, 1]
#     for i in range(2, n):
#         list.append(list[i-1] + list[i-2])
        
#     return list


# n = int(input())

# print(Fibonacci(n))

# # 재귀 함수
# def Fibonacci(a):
#     if a < 2:
#         return a
    
#     return Fibonacci(a - 1) + Fibonacci(a - 2)

# print(Fibonacci(6))

# # ------------------beakjoon 25501(재귀의 귀재)----------------------------

# def recursion(s, l, r):
#     global count
#     count += 1
#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

# count = 0
# n = int(input())
# list = [None] * n

# for i in range(n):
#     list[i] = input()
#     print(f'{isPalindrome(list[i])} {count}')
#     count = 0

# # --------------beakjoon 10828(스택)-----------------
# list = []
# n = int(input())

# for _ in range(n):
#     order = input().split()
    
#     if order[0] == 'top':
#             if len(list) <= 0:
#                 print(-1)
#                 continue
            
#             print(list[len(list)-1])

#     elif order[0] == 'pop':
#         if len(list) <= 0:
#             print(-1)
#             continue
        
#         temp = list[len(list) - 1]
#         list.remove(temp)
#         print(temp)
    
#     elif order[0] == 'size':
#         print(len(list))
    
#     elif order[0] == 'empty':
#         if len(list) <= 0:
#             print(1)
#             continue
#         print(0)
        
#     elif order[0] == 'push':
#         list.append(int(order[1]))

# # ------------------beakjoon 18258(큐2)-------------------
# list = []
# n = int(input())

# for _ in range(n):
#     order = input().split()
    
#     if order[0] == 'top':
#             if len(list) <= 0:
#                 print(-1)
#                 continue
            
#             print(list[len(list)-1])

#     elif order[0] == 'pop':
#         if len(list) <= 0:
#             print(-1)
#             continue
        
#         temp = list[len(list) - 1]
#         list.remove(temp)
#         print(temp)
    
#     elif order[0] == 'size':
#         print(len(list))
    
#     elif order[0] == 'empty':
#         if len(list) <= 0:
#             print(1)
#             continue
#         print(0)
        
#     elif order[0] == 'push':
#         list.append(int(order[1]))