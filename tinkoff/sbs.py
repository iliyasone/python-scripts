def get_all_subsequances(n: list):
    sub_sequances: set[tuple] = {(),}
    
    for i in range(len(n)):
        for sub_seq in sub_sequances.copy():
            sub_sequances.add(sub_seq + (n[i],))
            
    return sub_sequances


n, m = map(int, input().split())
money = list(map(int, input().split()))
money.extend(money)

for s in get_all_subsequances(money):
    if sum(s) == n:
        print(len(s))
        print(*sorted(s))
        break
else:
    print(-1)