# #103 - Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).

from collections import deque

def zigzagTraverse(root):
    levels_q = deque()
    levels_q.append([root])
    left = True

    while(levels_q):
        curr_level = levels_q.popleft()
        if left:
            for node in curr_level:
                print(node.val)
        else:
            for i in range(len(curr_level)-1, -1,-1):
                print(curr_level[i].val)
        left = not left
        
        level = []
        for node in curr_level:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        if level: 
            levels_q.append(level)

from Tree import Node
from binarySearchTree import print_tree

if __name__ == "__main__":
    root = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5, None)), Node(3, Node(6, None), Node(7, None))) 
    print_tree(root)

    zigzagTraverse(root)