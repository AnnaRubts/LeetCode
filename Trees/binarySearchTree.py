# created a BST from a sorted array
from Tree import Node

def sortedArrayToBST(array):
    if len(array)==1:
        return Node(array[0])
    if len(array)==0:
        return None
    
    middle = len(array)//2
    return Node(array[middle], sortedArrayToBST(array[:middle]), sortedArrayToBST(array[middle+1:]))

def print_tree(node, level=0):
    if node is not None:
        # First, print the right subtree with increased indentation.
        print_tree(node.right, level + 1)
        # Print the current node with indentation corresponding to its level.
        print(' ' * 4 * level + '-> ' + str(node.val))
        # Then, print the left subtree.
        print_tree(node.left, level + 1)


if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8]
    root = sortedArrayToBST(array)
    print_tree(root)