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


class FreqStack:
    def __init__(self):
        self.stack = Stack()
        self.freq = {}

    def push(self, val):
        self.stack.push(val)
        self.freq[val] = self.freq.get(val, 0) + 1

    def pop(self):
        temp = Stack()
        max_freq = max(self.freq.values())
        result = None

        while not self.stack.is_empty():
            val = self.stack.pop()

            if self.freq[val] == max_freq:
                result = val
                self.freq[val] -= 1
                break

            temp.push(val)

        while not temp.is_empty():
            self.stack.push(temp.pop())

        return result
