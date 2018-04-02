def query(collection: list, select: list, *field_filter: list) -> list:
    """Creates new list of data from the source list according to selected fields.

    :param collection: a list of dicts
    :param select: a list of selected fields' names
    :param field_filter: a list(s) of fields' data (field should correspond to fields from select
    :return: new list of sorted data
    """

    for i in range(len(field_filter)):
        new_list = [{field: data[field] for field in data if field in select} for data in collection
                    if data[field_filter[i][0]] in field_filter[i][1]]
    return new_list


def select(*field_name: str) -> list:
    """Creates a list of fields chosen.

    :param field_name: name(s) of fields
    :return: list of fields selected
    """

    selected = list(field_name)
    return selected


def field_filter(*field_name) -> list:
    """

    :param field_name: data in fields
    :return: list of field's data
    """

    filtered = list(field_name)
    return filtered


friends = [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
           {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'}]

result = query(friends,
               select('name', 'gender', 'sport'),
               field_filter('sport', ['Баскетбол', 'Волейбол']),
               field_filter('gender', ['Мужской']))
print(result)
