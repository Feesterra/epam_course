a = None
b = None
while (type(a) != int) or (type(b) != int):
    try:
        print("Input numbers:")
        a = int(input())
        b = int(input())
    except ValueError as e:
        print("Please try again. Use integers.")
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(abs(a + b))
