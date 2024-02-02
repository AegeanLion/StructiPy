class BinaryNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def leaves(self):
        return 
    
    def insert(self, val=None, current_node=self.root):
        appended_node = BinaryNode(val)
        
        if appended_node.val:
            if current_node == None or current_node.val == None:
                current_node = appended_node:
                return
            elif appended_node.val > current_node.val:
                if current_node.right == None:
                    current_node.right = appended_node
                else:
                    self.insert(val, current_node.right)
                    
            elif appended_node.val < current_node.val:
                if current_node.left == None:
                    current_node.left = appended_node
                else:
                    self.insert(val, current_node.left)
        return 
    
    def size(self):
        return 
    
    def node_level(self, node):
        return 
    
    def height(self):
        return 
    
    def display(self, node):
        return 

    
def bfs():
    return

def dfs():
    return
