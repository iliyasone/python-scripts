from __future__ import annotations
from typing import Sequence
import bisect

def bin_search(a: Sequence[int], x: int):
    # last smaller or equal
    left, right = 0, len(a) - 1
    
    ans = -1
    while  left <= right:
        middle = (left + right) // 2 
        if a[middle] == x:
            return middle
        elif a[middle] < x:
            ans = middle
            left = middle + 1
        else:
            right = middle - 1
            
    return ans

def gis(a: Sequence[int], b: int):
    n = len(a)
    particular_greates = [0] * n
    particular_greates[0] = 1
    
    done = [a[0]]
    for i in range(1, n):
        m = 1
        
        if a[i] == 6:
            pass
        
        max_index = bin_search(done, a[i])
        for j in range(max_index, -1, -1):
            if done[j] + b < a[i]:
                break
            if particular_greates[done[j]] + 1 > m:
                m = particular_greates[done[j]] + 1
        
        
        particular_greates[a[i]] = m
        
        done.insert(bisect.bisect_right(done, a[i]), a[i])
    #print(done)
    #print(particular_greates)
    return max(particular_greates)
    
n, b = map(int, input().split())
seq = tuple(map(int,input().split()))
print(gis(seq, b))