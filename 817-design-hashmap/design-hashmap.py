class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = []
        for i in range(self.size):
            self.buckets.append([])

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        list1 = self.buckets[index]
        for data in list1:
            if data[0] == key:
                data[1] = value
                return
        list1.append([key, value])

    def get(self, key: int) -> int:
        index = key % self.size
        list1 = self.buckets[index]
        for data in list1:
            if data[0] == key:
                return data[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        list1 = self.buckets[index]
        for i in range(len(list1)):
            if list1[i][0] == key:
                list1.pop(i)
                return

'''
 Keys that are exactly 1000 apart (like 5 and 2005) collide into the same bucket

# WHY 1000 BUCKETS (space vs time tradeoff):
# One big list (no hash): O(n) space, O(n) time per op — scans everything
# 1000 buckets (this):    O(1000+n) space, O(n/1000) avg time — scans ~1 bucket

# Hashing spends a small fixed amount of extra memory (1000 empty lists)
# to get average O(1) lookups instead of O(n). Worth it once n is large
# - "Average case O(1), worst case O(n) if everything collides into one bucket"
# - "This trades space (1000 fixed slots) for speed (avoiding a full scan)"
'''
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

