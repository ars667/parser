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


def expression_tail(chars):
    """Обрабатывает последовательные + или - операции."""
    while chars and chars[0] in "+-":
        read_char(chars)  # Считываем '+' или '-'
        expression(chars)  # Рекурсивно вызываем expression


def expression(chars):
    """Обрабатывает выражение."""
    if chars[0] in "abcdefghijklmnopqrstuvwxyz":  # Если начинается с буквы
        letter(chars)
        expression_tail(chars)  # Проверяем, нет ли последующих + или -
    elif chars[0] == "(":  # Если начинается с '('
        read_char(chars)  # Считываем '('
        expression(chars)  # Обрабатываем выражение внутри скобок
        if chars and chars[0] == "-":
            read_char(chars)  # Считываем '-'
            expression(chars)  # Обрабатываем второе выражение
            if chars and chars[0] == ")":
                read_char(chars)  # Считываем ')'
            else:
                raise SyntaxError("Ожидалась ')'")
        else:
            raise SyntaxError("Ожидалась '-' внутри скобок")
    else:
        raise SyntaxError(f"Ожидалось выражение, найдено: {chars[0]}")


def parse(input_string):
    """Основная функция для анализа строки."""
    chars = list(input_string)  # Преобразуем строку в список символов
    try:
        expression(chars)  # Начинаем анализ с выражения
        if chars:  # Если остались необработанные символы
            raise SyntaxError(f"Лишние символы: {''.join(chars)}")
        print("Ввод успешно распознан")
    except SyntaxError as e:
        print(f"Ошибка синтаксического анализа: {e}")


# Примеры использования
if __name__ == "__main__":
    parse(input())
