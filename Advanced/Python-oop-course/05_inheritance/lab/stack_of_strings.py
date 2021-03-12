class Stack(str):
    def __init__(self):
        super(Stack, self).__init__()
        self.data = []

    def __str__(self):
        return f"[{', '.join(item for item in reversed(self.data))}]"

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return self.data == []


# Test code
random_stack = Stack()
random_stack.push('something')
random_stack.push('notpop')
random_stack.push('pop')
print(random_stack)
print(random_stack.pop())
print(random_stack.peek())
print(random_stack.is_empty())
print(random_stack)
