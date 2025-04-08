from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque()

    def is_empty(self):
        return len(self._queue) == 0

    def length(self):
        return len(self._queue)

    def pop(self):
        if not self.is_empty():
            return self._queue.popleft()

    def peek(self):
        if not self.is_empty():
            return self._queue[0]

    def add(self, item):
        self._queue.append(item)


class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x):
        self.queue.add(x)

        for _ in range(self.queue.length() - 1):
            self.queue.add(self.queue.pop())

    def pop(self):
        return self.queue.pop()

    def top(self):
        return self.queue.peek()

    def empty(self):
        return self.queue.is_empty()
