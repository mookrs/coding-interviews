class MyQueue:
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else 'queue is empty'


q = MyQueue()
q.push(1)
q.push(2)
print(q.pop())
q.push(3)
print(q.pop())
q.push(4)
print(q.pop())
print(q.pop())
print(q.pop())
