def get_mask_card_number(card_number: str) -> str:
    """ " Функция принимает номер карты, далее шифрует и возвращает маску"""
    if type(card_number) is not str:
        card_number = str(card_number)

    mask_card_number = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """ " Функция принимает номер счета, далее шифрует и возвращает маску"""
    if type(account_number) is not str:
        account_number = str(account_number)

    return "**" + account_number[-4:]
