n, m = map(int,input().split())

bands = [[i] for i in range(n)]

bands_history = {i : 1 for i in range(n)}

current_band_by_member = {i : bands[i] for i in range(n)}

result = []


for _ in range(m):
    question = tuple(map(int,input().split()))
    
    match question:
        case 1, x, y:
            x -= 1
            y -= 1
            if current_band_by_member[x] == current_band_by_member[y]:
                pass
            else:
                new_band = current_band_by_member[x] + current_band_by_member[y]
                bands.append(new_band)
                for i in current_band_by_member[x]:
                    bands_history[i] += 1
                    if i != x:
                        current_band_by_member[i] = new_band
                for i in current_band_by_member[y]:
                    bands_history[i] += 1
                    
                    if i != y:
                        current_band_by_member[i] = new_band
                    
                current_band_by_member[x] = current_band_by_member[y] = new_band
                
                
                # bands.remove(current_band_by_member[x])
                # bands.remove(current_band_by_member[y])
        case 2, x, y:
            x -= 1
            y -= 1
            
            if current_band_by_member[x] == current_band_by_member[y]:
                print('YES')
            else:
                print('NO')
        case 3, x:
            x -= 1
            print(bands_history[x])
    