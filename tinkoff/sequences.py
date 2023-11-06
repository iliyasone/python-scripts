n = int(input())
current = list(map(int,input().split()))
target = list(map(int,input().split()))





def result(current: list[int], target: list[int]):
    for i in range(n):
        if current[i] != target[i]:
            first_difference = i
            break
    else:
        return True
        
    for i in range(n - 1, -1, -1):
        if current[i] != target[i]:
            last_diffrence = i
            break
    else:
        assert False
    
    target = target[first_difference:last_diffrence+1]
    current = current[first_difference:last_diffrence+1]
    
    current.sort()
    
    return current == target

if result(current, target):
    print("YES")
else:
    print("NO")
    

