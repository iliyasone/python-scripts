f = open('input.txt', 'r')
def input():
    return f.readline().strip()

students, _ = map(int, input().split())

programs_space = {
    i+1 : int(s) 
    for i, s in enumerate(input().split())
}

all_students_by_rating: dict[
    int, 
    list[tuple[list[int],int]]
    ] = {}

results = [-1] * students

# print(programs_space)
for i in range(students):
    rating, _, *programs = map(int, input().split())
    if rating in all_students_by_rating:
        all_students_by_rating[rating].append((programs, i))
    else:
        all_students_by_rating[rating] = [(programs,i)]

print(all_students_by_rating)

for rating, items in sorted(all_students_by_rating.items()):
    print(items)
    sample_programs_space = programs_space.copy()
    while True:
        overflown = []
        current_program_space = sample_programs_space.copy()
        for student, i in items:
            for wanted_program in student:
                if wanted_program in current_program_space:
                    current_program_space[wanted_program] -= 1
                    
                    if current_program_space[wanted_program] < 0:
                        overflown = [wanted_program] 
                        break
                    
                    results[i] = wanted_program
                    break
            else:
                results[i] = -1
        
        if len(overflown) > 0:
            for program in overflown:
                del sample_programs_space[program]
        else:
            for i in current_program_space:
                programs_space[i] -= sample_programs_space[i] - current_program_space[i]
            break

print(*results)

f.close()
del f