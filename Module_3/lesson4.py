from collections import deque

# def my_func(get_list: list, n: int) -> list:
#     start = len(get_list) * int(not n > 0)
#     end = -1 * int(n > 0)
#     return [get_list[1:start] + [get_list[0]] if start else [get_list[end]] + get_list[:end] for _ in range(abs(n))][0]

# class Deque(list):
#     def __init__(self, get_list):
#         super().__init__()
#         self.get_list = get_list
#
#     def my_deque(self, n: int) -> None:
#         start = len(self.get_list) * int(not n > 0)
#         end = -1 * int(n > 0)
#         for i in range(abs(n)):
#             self.get_list.insert(start, self.get_list[end])
#             self.get_list.pop(end)
#
#     def extend_left(self, get_val: Iterable) -> None:
#         add = [type(get_val)(get_val)] + list(get_val)
#         self.get_list[0:] = get_val
#
#     def append_left(self, get_val: Iterable) -> None:
#         add = [type(get_val)(get_val)] + list(get_val)
#         self.get_list = type(add)(add)
# print(my_func([1, 2, 3], -9))


#

from itertools import chain
from typing import Iterable

# def adder(*args: list) -> list:
#     return [(lambda *val: val)(*i) for i in args]
#
#
# print(adder([1, 2, 3], [4, 8, 78]))
#
# k = [1, 2, 3]
# print(*k)


matrix = [
    [1, 2, 3],
    [4, 5, 6, 7, 8],
    [7, 8, 9, 2],
]


def my_func(get_list: list, fillval=None) -> list:
    return list(zip(*map(lambda val: val + [fillval] * (len(max(get_list, key=len)) - len(val)), get_list)))


for i in my_func(matrix, 15):
    print(i)
