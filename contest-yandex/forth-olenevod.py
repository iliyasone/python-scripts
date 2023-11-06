f = open('input.txt', 'r')
def input():
    return f.readline().strip()

def differentiate(a: list[int]):
    r = [0] * (len(a)-1)
    for i in range(1, len(a)):
        r[i-1] = a[i] - a[i-1]
        
    return r 
        

k, n, m = map(int, input().split())

schedule: dict[int, list[int]] = {} # walk : days_occupaed


for _ in range(n):
    d, w = map(int, input().split())
    
    if w in schedule:
        schedule[w].append(d)
    else:
        schedule[w] = [d]

if m >= n:
    print(0)
elif len(schedule) > m:
    print(-1)
elif len(schedule) == m:
    result = 0
    
    for w, days in schedule.items():
        if len(days) > 1:
            result += days[-1] - days[0]

    print(result)
else:
    results = []
    free_excavation = m
    
    for w, days in sorted(schedule.items()):
        # print(w, days,differentiate(days))
        if len(days) > 1:
            results.extend(differentiate(days))
        free_excavation -= 1
        
    results.sort()
    print(sum(results[:-free_excavation]))
    # print(results, free_excavation)
    
f.close()
