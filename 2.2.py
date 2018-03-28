def change(a):
    result = 0
    for elem in a:
        ras = 0
        ost = ord(elem)
        while ost > 0:
            ost = ost // 10
            ras += 1
        result *= 10**ras
        result += ord(elem)
    print(result)


change('abcd')
