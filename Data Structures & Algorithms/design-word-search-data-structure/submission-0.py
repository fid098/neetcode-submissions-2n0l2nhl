class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
        d['.'] = '.'
        
    def search(self, word: str) -> bool:
        d = self.trie
        #we want to search each node from each letter
        def dfs(node, i):
            #if we are at the end of the word
            if i == len(word):
                return '.' in node

            #char for the each word
            char = word[i]

            if char == '.':
                #loop through the node
                for child in node:
                    #if the child is not . and the next value is in the trie
                    if child != '.' and dfs(node[child], i + 1):
                        return True 
                return False
            else:
                if char not in node:
                    return False
                return dfs(node[char], i + 1)
        return dfs(d, 0)
        
