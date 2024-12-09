class SyntaxError(Exception):
    """Исключение для синтаксических ошибок."""
    pass


def read_char(chars):
    """Считывает текущий символ и продвигается к следующему."""
    if not chars:
        raise SyntaxError("Неожиданный конец ввода")
    return chars.pop(0)


def letter(chars):
    """Обрабатывает букву."""
    if chars[0] in "abcdefghijklmnopqrstuvwxyz":
        read_char(chars)
    else:
        raise SyntaxError(f"Ожидалась буква, найдено: {chars[0]}")


def expression_tail(chars, flag):
    """Обрабатывает последовательные + или - операции."""
    if not flag:
        while chars and chars[0] in "+-":
            # Считываем '+' или '-'
            read_char(chars)
            expression(chars, flag)  # Рекурсивно вызываем expression
    else:
        if chars[0] == '+':
            raise ValueError("Нельзя ставить + в скобках")
        while chars and chars[0] in "-":
            # Считываем '+' или '-'
            read_char(chars)
            expression(chars, flag)


def expression(chars, flag):
    """Обрабатывает выражение."""
    if chars[0] in "abcdefghijklmnopqrstuvwxyz":  # Если начинается с буквы
        letter(chars)
        expression_tail(chars, flag)  # Проверяем, нет ли последующих + или -
    elif chars[0] == "(":  # Если начинается с '('
        read_char(chars)  # Считываем '('
        print(chars)
        expression(chars, 1)  # Обрабатываем первое выражение внутри скобок
        print(chars)
        if chars and chars[0] == ")":  # Проверяем закрывающую скобку
            read_char(chars)
        else:
            raise SyntaxError("Ожидалась ')'")
    else:
        raise SyntaxError(f"Ожидалось выражение, найдено: {chars[0]}")


def parse(input_string):
    """Основная функция для анализа строки."""
    chars = list(input_string.replace(" ", ""))  # Преобразуем строку в список символов, убираем пробелы
    try:
        expression(chars, 0)  # Начинаем анализ с выражения
        if chars:  # Если остались необработанные символы
            raise SyntaxError(f"Лишние символы: {''.join(chars)}")
        print("Ввод успешно распознан")
    except SyntaxError as e:
        print(f"Ошибка синтаксического анализа: {e}")


# Примеры использования
if __name__ == "__main__":
    print('Алгебраические формулы со скобками и знаками операций + и -. При этом сумма операндов никогда не берется в скобки, а разность может браться, а может нет\nПример: a+b-(c-(d-f))')
    parse(input("Введите выражение: "))
    input()
