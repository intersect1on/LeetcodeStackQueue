from collections import deque

class Stack:
    def __init__(self):
        self._stack = deque()

    def is_empty(self):
        return len(self._stack) == 0

    def length(self):
        return len(self._stack)

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]

    def push(self, item):
        self._stack.append(item)


class MyQueue:
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def push(self, x):
        self.input_stack.push(x)

    def pop(self):
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())

        return self.output_stack.pop()

    def peek(self):
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())

        return self.output_stack.peek()

    def empty(self):
        return self.input_stack.is_empty() and self.output_stack.is_empty()
