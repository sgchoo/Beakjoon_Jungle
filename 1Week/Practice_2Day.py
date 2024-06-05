# # ----------Beakjoon 1914(하노이의 탑)-----------------
# #Solve1(출력 초과)
# def Hanoi(cnt, curPos, targetPos):
#     if cnt > 0:
#         Hanoi(cnt-1, curPos, (6 - curPos - targetPos))
#         print(f'{curPos} {targetPos}')
#         Hanoi(cnt-1, (6-curPos-targetPos), targetPos)
#     else:
#         return
    
# num = int(input())
# print(2**num - 1)
# print(Hanoi(num, 1, 3))

# # Solve2
# def Hanoi(cnt, curPos, targetPos):
#     if cnt > 0:
#         Hanoi(cnt-1, curPos, (6 - curPos - targetPos))
#         print(f'{curPos} {targetPos}')
#         Hanoi(cnt-1, (6-curPos-targetPos), targetPos)
#     else:
#         return
    
# num = int(input())
# print(2**num - 1)
# if num <= 20:
#     Hanoi(num, 1, 3)

# #------------------Beakjoon 2750(수 정렬하기)---------------------
# # OrderBy
# a = int(input())
# list = []
# for _ in range(a):
#     list.append(int(input()))

# for i in range(len(list) - 1):
#     for j in range(len(list) - 1, i, -1):
#         if list[j - 1] > list[j]:
#             list[j - 1], list[j] = list[j], list[j - 1]
            
# for i in range(len(list)):
#     print(list[i])

# # DescendingOrderBy
# a = int(input())
# list = []

# for _ in range(a):
#     list.append(int(input()))
    
# for i in range(len(list)-1):
#     for j in range(len(list)-1, i, -1):
#         if list[j] > list[j-1]:
#             list[j], list[j-1] = list[j-1], list[j]
            
# print(list)

# #improve code1
# a = int(input())
# list = []

# for _ in range(a):
#     list.append(int(input()))


# for i in range(len(list)-1):
#     counting = 0
#     for j in range(len(list)-1, i, -1):
#         if list[j-1] > list[j]:
#             list[j-1], list[j] = list[j], list[j-1]
#             counting += 1
        
#     if counting <= 0:
#         break    

# # improve code2
# a = int(input())
# list = []

# for _ in range(a):
#     list.append(int(input()))

# k = 0

# while k < len(list)-1:
#     last = len(list)-1
#     for i in range(len(list)-1, k, -1):
#         if list[i-1] > list[i]:
#             list[i-1], list[i] = list[i], list[i-1]
#             last = i
#     k = last

# for i in range(len(list)):
#     print(list[i])
    
# ------------------Beakjoon 2750(수 정렬하기2)------------------
# list = [1, 3, 9, 4, 7, 8, 6]

# length = len(list)
# k = 0

# passes = 0
# compare = 0

# while k < length-1:
#     last = length-1
#     passes += 1
#     for i in range(length-1, k, -1):
#         compare += 1
#         if list[i-1]>list[i]:
#             list[i-1], list[i] = list[i], list[i-1]
#             last = i
#     k = last
    
# print(list)
# print(passes)
# print(compare)


# list = [1, 3, 9, 4, 7, 8, 6]
# passes2 = 0
# compare2 = 0
# for i in range(len(list) - 1):
#     passes2 += 1
#     for j in range(len(list) - 1, i, -1):
#         compare2 += 1
#         if list[j - 1] > list[j]:
#             list[j - 1], list[j] = list[j], list[j - 1]
           
# print(list)
# print(passes2)
# print(compare2)

# list = [1, 3, 9, 4, 7, 8, 6]
# passes3 = 0
# compare3 = 0

# for i in range(len(list) - 1):
#     passes3 += 1
#     trade = 0
#     for j in range(len(list) - 1, i, -1):
#         compare3 += 1
#         if list[j - 1] > list[j]:
#             list[j - 1], list[j] = list[j], list[j - 1]
#             trade += 1
#     if trade <= 0:
#         break
    
# print(list)
# print(passes3)
# print(compare3)

# # -------------단순 선택 정렬------------
# list = [6, 4, 8, 3, 1, 9, 7]

# n = len(list)

# for i in range(n-1):
#     min = i
#     for j in range(i+1, n):
#         if list[j] < list[min]:
#             min = j
#     list[i], list[min] = list[min], list[i]
    
# print(list)

# ---------------단순 삽입 정렬--------------
# def insertion_sort(a):
#     n = len(a)
#     for i in range(1, n):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j-1] > tmp:
#             a[j] = a[j-1]
#             j -= 1
#         a[j] = tmp
        
# list = [6, 4, 3, 7, 1, 9, 8]
# insertion_sort(list)
# print(list)

# def binary_insertion_sort(a):
#     n = len(a)
#     for i in range(1, n):
#         key = a[i]
#         pl = 0
#         pr = i-1 
        
