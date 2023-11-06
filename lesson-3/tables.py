#(x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w

print('x w z ')
for x in (0,1):
    for y in (0,1):
        for z in (0,1):
            for w in (0,1):
                r = (x and not y) or (y == z) or (not w)
                
                if not r:
                    print(x,w,z,y, 0)