# Define your "TreeNode" Python class below
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")

root.add_child(child)