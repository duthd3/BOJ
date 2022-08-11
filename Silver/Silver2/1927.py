import sys
import heapq

_list = []
heapq.heapify(_list)

calnum = int(input())
for i in range(calnum):
    inputnum = int(sys.stdin.readline())
    if inputnum != 0:
        heapq.heappush(_list, inputnum)
    else:
        try:
            print(heapq.heappop(_list))
        except:
            print(0)
        
