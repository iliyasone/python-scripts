from __future__ import annotations
from copy import deepcopy


n = int(input())

tree = [[] for _ in range(n)]
one_direct_tree = [[] for _ in range(n)]

distance = [[0 if x == y else -1 for x in range(n)] for y in range(n)]


for _ in range(n-1):
    a, b, c = map(int, input().split())
    a, b = sorted((a,b))
    tree[a-1].append((b-1, c))
    tree[b-1].append((a-1, c))
    
    one_direct_tree[a-1].append((b-1, c))
    
    distance[a-1][b-1] = distance[b-1][a-1] = c

def calc_distance(a: int, b: int, visited: set[int] | None = None):
    if visited is None:
        visited = set()
    
    if distance[a][b] != -1:
        return distance[a][b]
    
    visited.add(a)
    
    results = []
    
    for v, e in tree[a]:
        if v in visited:
            continue
        
        
        dist = calc_distance(v, b, visited.copy())
        if dist != float('+inf'):
            results.append(e + dist)
        
    if len(results) == 0:
        return float('+inf')
    
    distance[a][b] = distance[b][a] = min(results)
    return distance[a][b]


r_double_min = float('+inf')


for v in range(n):
    for u, edge in one_direct_tree[v]:
        new_distances = [0] * n

        for i in range(n):
            new_distances[i] = min(calc_distance(i, v), calc_distance(i,u))
        
        #print(u, v, new_distances)
        
        r_double = max(new_distances)
        if r_double < r_double_min:
            r_double_min =  r_double 
            
print(r_double_min)