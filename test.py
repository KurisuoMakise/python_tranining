class Stack():
    def __init__(self):
        self.my_stack = []
    def my_push(self,data):
        self.my_stack.append(data)
    def my_pop(self):
        return self.my_stack.pop()
    def size(self):
        return len(self.my_stack)
    def isEmpty(self):
        return self.my_stack == []
    def get(self):
        if len(self.my_stack) == 0:
            return 0
        return self.my_stack[(len(self.my_stack) - 1)]

stack = Stack()
stack.my_push("Apple")
stack.my_push("Logitech")
print(stack.get())