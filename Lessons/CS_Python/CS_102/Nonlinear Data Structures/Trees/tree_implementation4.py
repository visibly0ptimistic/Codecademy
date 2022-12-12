# Define your "TreeNode" Python class below
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children 
                    if child is not child_node]
    
    def traverse(self):
        print(self.value)
        for node in self.children:
            print(node.value)

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")

root.add_child(first_child)
root.add_child(second_child)

root.traverse()