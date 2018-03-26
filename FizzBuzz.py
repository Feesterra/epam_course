a = [x for x in range(1, 101)]

for x in range(len(a)):
    if a[x] % 15 == 0:
        a[x] = 'FizzBuzz'
    elif a[x] % 3 == 0:
        a[x] = 'Fizz'
    elif a[x] % 5 == 0:
        a[x] = 'Buzz'

print(a)
