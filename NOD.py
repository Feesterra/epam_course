nod = None
a = None
b = None
while True:
    while (type(a) != int) | (type(b) != int):
        try:
            print("Input numbers:")
            a = int(input())
            b = int(input())
        except ValueError as e:
            print("Please try again. Use integers.")
    minimal = abs(min(a, b))
    if minimal != 0:
        for i in range(1, minimal+1):
            if (a % i == 0) & (b % i == 0):
                nod = i
        print(nod)
        break
    else:
        print(abs(max(a, b)))
        break
