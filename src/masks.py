import logging

logger = logging.getLogger(__name__)
file_hanlder = logging.FileHandler(f"logs/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s %(name)s\
                                    %(levelname)s %(message)s"
)
file_hanlder.setFormatter(file_formatter)
logger.addHandler(file_hanlder)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """ " Функция принимает номер карты, далее шифрует и возвращает маску"""
    if not isinstance(card_number, str):
        card_number = str(card_number)

    card_number_spaceless = "".join(filter(str.isdigit, card_number))

    if len(card_number_spaceless) != 16:
        logger.error("Некорректная длина номера карты")
        return "Некорректная длина номера карты"

    mask_card_number = (
        card_number_spaceless[0:4]
        + " "
        + card_number_spaceless[4:6]
        + "** **** "
        + card_number_spaceless[12:]
    )

    logger.info("Успешно зашифрован номер карты и возвращена маска")
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """ " Функция принимает номер счета, далее шифрует и возвращает маску"""
    if not isinstance(account_number, str):
        account_number = str(account_number)

    account_number_spaceless = "".join(filter(str.isdigit, account_number))

    if len(account_number_spaceless) != 20:
        logger.error("Некорректная длина номера карты")
        return "Некорректная длина номера карты"

    logger.info("Успешно зашифрован номер счета и возвращена маска")
    return "**" + account_number_spaceless[-4:]


get_mask_account("dm,sadk")
