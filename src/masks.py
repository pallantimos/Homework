def get_mask_card_number(card_number: str) -> str:
    """ " Функция принимает номер карты, далее шифрует и возвращает маску"""
    if not isinstance(card_number, str):
        card_number = str(card_number)

    card_number_spaceless = "".join(filter(str.isdigit, card_number))

    if len(card_number_spaceless) != 16:
        return "Некорректная длина номера карты"

    mask_card_number = (
        card_number_spaceless[0:4] + " " + card_number_spaceless[4:6] +
        "** **** " + card_number_spaceless[12:]
    )
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """ " Функция принимает номер счета, далее шифрует и возвращает маску"""
    if not isinstance(account_number, str):
        account_number = str(account_number)

    account_number_spaceless = "".join(filter(str.isdigit, account_number))

    if len(account_number_spaceless) != 20:
        return "Некорректная длина номера карты"

    return "**" + account_number_spaceless[-4:]
