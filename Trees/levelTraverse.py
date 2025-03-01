# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

def levelTraverse(root):
    queue = deque()
    if root:
        queue.append(root)
    
    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


from Tree import Node
from binarySearchTree import print_tree

if __name__ == "__main__":
    root = Node(1, Node(2, Node(4, Node(8)), Node(5, None)), Node(3, Node(6, None), Node(7, None))) 
    print_tree(root)

    levelTraverse(root)