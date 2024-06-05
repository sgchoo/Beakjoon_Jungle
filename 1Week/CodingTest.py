# # ---------------------Beakjoon 1110번(더하기 사이클)---------------------------------
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

# # ---------------------------Beakjoon 1182번(BackTracking)-------------------------------------
# def Sum(idx):
#     global N
#     global K
#     global count
    
#     if sum(resultList) == K and len(resultList) > 0:
#         count += 1
#         return
    
#     for i in range(idx, N):
#         resultList.append(list[i])
#         Sum(i+1)
#         resultList.pop()
    
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# list = list(map(int, input().split()))
# resultList = []
# count = 0

# Sum(0)
# print(count)

# # ------------beakjoon 15649(N과 M(1), BackTracking)-------------

# def CheckElement():
#     if len(resultList) == M: 	# 요소 갯수가 맞으면 출력후 리턴
#         print(" ".join(map(str, resultList)))
#         return
    
#     for i in range(1, N+1):
#         if visited[i-1]: 		# 방문한 곳이면 건너뛰기
#             continue
#         resultList.append(i) 	# 아니라면 i를 리스트에 넣어준 후
#         visited[i-1] = True 	# 사용했다고 바꾸고
#         CheckElement()			# 다음 수를 넣어준다
#         resultList.pop()		# 만약 조건에 맞지 않는다면 pop해준다
#         visited[i-1] = False	# 사용 bool값을 되돌려준다.

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# visited = [False] * N
# resultList = []

# CheckElement()

# ---------Beakjoon 1992(쿼드트리)------------
def Divide(start, end, n):
    color = board[start][end]
    
    for i in range(start, start+n):
        for j in range(end, end+n):
            if color != board[i][j]:
                Divide(start, end, n//2)
                Divide(start, end+n//2, n//2)
                Divide(start+n//2, end, n//2)
                Divide(start+n//2, end+n//2, n//2)
                return
            
    if color == 0:
        result.append(0)
    else:
        result.append(1)
    
    
import sys
input = sys.stdin.readline

a = int(input())
board = []
print(board)
result = []
Divide(0, 0, a)
print(result)

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
# import sys
# input = sys.stdin.readline

# n = int(input())

# arr = [list(input()) for _ in range(n)]

# ans = []

# def compare(n, x, y):
# 	for i in range(n):
# 		for j in range(n):
# 			if arr[i + y][j + x] != arr[y][x]:
# 				return 0
# 	return 1

# def sol(n, x, y):
# 	if compare(n, x, y):
# 		ans.append(arr[y][x])
# 	else:
# 		n //= 2
# 		ans.append('(')
# 		sol(n, x, y)
# 		sol(n, x + n, y)
# 		sol(n, x, y + n)
# 		sol(n, x + n, y + n)
# 		ans.append(')')

# sol(n, 0, 0)

# print("".join(ans))