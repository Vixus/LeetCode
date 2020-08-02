from Design_Hashset import MyHashSet


def test1():
    instrList = ["MyHashSet", "add", "add", "contains",
                 "contains", "add", "contains", "remove", "contains"]
    paramList = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    sol = [None, None, None, True, False, None, True, None, False]
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

    hashSol = [False]*1000001
    hashSol[1] = True
    assert ans == sol and obj.hashSet == hashSol
