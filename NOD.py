minimal = 1
nod = None

while True:
    a = int(input())
    b = int(input())
    if a <= b:
        minimal = abs(a)
    else:
        minimal = abs(b)
    if minimal != 0:
        for i in range(1, minimal+1):
            if (a % i == 0) & (b % i == 0):
                nod = i
        break
    else:
        print('Division by zero is not defined. Please input other integers next time.')
print(nod)
