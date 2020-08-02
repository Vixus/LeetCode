class MyHashSet:
    """
    Design a HashSet without using any built-in hash table libraries.

    To be specific, your design should include these functions:

    add(value): Insert a value into the HashSet. 
    contains(value) : Return whether the value exists in the HashSet or not.
    remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

    Example:

    MyHashSet hashSet = new MyHashSet();
    hashSet.add(1);         
    hashSet.add(2);         
    hashSet.contains(1);    // returns true
    hashSet.contains(3);    // returns false (not found)
    hashSet.add(2);          
    hashSet.contains(2);    // returns true
    hashSet.remove(2);          
    hashSet.contains(2);    // returns false (already removed)

    Note:

    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.
    """
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.hashSet = []

    # def add(self, key: int) -> None:
    #     if key not in self.hashSet:
    #         self.hashSet.append(key)

    # def remove(self, key: int) -> None:
    #     if key in self.hashSet:
    #         self.hashSet.remove(key)

    # def contains(self, key: int) -> bool:
    #     """
    #     Returns true if this set contains the specified element
    #     """
    #     if key in self.hashSet:
    #         return True
    #     else:
    #         return False
    
    # FASTER SOLUTION BUT MORE MEMORY
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = [False]*1000001

    def add(self, key: int) -> None:
        self.hashSet[key] = True

    def remove(self, key: int) -> None:
        self.hashSet[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hashSet[key]


def main():
    instrList = ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
    paramList = [[],[1],[2],[1],[3],[2],[2],[2],[2]]
    ans = []

    for i, instr in enumerate(instrList):
        if instr == 'add':
            obj.add(paramList[i][0])
            ans.append(None)
        elif instr == 'remove':
            obj.remove(paramList[i][0])
            ans.append(None)
        elif instr == 'contains':
            ans.append(obj.contains(paramList[i][0]))
        elif instr == 'MyHashSet':
            obj = MyHashSet()
            ans.append(None)

    print(ans)


if __name__ == '__main__':
    main()
