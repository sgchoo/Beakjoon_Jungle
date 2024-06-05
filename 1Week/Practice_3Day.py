# # --------------beakjoon 2309(일곱 난쟁이)--------------------
# list = [None] * 9
# amount = 0
# exception = 0
# findCheck = True

# for i in range(9):
#     list[i] = int(input())
#     amount += list[i]

# targetValue = amount - 100
# n = len(list)

# while findCheck:
#     for j in range(n):
#         if j == exception:
#             continue
        
#         if list[exception] + list[j] == targetValue:
#             a, b = list[exception],list[j]
#             list.remove(a)
#             list.remove(b)
#             findCheck = False
#             break
        
#     if exception < n:
#         exception += 1
       
# list.sort()
     
# for i in range(len(list)):
#     print(list[i])

# # --------------beakjoon 1920(수 찾기)--------------------

# def BinarySearch(list, targetKey):
#     pl = 0
#     pr = len(list) - 1
    
#     while True:
#         center = (pl + pr)//2
#         if targetKey == list[center]:
#             return 1
#         elif targetKey > list[center]:
#             pl = center + 1
#         else:
#             pr = center - 1
            
#         if pl > pr:
#             break
#     return 0

# a = int(input())
# findList = list(map(int, input().split()))
# findList.sort()
# b = int(input())
# targetList = list(map(int, input().split()))

# for i in range(len(targetList)):
#     print(BinarySearch(findList, targetList[i]))

# # -------------beakjoon 2630(색종이 만들기)---------------

# def Divide(X, Y, count):
#     color = square[X][Y]
    
#     for i in range(X, X+count):
#         for j in range(Y, Y+count):
#             if color != square[i][j]:
#                 Divide(X, Y, count//2)
#                 Divide(X, Y+count//2, count//2)
#                 Divide(X+count//2, Y, count//2)
#                 Divide(X+count//2, Y+count//2, count//2)
#                 return
            
#     if color == 0:
#         result.append(0)
#     else:
#         result.append(1)

# a = int(input())
# square = [list(map(int, input().split())) for _ in range(a)]

# result = []

# Divide(0, 0, a)

# print(result.count(0))
# print(result.count(1))
