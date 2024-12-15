def read_char(chars):
    if not chars:
        raise SyntaxError("Неожиданный конец ввода")
    return chars.pop(0)


def letter(chars):
    if chars[0] in "abcdefghijklmnopqrstuvwxyz":
        read_char(chars)
    else:
        raise SyntaxError(f"Ожидалась буква, найдено: {chars[0]}")


def expression_tail(chars, flag):
    if not flag:
        while chars and chars[0] in "+-":
            read_char(chars)
            expression(chars, flag)
    else:
        while chars and chars[0] in "+-":
            ind = chars.index(')')
            if not '-' in chars[:ind]:
                raise IndexError('в скобках может быть только -')
            read_char(chars)
            expression(chars, 0)


def expression(chars, flag):
    if chars[0] in "abcdefghijklmnopqrstuvwxyz":
        letter(chars)
        expression_tail(chars, flag)
    elif chars[0] == "(":
        read_char(chars)
        expression(chars, 1)
        if chars and chars[0] == ")":
            read_char(chars)
        else:
            raise SyntaxError("Ожидалась ')'")
    else:
        raise SyntaxError(f"Ожидалось выражение, найдено: {chars[0]}")


def parse(input_string):
    chars = list(input_string.replace(" ", ""))
    try:
        expression(chars, 0)
        if chars:
            raise SyntaxError(f"Лишние символы: {''.join(chars)}")
        print("Ввод успешно распознан")
    except SyntaxError as e:
        print(f"Ошибка синтаксического анализа: {e}")


if __name__ == "__main__":
    print(
        'Алгебраические формулы со скобками и знаками операций + и -. При этом сумма операндов никогда не берется в скобки, а разность может браться, а может нет\nПример: a+b-(c-(d-f))')
    for i in range(10000):
        try:
            parse(input("Введите выражение: "))
        except:
            print("Выржение не распознано")
