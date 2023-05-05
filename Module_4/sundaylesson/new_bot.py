import time
from itertools import cycle

t = 0
for i in cycle([1]):
    time.sleep(.5)
    t += i
    print(t)
