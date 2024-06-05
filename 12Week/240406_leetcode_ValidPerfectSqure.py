import sys
input = sys.stdin.readline

NUM = int(input())
isPerfect = False

def isPerfectSqure(self, num: int) -> bool:
    for i in range(2, num):
        if(i**2 == num):
            self = True
        elif(i**2 > num):
            break
    return self

print(isPerfectSqure(isPerfect, NUM))