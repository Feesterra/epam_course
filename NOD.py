minimal = 1
nod = None

while True:
    a = int(input())
    b = int(input())
    if a <= b:
        minimal = a
    else:
        minimal = b
    if minimal != 0:
        for i in range(1, abs(minimal)+1):
            if (a % i == 0) & (b % i == 0):
                nod = i
        print(nod)
        break
    else:
        print('Division by zero is not defined. Please input other integers next time.')
