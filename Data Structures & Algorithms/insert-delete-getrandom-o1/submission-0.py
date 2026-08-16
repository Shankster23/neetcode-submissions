class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.hash_map[val] = len(self.hash_map)
            self.arr.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            index = self.hash_map[val]
            last = self.arr[-1]
            self.arr[index] = last
            self.hash_map[last] = index
            self.arr.pop()
            del self.hash_map[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        import random
        return random.choice(self.arr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()