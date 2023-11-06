def differentiate(a: list[int]):
    r = [0] * (len(a)-1)
    for i in range(1, len(a)):
        r[i-1] = a[i] - a[i-1]
        
    return r
        
n, k = map(int,input().split())
fence = list(map(int, input().split()))

# n, k = 5, 1
# fence = [1, 1, 1, 4, 4]

fence.sort()
# print(*fence)
dif = differentiate(fence) # shows difference between each element
# print(*dif)                 

v_n = v = sum(dif[0:n-k-1])
for i in range(1, k+1):
    v_n = v_n - dif[i-1] + dif[n-k-2+i]
    if v_n < v:
        #print(i, v_n, dif[i:n-k-1+i])
        v = v_n
        
print(v)