class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        return None

    def min(self):
        return self.min_stack[-1] if self.min_stack else None
