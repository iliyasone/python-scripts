def transform(n: int):
    binary = bin(n)[2:]
    sum = 0
    for d in binary:
        sum += int(d)
        
    if sum % 2 == 0:
        binary += '00'
    else:
        binary += '10'
    
    return int(binary, 2)

for i in range(100):
    print(i, transform(i))