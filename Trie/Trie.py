# The Trie data structure is a tree-like data structure used for storing a dynamic set of strings.
# In this implementation I assumed I store prfixes i the Trie, and can check if a given word match some saved prefix

class TrieNode:
    def __init__(self):
        self.children = {} #dict will contain (key-value : val-TrieNode)
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_prefix(self, prefix):
        curr_node = self.root
        for c in prefix:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.is_end = True
    
    def search_matching_prefix(self, word):
        curr_node = self.root
        for c in word:
            if curr_node.is_end:
                return True
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                #print ("No matching prefix")
                return False
        if curr_node.is_end:
            return True
        else:
            #print ("No matching prefix")
            return False
