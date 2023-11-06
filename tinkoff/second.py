line = input()

word = "sherif"
letters = {s : 0 for s in word}

for s in line:
    if s in word:
        letters[s] += 1

letters['f'] //= 2
print(min(letters.values()))