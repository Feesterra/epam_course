import itertools


def students_data():
    """Represents data about students.
    :returns: list of dicts.
    """

    return [
        {'name': 'Alexey', 'rate': 2, 'course': 'Python'},
        {'name': 'Vali', 'rate': 5, 'course': 'Java'},
        {'name': 'Olga', 'rate': 4, 'course': 'Python'},
        {'name': 'Frank', 'rate': 5, 'course': 'Python'},
        {'name': 'Masha', 'rate': 3, 'course': 'Java'},
        {'name': 'Vasily', 'rate': 2, 'course': 'Java'},
        {'name': 'Daria', 'rate': 3, 'course': 'Python'},
        {'name': 'Nickname', 'rate': 4, 'course': 'Python'},
        {'name': 'Fort', 'rate': 3, 'course': 'Java'},
        {'name': 'Lama', 'rate': 4, 'course': 'Java'},
        {'name': 'Pop', 'rate': 2, 'course': 'Python'},
        {'name': 'Sort', 'rate': 3, 'course': 'Python'},
        {'name': 'Elya', 'rate': 5, 'course': 'Java'},
        {'name': 'Tolik', 'rate': 4, 'course': 'Python'},
    ]


def get_course(data):
    """Makes a set with courses from data.
    :param data: dict/list of dicts with key 'course'.
    :returns: set of items.
    """

    return {item['course'] for item in data}


def get_rates(data, course):
    """Filters data by given items.
    :param data: dict/list of dicts
    :param course: any probable key in data ('course' suggested)
    :returns: sorted reversed list of data (sorted by field 'rate').
    """

    return sorted([(item['name'], item['rate']) for item in data if item['course'] == course],
                  key=lambda x: x[1], reverse=True)


def top_students_table(course):
    """Represents TOP-3 students of each course.
    :param course: course name
    :returns: formatted strings of course, names and rates.
    """

    return 'COURSE {}\n'.format(course) + \
           '\n'.join('{:10} --- {:4}'.format(*rate)
                     for rate in itertools.islice(get_rates(students_data(), course), 3))


if __name__ == '__main__':
    print('\n'.join(top_students_table(course) for course in get_course(students_data())))
