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


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

