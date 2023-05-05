import random
import time

# lst, tpl = [], []
# for _ in range(1000):
#     lst.append(random.randint(1, 100))
#     tpl.append(random.randint(1, 100))
# tpl = tuple(tpl)
#
#
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end - start)
#     return wrapper
#
#
# @timer
# def summa_lst():
#     summa = 0
#     for i in lst:
#         summa += i
#     print(summa)
#
#
# @timer
# def summa_tpl():
#     summa = 0
#     for i in tpl:
#         summa += i
#     print(summa)
#
#
# summa_lst()
# print('-------------------')
# summa_tpl()
#
#
# def dec(function):
#     def wrapper():
#         func = function()
#         uppc = func.upper()
#         return uppc
#     return wrapper()
#
#
# def my_func():
#     return 'My func'
#
# res = dec(my_func)
#
# print(res)


# def dec(func):
#     def wrapper(wrd: str) -> str:
#         return str(int(wrd) + 1) if wrd.isnumeric() else wrd + '1'
#
#     return wrapper
#
#
# @dec
# def my_func(word: str) -> str:
#     return word
#
#
# word = '489468'
#
# print(my_func(word))


# def dec(doubled=1):
#     def inside(func):
#         def wrapper(a, b):
#             func(a * doubled, b * doubled)
#
#         return wrapper
#
#     return inside
#
#
# @dec()
# def my_func(a, b):
#     print(a, b)
#
#
# my_func(1, 2)
from typing import Any


# def dec(*, upper=False, lower=False, to_type=None, reversed=False):
#     def inside(func):
#         def wrapper(word):
#             if upper:
#                 return func(word.upper())
#             if lower:
#                 return func(word.lower())
#             if to_type is not None:
#                 try:
#                     return to_type(func(word))
#                 except TypeError:
#                     print("ERROR")
#             if reversed:
#                 return func(word[::-1])
#
#         return wrapper
#
#     return inside
#
#
# @dec()
# def my_func(word):
#     return word
#
#
# print(my_func('123'))

import re

s = 'sal448|o4869985|8987dew|864'
res = max(map(lambda val: len(re.sub('[A-Za-z]+', '', val)), s.split('|')[1:-1]))
print(res)


phone_no = '(212)-456-7890'
pattern = '2'
result = phone_no.replace(pattern, '')

print(result)

pattern = re.compile("[A-Za-z0-9]+")
pattern.fullmatch(phone_no)