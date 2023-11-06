n = int(input())
tree = [int(input()) for _ in range(n)]
count_ancestors = [0] * n

for i in range(n):
    if tree[i] == 0:
        count_ancestors[i] = 1
    else:
        count_ancestors[i] = count_ancestors[tree[i]-1]+1
    
print(count_ancestors.index(max(count_ancestors))+1)