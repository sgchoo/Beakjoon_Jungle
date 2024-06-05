# print('이름을 입력하세요: ', end='')
# name =  input()
# print(f'안녕하세요 {name}님')

# print(1, 2, 3, sep='and')

# name = input('이름을 입력하세요: ')
# print(f'안녕하세요 {name}님')

# b = float('3.14')
# print(b, type(b))

# ----------중앙 값 구하기--------------
# def med3(a, b, c):
#     if a >= b:
#         if b >= c:      return b
#         elif a >= c:    return c
#         else:           return a
        
#     elif a > c:         return a
    
#     elif b > c:         return c
    
#     else:               return b
    
# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요: '))
# b = int(input('정수 b의 값을 입력하세요: '))
# c = int(input('정수 c의 값을 입력하세요: '))

# print(f'중앙값 = {med3(a, b, c)}')

# --------- 정수의 합 구하기------------
# n = int(input('limit: '))

# sum = 0
# i = 1

# while i<=n:
#     sum += i
#     i += 1
    
# print(sum)

# ------------약수 구하기-----------------
# area = int(input('직사각형의 넓이를 입력하세요.: '))

# for i in range(1, area + 1):
#     if i * i > area: break
#     if area % i: continue
#     print(f'{i} X {area // i}')

#------------시퀀스 원소의 최댓값 출력하기-----------
# from typing import Any, Sequence

# def max_of(a: Sequence) -> Any:
#     maximum = a[0]
#     for i in range(1, len(a)):
#         if a[i] > maximum:
#             maximum = a[i]
#     return maximum

# if __name__ == '__main__':
#     print('배열의 최댓값을 구합니다.')
#     num = int(input('원소 수를 입력하세요: '))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]값을 입력하세요: '))
        
#     print(f'최댓값을 {max_of(x)}입니다')

#int, string = map(str, input().split())

# #Solve1(시간초과)
# # ----------- Beakjoon 9020(골드바흐의 추측)---------------
# def PrimeNumber(a):
#     list = []
#     if a == 1:
#         return
    
#     for i in range(2, a):
#         check = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 check += 1
#             if j == i and check == 2:
#                 list.append(i)
                
#     return list


# a = int(input())
# primeNumList = []

# for _ in range(a):
#     primeNumList.append(int(input()))
    
# for num in primeNumList:
#     if num % 2:
#         continue
#     tempList = PrimeNumber(num)
#     resultList = []
    
#     for i in range(len(tempList)):
#         if i == len(tempList) - 1:
#             break
#         for j in range(len(tempList)):
#             if tempList[i] + tempList[j] == num:
#                 resultList.append((tempList[i], tempList[j]))
#                 break
    
#     a, b = resultList[0][0], resultList[0][1]
#     for i in resultList:
#         if abs(a - b) > abs(i[0] - i[1]):
#             a, b = i[0], i[1]
           
#     if a > b:
#             print(f'{b} {a}')
#     else:
#         print(f'{a} {b}')

# # #Solve2(시간초과)
# def PrimeNumberCheck(a):
#     check = 0
    
#     if a == 2:
#         return True
    
#     for i in range(1, a + 1):
#         if a % i == 0:
#             check += 1
#         if i == a and check > 2:
#             return False
        
#     return True


# a = int(input())

# for _ in range(a):
#     num = (int(input()))
    
#     elementA = num // 2
#     elementB = num // 2
    
#     for _ in range(num // 2):
#         if PrimeNumberCheck(elementA) and PrimeNumberCheck(elementB):
#             print(elementA, elementB)
#             break
        
#         else:
#             elementA -= 1
#             elementB += 1
            
# # Solve3(성공)
# def PrimeNumberCheck(n):
#     if n == 1:
#         return False
#     for j in range(2, int(n**0.5) + 1):
#         if n % j == 0:
#             return False
#     return True

# a = int(input())

# for _ in range(a):
#     num = (int(input()))
    
#     elementA = num // 2
#     elementB = num // 2
    
#     for _ in range(num // 2):
#         if PrimeNumberCheck(elementA) and PrimeNumberCheck(elementB):
#             print(elementA, elementB)
#             break
        
#         else:
#             elementA -= 1
#             elementB += 1

# # ------------Beakjoon 10872(팩토리얼)--------------
# def Fatorial(a):
#     if a > 0:
#         return a*Fatorial(a - 1)
#     else:
#         return 1
    
# num = int(input())

# print(Fatorial(num))

