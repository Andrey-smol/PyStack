import pytest
from src.stack import Stack


@pytest.fixture
def create_stack():
    stack = Stack()
    yield stack
    del stack


@pytest.fixture
def push_stack(create_stack):
    create_stack.push('Hello')
    create_stack.push('Test')
    create_stack.push(2)
    create_stack.push(3)
    yield create_stack


def test_stack_push_error(create_stack):
    with pytest.raises(ValueError):
        create_stack.push(None)


def test_stack_is_empty(create_stack):
    expected = True
    result = create_stack.is_empty()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"


def test_stack_is_empty_false(push_stack):
    expected = False
    result = push_stack.is_empty()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"


@pytest.mark.parametrize('initial, expected',
                         (
                                 ([1, 2, 3], 3),
                                 ([1, 2], 2),
                                 (["Test"], "Test")
                         ))
def test_stack_pop(create_stack, initial, expected):
    for item in initial:
        create_stack.push(item)
    result = create_stack.pop()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"


def test_stack_pop_(push_stack):
    expected = 3
    result = push_stack.pop()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"
    expected = 2
    result = push_stack.pop()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"
    expected = 'Test'
    result = push_stack.pop()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"


def test_stack_error(create_stack):
    with pytest.raises(IndexError):
        create_stack.pop()


def test_stack_peek(push_stack):
    expected = 3
    result = push_stack.peek()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"


def test_stack_size(push_stack):
    expected = 4
    result = push_stack.size()
    assert result == expected, f"Ожидаемое значение {expected}, полученное {result}"
