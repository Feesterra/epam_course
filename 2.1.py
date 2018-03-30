def intersect(*args):
    result = set(args[0])
    for i in range(1, len(args)):
        result = result & set(args[i])
    print(result)


def union(*args):
    result = set(args[0])
    for i in range(1, len(args)):
        result = result | set(args[i])
    print(result)


intersect('spam', 'cams', 'trapse')
union('spam', 'cams', 'trapse')
