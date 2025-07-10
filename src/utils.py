import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
file_hanlder = logging.FileHandler(f"logs/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    (
        "%(asctime)s %(name)s\
                                    %(levelname)s %(message)s"
    )
)
file_hanlder.setFormatter(file_formatter)
logger.addHandler(file_hanlder)
logger.setLevel(logging.DEBUG)


def get_transactions(json_path: str) -> Any:
    """
    Читает и возвращает содержимое JSON-файла.
    В случае ошибки пути или некорректного JSON возвращает пустой словарь.
    """

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            file_json = json.load(file)
            logger.info("Файл прочитан и вовзращен результат")
            return file_json
    except FileNotFoundError:
        logger.error("Не найден файл")
        print("Указан неправильный путь")

    return []


get_transactions("d,asdl;as")
