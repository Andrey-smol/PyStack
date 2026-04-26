import pytest

from src.main import checking_balance_brackets


@pytest.mark.parametrize('text, expected',
                         (
                                 ('(((([{}]))))', 'Сбалансированно'),
                                 ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
                                 ('{{gh[(lk;)]rtyu}}', 'Сбалансированно')
                         ))
def test_checking_balance_brackets_balanced(text, expected):
    result = checking_balance_brackets(text)
    assert result == expected, f'Ожидаемый результат {expected}, а получено {result}'


@pytest.mark.parametrize('text, expected',
                         (
                                 ('}{}', 'Несбалансированно'),
                                 ('{qw{[(gh])]p}}', 'Несбалансированно'),
                                 ('[[{())}]', 'Несбалансированно')
                         ))
def test_checking_balance_brackets_not_balanced(text, expected):
    result = checking_balance_brackets(text)
    assert result == expected, f'Ожидаемый результат {expected}, а получено {result}'
