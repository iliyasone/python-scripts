_, money = map(int, input().split())
guns = list(map(int, input().split()))

most_expensive = 0

for price in guns:
    if price > most_expensive and money >= price:
        most_expensive = price
        
print(most_expensive)