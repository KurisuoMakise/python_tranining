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
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def printed(self,num):
        if self.left:
            self.left.printed(num)
        if self.right:
            self.right.printed(num)
        if not self.left:
            if not self.right:
                num = num + 1
num = 0
tree = Node()
datas = [10,5,21,9,13,28,3,4,1,17,32]
for d in datas:
    tree.insert(d)
tree.preorder()
tree.printed(num)
print("節點數量: %d"%num)