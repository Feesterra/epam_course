class Price:
    """Checks parameters (0-100)."""
    
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        print("Descr.__get__")
        return self.__dict__[self.label]

    def __set__(self, instance, value):
        print("Descr.__set__")
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        else:
            self.__dict__[self.label] = value


class Book:
    """Represent a book.
    :param author: author's name. Contains letters only
    :param title: book's heading
    :param price: book's price
    :type price: int between 0 and 100.
    """

    price = Price("price")

    def __init__(self, author, title, price):
        if author.isalpha:
             self.author = author
        else:
            raise ValueError("Author's name should contain letters only.")
        self.title = title
        self.price = price


if __name__ == '__main__':
    chelinger = Book("William Faulkner", "The Sound and the Fury", 12)
    # chelinger.price = -12
    chelinger.price = 100
    print(chelinger.price)
