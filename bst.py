class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert_bst(self,value):
        if self.root == None :
            self.root = Node(value)
        else :
            self._insert(value,self.root)

    def _insert(self,value,current_node):
        if value < current_node.value :
            if current_node.left == None :
                current_node.left = Node(value)
            else :
                self._insert(value,current_node.left)
        elif value > current_node.value:
            if current_node.right == None :
                current_node.right = Node(value)
            else :
                self._insert(value,current_node.right)
        else :
            print('Sorry! the value is already present in the Binary search Tree')

    def search(self,value):
        pass

    def pre_print(self):
        if self.root == None:
            print('Empty Tree')
        else :
            return self._pre_print(self.root,"")

    def _pre_print(self,presentnode,traversal):
        if presentnode:
            traversal += (str(presentnode.value)+' ')
            traversal = self._pre_print(presentnode.left,traversal)
            traversal = self._pre_print(presentnode.right,traversal)
        return traversal



tree = binary_search_tree()

tree.insert_bst(2)
tree.insert_bst(12)
tree.insert_bst(3)
tree.insert_bst(1)
tree.insert_bst(11)
print(tree.pre_print())