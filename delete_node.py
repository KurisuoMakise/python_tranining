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
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
class Delete_Node():
    def deleteNode(self,root,key):
        if root is None:
            return None
        if key < root.data:
            root.left = self.deleteNode(root.left,key)
            return root
        if key > root.data:
            root.right = self.deleteNode(root.right,key)
            return root
        if root.left is None:
            new_root = root.right
            return new_root
        if root.right is None:
            new_root = root.left
            return new_root
        succ = self.max_node(root.left)
        tmp = Node(succ.data)
        tmp.left = self.left_node(root.left)
        tmp.right = root.right
        return tmp
    def left_node(self,node):
        if node.right is None:
            new_root = node.left
            return new_root
        node.right = self.left_node(node.right)
        return node
    def max_node(self,node):
        while node.right:
            node = node.right
        return node



tree = Node()
datas = [10,5,21,9,13,28,3,4,1,17,32]
for d in datas:
    tree.insert(d)
tree.inorder()
del_data = 5
print("刪除 %d 資料以後"%del_data)
delete_obj = Delete_Node()
result = delete_obj.deleteNode(tree,del_data)
result.inorder()
