import re
a = open("/Users/waltermundt-petersen/Desktop/Advent of Code 2024/Day3/input.txt", "r").read().strip()
ans = 0
on = True
for i in range(len(a)):
    if a[i:i+4] == 'do()':
        on = True
    if a[i:i+7] == "don't()":
        on = False
    if a[i:i+4] == 'mul(': #hitta början av sekvens
        j = i+4 # hitta slut av sekvens
        while a[j] != ')':
            j += 1
        try:
            x,y = list(map(int, re.findall('\d+', a[i:j+1])))
            
            if a[j-1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                continue
            print(a[i:j+1])
            print(x, y)
            if on:
                ans += x*y    
        except:
            pass
print(ans)