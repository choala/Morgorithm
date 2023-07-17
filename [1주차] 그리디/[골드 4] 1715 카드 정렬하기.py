import sys
import heapq

n = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

result = 0
if n == 1:
    print(result)
else:
    for i in range(n-1):
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        result += first + second
        heapq.heappush(cards, first+second)
        
    print(result)
