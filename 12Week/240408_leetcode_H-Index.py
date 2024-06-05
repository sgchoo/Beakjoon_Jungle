import sys
input = sys.stdin.readline

citations = list(map(int, input().split(' ')))
sortedCitations = sorted(citations, reverse=True)

h_index = 0

for i in range(len(sortedCitations)):
    h_index = max(h_index, min(sortedCitations[i], i + 1))
    
print(h_index)