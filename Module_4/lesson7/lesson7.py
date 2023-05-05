# def decorator(func):
#     def wraper(*args, **kwargs):
#         check1 = list(map(lambda val: isinstance(val, (int, float)), args))
#         check2 = list(map(lambda val: type(val) == str and len(val) < 4, kwargs.values()))
#         print('Warning') if False in check2 + check1 else None
#         return func(*args, **kwargs)
#     return wraper
#
#
# @decorator
# def task(*args, **kwargs):
#     return args, kwargs
# a = bool()
#
# print(task(1, False, a=[True]))
import json
import time
import httpx
import yaml
from threading import Thread

res = httpx.get('https://jsonplaceholder.typicode.com/photos').json()

start = time.time()


def task1():
    with open('photos.json', 'w') as f:
        json.dump(res, f, indent=2)
        json.dump(res, f, indent=2)
        time.sleep(5)
    print('Task 1')


def task2():
    with open('photos.yml', 'w') as file:
        yaml.dump(res, file)
        yaml.dump(res, file)
    print('Task 2')


oqim_1 = Thread(target=task1)
oqim_2 = Thread(target=task2)

oqim_1.start()
oqim_2.start()

oqim_1.join()
oqim_2.join()

end = time.time()
print(end - start)
