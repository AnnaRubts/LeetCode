from Trie import Trie

# given prefixes list and words list, check if there is a prefix matching one of the words

def check_prefix_match(prefixes, words):
    myTrie = Trie()
    for prefix in prefixes:
        myTrie.add_prefix(prefix)
    
    for word in words:
        if myTrie.search_matching_prefix(word):
            return True
    
    return False

if __name__ == "__main__":
    prefixes = ["ab", "co", "dad"]
    words = ["a", "walla", "mom", "car"]
    print(check_prefix_match(prefixes, words)) #should return False
    words.append("daddy")
    print(check_prefix_match(prefixes, words)) #should return True
    