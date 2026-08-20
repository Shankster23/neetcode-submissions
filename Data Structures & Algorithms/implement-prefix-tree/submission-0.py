class PrefixTree:

    def __init__(self):
        self.hash_set = set()
        self.prefix_set = set()
        

    def insert(self, word: str) -> None:
        self.hash_set.add(word)
        counter_str = ""
        for w in word:
            counter_str += w
            self.prefix_set.add(counter_str)
        
        


    def search(self, word: str) -> bool:
        return word in self.hash_set

        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_set
        
        