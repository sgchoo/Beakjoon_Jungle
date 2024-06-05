import sys
input = sys.stdin.readline

AMOUNT, NUM = map(int, input().split())

cards = list(map(int, input().split()))

blackJack = 0

for i in range(AMOUNT - 2):
    for j in range(i+1, AMOUNT - 1):
        for k in range(j+1, AMOUNT):
            sum = cards[i]+cards[j]+cards[k]
            if sum <= NUM and blackJack < sum:
                blackJack = sum
                
print(blackJack)