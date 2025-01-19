from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """ "Функция принимает номер карты или номер счета,
    далее шифрует и возвращает маску"""
    if account_card[0:4] == "Счет":
        return "Счет " + get_mask_account(account_card[5:])
    else:
        card_number_split = account_card.split(" ")
        hashed_card_number = get_mask_card_number(card_number_split[-1])
        card_number_split.pop()
        card_number_split.append(hashed_card_number)
        return " ".join(card_number_split)


def get_date(date: str) -> str:
    """ "Функция принимает дату в формате 2024-03-11T02:26:18.671407
    и возвращает в формате ДД.ММ.ГГГГ"""
    only_date = date[0:10].split("-")
    only_date.reverse()
    return ".".join(only_date)
