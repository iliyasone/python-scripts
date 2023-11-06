from math import floor

n = int(input())
m = int(input())

d = m - n

c1 = int(input()) # + 1 
c2 = int(input()) # + 4

if d <= 0:
    print(0)
elif c1 <= c2/4:
    print(d*c1) # only c1
else: #c2 < 4*c1:
    a = floor(d/4)*c2 #c some c2 
    
    if (d % 4) * c1 < c2: # and maybe some c1
        a += (d % 4) * c1
    else:
        a += c2
    print(a)