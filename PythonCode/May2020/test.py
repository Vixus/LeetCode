a = 'a'
b = 'b'
c = '4210'

if a[0] == 'a' or a[1] == 'b':
    print('True')
else:
    print('False')

a = 'jhgjh', 'jhgjg', 'kjhkh'
print(a)
print(f'asfsf {c} asd')
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

numList = [0, 1, 2]
engList = ['zero', 'one', 'two']
espList = ['cero', 'uno', 'dos']

Eng = list(zip(engList, espList, numList))
Eng.sort()  # sort by engList
print(Eng)
a, b, c = zip(*Eng)

print(a)
