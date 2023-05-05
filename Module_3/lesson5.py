# from itertools import groupby
#
# s = 'hellllllo worrrrld'
# res = (list(s) for l, s in groupby(s))
# print(len(max(sorted(groupby(s), key=lambda val: -len(list(val[1]))), key=len)))
#
# for v in groupby(s):
#     print(list(v[1]))
#
# print(sorted(list(groupby(s)), key=lambda val: len(list(val[1])), reverse=True))

# a = [1, 7, 9, 19]
# b = [2, 3, 8, 9, 11, 20]
# print(a.pop(2))
# for i in range(len(b)):
#     for j in range(len(a)-1):
#         if a[j] < b[i] <= a[j + 1]:
#             a.insert(j+1, b[i])
#             break
#     else:
#         a.insert(len(a)*(b[i] > a[0]), b[i])
# print(a)


# time = "2?:0?"
# keys = [2, 3, 5, 9]
# time = time.split(':')
# hour = time[0]
# minutes = time[1]
# if hour[0] == '2':
#     hour = hour.replace('?', '3')
# elif hour[0] == '1' == '0':
#     hour = hour.replace('?', '9')
# else:
#     hour = hour.replace('?', '2')
#
# minutes = minutes.replace('?', '5' if minutes[0] == '?' else '9')
#
# print(hour, minutes)




