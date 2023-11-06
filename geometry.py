from math import tan, pi

count = 0
for x in range(-1,12):
    for y in range(-1,12):
        if x > 0 and y > tan(pi/6) * x and y < - tan(pi/6) * x + 10:
            count += 1 
            
print(count)