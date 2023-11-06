print("w x y z F")

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = ((x <= y) or (y == w)) and ((x or z) == w)
                if f:
                    print(w, x, y ,z , int(f))