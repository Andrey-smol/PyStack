from typing import Any


class Stack:
    def __init__(self):
        self.__stack_list = []

    def is_empty(self) -> bool:
        """
        checking the stack for emptiness
        :return:
            True if stack is empty
            else False
        """
        return len(self.__stack_list) == 0

    def push(self, item: Any):
        """
        Push item into the stack (append to the top).
        """
        if item is None:
            raise ValueError('Object is None')
        self.__stack_list.append(item)

    def pop(self) -> Any:
        """
        deletes the top element of the stack
        :return: the top element of the stack
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.__stack_list.pop()

    def peek(self) -> Any:
        """
        returns the top element of the stack, but does not remove it
        :return: the top element of the stack
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.__stack_list[-1]

    def size(self) -> int:
        """
        :return: the number of items in the stack
        """
        return len(self.__stack_list)

    def __str__(self):
        return str(self.__stack_list)
