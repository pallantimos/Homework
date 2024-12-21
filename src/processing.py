def filter_by_state(list_dict: list, state='EXECUTED') -> list:
    """ "Функция фильтрует список словарей по ключ state"""
    return [item for item in list_dict if item.get("state") == state]


def select_filter(sort_by: str) -> bool:
    """ "Функция возвращает булевый тип в зависимости от сортировки"""
    if sort_by == 'decreasing':
        return True
    else:
        return False


def sort_by_date(list_dict: list, sort_by='decreasing') -> list:
    """ "Функция сортирует список по дате"""
    return sorted(list_dict, key=lambda x: x['date'], reverse=select_filter(sort_by))
