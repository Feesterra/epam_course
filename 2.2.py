def change(a) -> int:
    """Function changes string to int represent the ASCII code for each char in the string.
    :param a: string to change
    :type a: str
    :returns: int"""
    
    result = 0
    for elem in a:
        ras = 0
        ost = ord(elem)
        while ost > 0:
            ost = ost // 10
            ras += 1
        result *= 10**ras
        result += ord(elem)
    return result


print(change('abcd'))
