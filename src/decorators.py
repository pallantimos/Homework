from typing import Any, Callable


def log(filename: str = "console") -> Callable:
    """ "Декоратор логирует данные о работе функции в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if filename == "console":
                    print(f"{func.__name__} error: {repr(e)}. Inputs: ({args}), {kwargs}")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {repr(e)}. Inputs: ({args}), {kwargs}\n")
                return None
            else:
                if filename == "console":
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                return result

        return wrapper

    return decorator
