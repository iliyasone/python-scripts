def transform(n: int):
    b = bin(n)[2:]
    
    sum = 0
    
    for s in b:
        sum += int(s)
    
    if sum % 2 == 0:
        b += '00'
    else:
        b += '10'
        
    return int(b, 2)


for n in range(20):
    print(n, transform(n))