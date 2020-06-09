from collections import defaultdict
import numpy as np

a = '423'
print(int('+3434'))
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
