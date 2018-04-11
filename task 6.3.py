while True:
    try:
        kol = int(input("Type the number of pairs: \n"))
        for i in range(kol):
            a = int(input())
            b = int(input())
            c = a / b
            print(c)
    except ValueError:
        print("Please input ints.")
    except ZeroDivisionError:
        print("Error code: division be Zero detected!")

