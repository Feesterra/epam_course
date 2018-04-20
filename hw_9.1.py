import time
import datetime


class MineManager:
    def __init__(self):
        """Constructor. Creates or opens a file to write information there."""

        self.f = open('/home/alex/Документы/out_err.txt', 'w')

    def __enter__(self):
        """Calculates date time when managed function is run."""

        self.start_t = datetime.datetime.now()
        self.in_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """If an error occurs, writes to file information about date, time, duration of function executed and error."""

        if exc_type:
            timing = time.time() - self.in_time
            self.f.write('Date and time: {},\nDuration: {}\n'.format(self.start_t, timing))
            self.f.write('Error: {} {} {}'.format(exc_type, exc_val, exc_tb))
        self.f.close()
        return False


def managed():
    """Function prints something."""

    print('Inside manager')
    print('ihfhdv'[333])


if __name__ == '__main__':
    with MineManager():
        managed()





