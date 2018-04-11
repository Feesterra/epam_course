class Prop(object):
    """Emulates property."""

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)


# written for testing
class Something:
    """Class with attribute.
    :param value: any parameter.
    """

    def __init__(self, value):
        self.attr = value

    # testing class Property
    @Prop
    def getting(self):
        return self.attr


class AnotherSomething(object):
    """Another class with attribute."""

    def __init__(self):
        self.value = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def del_value(self):
        self.value = 'Not exist'

    cot = Prop(get_value, set_value, del_value, 'свойство cot')


if __name__ == '__main__':
    s = Something(42)
    print(s.getting)
    print(type(AnotherSomething.cot))
    anx = AnotherSomething()
    print(anx.cot)
    anx.cot = 47
    print(anx.cot)
    anx.cot = 111
    print(anx.cot)
    del anx.cot
    print(anx.cot)




