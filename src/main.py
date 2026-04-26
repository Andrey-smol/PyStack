from src.stack import Stack


def checking_balance_brackets(str_: str) -> str:
    """
    checking the balance of the brackets
    :param str_: a string with parentheses
    :return: сообщение: «Сбалансированно», если строка корректная,
            и «Несбалансированно», если строка составлена неверно.
    """
    stack = Stack()
    brackets_dict = {
        'opening': ('(', '[', '{'),
        'closing': (')', ']', '}')
    }
    for letter in str_:
        if letter in brackets_dict['opening']:
            stack.push(letter)
        elif letter in brackets_dict['closing']:
            idx = brackets_dict['closing'].index(letter)
            opening_letter = brackets_dict['opening'][idx]
            if stack.size() and stack.peek() == opening_letter:
                stack.pop()
            else:
                return 'Несбалансированно'
    return 'Сбалансированно' if stack.is_empty() else 'Несбалансированно'


if __name__ == "__main__":
    pass
