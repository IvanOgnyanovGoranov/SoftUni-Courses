class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last_element = self.data.pop()
        return last_element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"


s = Stack()
s.push('1')
s.push('2')
print(s)
print(s.pop())
