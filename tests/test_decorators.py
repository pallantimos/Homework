from src.decorators import log

def test_log_ok():
    @log(filename="mylog.txt")
    def test(x, y):
        return x + y

    test(1, 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        last_line = lines[-1].strip() if lines else ""
    assert last_line == "test ok"


def test_log_err():
    @log(filename="mylog.txt")
    def test(x, y):
        return x + y

    test("1", 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        last_line = lines[-1].strip() if lines else ""
    assert (
        last_line == "test error: TypeError('can only concatenate "
                     "str (not \"int\") to str'). Inputs: (('1', 2)), {}"
    )


def test_log_ok_console(capsys):
    @log()
    def test(x, y):
        return x + y

    test(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "test ok\n"


def test_log_err_console(capsys):
    @log()
    def test(x, y):
        return x + y

    test("1", 2)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "test error: TypeError('can only concatenate str "
           "(not \"int\") to str'). Inputs: (('1', 2)), {}\n"
    )
