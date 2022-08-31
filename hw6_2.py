global num
global x
global left
global right
global deep
class Node():
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
    def deep_count_left(self,data):
        if self.left:
            data = self.left.deep_count_left(data)
        return data + 1
    def deep_count_right(self,data):
        if self.right:
            data = self.right.deep_count_right(data)
        return data + 1
num = 0
x = 0
left = 0
right = 0
deep = 0
tree = Node()
datas = [10,21,5,9,13,28]
for d in datas:
    tree.insert(d)
tree.postorder()
left = tree.deep_count_left(left)
right = tree.deep_count_right(right)
if left > right:
    deep = left
else:
    deep = right
print("深度為: %d"%deep)
