def filter_by_state(list_dict: list, state='EXECUTED') -> list:
    return [item for item in list_dict if item.get("state") == state]


def choose_filter(sort_by: str):
    if sort_by == 'убывание':
        return True
    else:
        return False


def sort_by_date(list_dict: list, sort_by='убывание') -> list:
    return sorted(list_dict, key=lambda x: x['date'], reverse=choose_filter(sort_by))
