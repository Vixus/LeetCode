from collections import defaultdict
from collections import Counter
import numpy as np
from Tools.TreeFunctions import treeToArr, arrToTree

a = [1, 2, 3]
b = [4, 5, 2]

for x in b:
    if x in a:
        print(x)


"""
sentence = 'The rocket, who was named Ted, came back'
vowels = 'aeiou'
Arr = []


def f(x):
    if x.isalpha() and x.lower() not in Arr:
        Arr.append(x.lower())
    return x.lower()


ans = [f(x) for x in sentence if x not in Arr]
print(ans)
"""

"""
a = [1, 2, 3, 4]


def bla(a):
    # a.append(5)
    a = [1,2,3,4,5]
    print(a)


bla(a)
print(a)

x = 0


def add(x):
    x += 1
    print(x)


add(x)
print(x)
"""

# def try_to_change_list_reference(the_list):
#     print('got', the_list)
#     the_list = ['and', 'we', 'can', 'not', 'lie']
#     print('set to', the_list)


# outer_list = ['we', 'like', 'proper', 'English']

# print('before, outer_list =', outer_list)
# try_to_change_list_reference(outer_list)
# print('after, outer_list =', outer_list)
# print('hede')
# a = [4,5,6]

# A = [10, -2, -5, -4, -8, 9, 8, -20, 7, 6, 3, -1]
# A = [1, 2]
# print(len(A))
# print(list(range(-1, -len(A), -1)))

# a_list = ["a4cd", "12345", "argument", "a", "2"]
# output = [idx for idx, element in enumerate(a_list) if len(element) > 4]
# print(output)

# print(sum(A))
# print(list(range(3)) + list(range(5)))
# a = 'a'
# b = 'b'
# c = '4210'

# if a[0] == 'a' or a[1] == 'b':
#     print('True')
# else:
#     print('False')

# a = 'jhgjh', 'jhgjg', 'kjhkh'
# print(a)
# print(f'asfsf {c} asd')
# print(a+b)
# print(c.index(min(c)))
# print(c[1:])
# print(1e10)
# print(sys.)

# e = [None]*6
# print(ord('a')-97)
# print(e[0])
# if None:
#     print("hello")

# print(list(enumerate('abc')))
# d = [1, 2, 3, 4, 5]
# print(d[3])
# print([None]*26)

# for x in range(0):
#     print("hello")
#     print(range(0))

# numList = [0, 1, 2]
# engList = ['zero', 'one', 'two']
# espList = ['cero', 'uno', 'dos']

# Eng = list(zip(engList, espList, numList))
# Eng.sort()  # sort by engList
# print(Eng)
# a, b, c = zip(*Eng)

# print(a)
