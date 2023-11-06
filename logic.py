A = 0
B = 0
C = 1

print("A B C f f1")
for A in (0,1):
    for B in (0,1):
        for C in (0,1):
            l = A * B + A * B * (not C) + B * (not C) + C
            r = (not C) + A * C + (not A) * B * (not C)
            print(A, B, C, l and r)