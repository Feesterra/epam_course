def intersect(*args):
    res = []
    result =[]
    count = len(args)
    for arg in args:
        arg = list(arg)
        res.extend(arg)
    for el in res:
        num = res.count(el)
        if num == count:
            result.append(el)
    print(set(result))


def union(*args):
    res = []
    for arg in args:
        arg = list(arg)
        res.extend(arg)
    print(set(res))


intersect('spam', 'scamp', 'trapse')
union('spam', 'scamp', 'trapse')
