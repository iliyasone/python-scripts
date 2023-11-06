from __future__ import annotations
from typing import Sequence
import bisect

def bin_search(a: Sequence[int], x: int):
    # last smaller or equal
    left, right = 0, len(a) - 1
    ans = 0
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


def gis(a: Sequence[int], b: int) -> int:
    tails = []  
    for x in a:
        last_equal_or_smaller = bisect.bisect_right(tails, x + b)  
        if last_equal_or_smaller >= len(tails):
            tails.append(x)  
        else:
            tails[last_equal_or_smaller] = x 
    
    return len(tails)


    
n, b = map(int, input().split())
seq = tuple(map(int,input().split()))
print(gis(seq, b))