#         while True:
#             pc = (pl + pr) // 2
#             if len(a[pc]) == len(key):
#                 break
#             elif len(a[pc]) < len(key):
#                 pl = pc + 1
#             else:
#                 pr = pc - 1
#             if pl > pr:
#                 break
            
#         pd = pc + 1 if pl <= pr else pr + 1
        
#         for j in range(i, pd, -1):
#             a[j] = a[j-1]
#         a[pd] = key

# def sort(a):
#     length = len(a)
#     k = 0
#     while k < length-1:
#         last = length-1
#         for i in range(length-1, k, -1):
#             if a[i-1] > a[i]:
#                 a[i-1], a[i] = a[i], a[i-1]
#                 last = i
#             elif a[i-1] == a[i]:
#                 check = 0
#                 for j in range(len(a[i])):
#                     if ord(a[i-1][j]) > ord(a[i][j]):
#                         a[i - 1], a[i] = a[i], a[i-1]
#                     elif ord(a[i-1][j]) == ord(a[i][j]):
#                         check+=1
#                     if check == len(a[i]):
#                         a.remove(a[i-1])
#         k = last

# string = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

# # binary_insertion_sort(string)
# sort(string)
# print(string)

# # ------------beakjoon 1181(단어 정렬)-------------

# a = int(input())
# list = []
# listSet = set()

# for _ in range(a):
#     array = input()
#     listSet.add(array)
    
# for i in listSet:
#     list.append(i)
    
# list.sort()
# list.sort(key=len)

# print(list)

# def qsort(list, left, right):
#     pl = left
#     pr = right
#     pivot = list[(left + right) // 2]
    
#     print(f'a[{left}] ~ a[{right}]: ', *list[left:right+1])
    
#     while pl <= pr:
#         while list[pl] < pivot: pl += 1
#         while list[pr] > pivot: pr -= 1
#         if pl <= pr:
#             list[pl], list[pr] = list[pr], list[pl]
#             pl += 1
#             pr -= 1
            
#     if left < pr: qsort(list, left, pr)
#     if right > pl: qsort(list, pr, right)
    
# list = [5, 8, 4, 2, 6, 1, 3, 9, 7]
# qsort(list, 0, len(list) - 1)
# print(list)

# 퀵 정렬
# def GetMiddleValue(list, idx1, idx2, idx3):
#     if list[idx1] > list[idx2]: list[idx1], list[idx2] = list[idx2], list[idx1]
#     if list[idx2] > list[idx3]: list[idx2], list[idx3] = list[idx3], list[idx2]
#     if list[idx1] > list[idx2]: list[idx1], list[idx2] = list[idx2], list[idx1]
    
#     return idx2

# def InsertionSort(list):
#     for i in range(1, len(list)):
#         idx = i
#         tempValue = list[i]
        
#         while idx > 0 and list[idx - 1] > tempValue:
#             list[idx] = list[idx-1]
#             idx -= 1
            
#         list[idx] = tempValue

# def Sort(list, pl, pr):
#     if len(list) < 9:
#         InsertionSort(list)
    
#     else:
#         left = pl
#         right = pr
#         # middleIndex = GetMiddleValue(list, left, (left + right)//2, right)
#         pivot = list[(left + right)//2]
        
#         # list[pivot], list[right - 1] = list[right - 1], list[pivot]
#         # left += 1
#         # right -= 2
        
#         while left <= right:
#             while list[left] < pivot: left += 1
#             while list[right] > pivot: right -= 1
            
#             if left <= right:
#                 list[left], list[right] = list[right], list[left]
#                 left += 1
#                 right -= 1
                
#         if pl < right: Sort(list, pl, right)
#         if left < pr: Sort(list, left, pr)
            
# a = int(input())
# inputList = [None] * a

# for i in range(a):
#     inputList[i] = int(input())
    
# print(inputList)
    
# Sort(inputList, 0, len(inputList) - 1)
# print(inputList)
# for i in range(len(inputList)):
#     print(inputList[i])


# # 병합 정렬
# def Sort(list):
#     def MergeSort(list, left, right):
#         if left < right:
#             center = (left + right)//2
            
#             MergeSort(list, left, center)
#             MergeSort(list, center+1, right)
            
#             p = i = 0
            
#             j = k = left
            
#             while j <= center:
#                 buff[p] = list[j]
#                 p += 1
#                 j += 1
                
#             while j <= right and i < p:
#                 if buff[i] <= list[j]:
#                     list[k] = buff[i]
#                     i += 1
#                 else:
#                     list[k] = list[j]
#                     j += 1
#                 k += 1
                
#             while i < p:
#                 list[k] = buff[i]
#                 k += 1
#                 i += 1            
                   
#     n = len(list)
#     buff = [None] * n
#     MergeSort(list, 0, n - 1)
#     del buff
        
# list = [1, 3, 12, 6, 4, 11, 8, 7, 3, 2, 6, 5]
# Sort(list)
# print(list)

