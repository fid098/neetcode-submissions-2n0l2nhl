class PrefixTree:
    #think of tries as a nested dictionary
    #bin: b:{i:{n:{.:.}}}
    #
    #
    def __init__(self):
        self.trie = {} #initialise the dictionary

    def insert(self, word: str) -> None:
        d = self.trie 
        for char in word:
            if char not in d:
                d[char] = {} #create a new dictionary
            d = d[char] #move into the inside dictionary
        d['.'] = '.'  #this is the end of the word

    def search(self, word: str) -> bool:
        d = self.trie 
        for char in word:   
            if char not in d:  #if the char is not in the dictionary
                return False
            d = d[char]
        return '.' in d  #if we keep going to the end of the word and . is the end
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie 
        for char in prefix:   
            if char not in d:  #if the char is not in the dictionary
                return False
            d = d[char]
        return True
        