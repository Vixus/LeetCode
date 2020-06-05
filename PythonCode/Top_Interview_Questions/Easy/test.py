from collections import defaultdict
import numpy as np

input = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"]
]

a = np.matrix(input)

print('10' in a)

# import inspect


# def decorator_wrapper(parameter):
#     print(parameter)

#     def decorator(func):
#         def wrapper(message):
#             print("Wrapper start")
#             func(message)
#             print("Wrapper end")

#         return wrapper

#     return decorator


# # Here, instead of having the decorator function object as in prevision cases,
# # we are executing the decorator_wrapper function using the round brackets which returns the
# # decorator function. So ultimately the code changes to
# '''
# decorator = decorator_wrapper("Decorator paramerter")
# @decorator
# def say_hello(message):
#     print message
# '''
# @decorator_wrapper("Decorator parameter")
# def say_hello(message):
#     print(message)


# # print inspect.getsource(say_hello)
# '''
#     def wrapper(message):
#         print "Wrapper start"
#         func(message)
#         print "Wrapper end"
# '''

# say_hello("Hello, world")
