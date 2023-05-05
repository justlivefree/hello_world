from itertools import combinations

# def rec(s: str):
#     if s == '':
#         return ''
#     if not (']' in s):
#         return s
#     c = int(s[0])
#     start = s.index('[')
#     end = s.index(']')
#     return c*s[start+1:end] + rec(s[end+1:])
#
# print(rec("3[a2[c]]"))