a = []
for n in range(2, 100):
    is_prime = True
    for d in range(2, int(n**0.5)+1):
        if n%d == 0:
            is_prime = False
            break
    
    if is_prime:
        a.append(n)
        print(n)