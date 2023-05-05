from math import exp

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[21], [52], [9], [7], [3], [12], [97], [55]])
y = np.array([41, 103, 17, 13, 8, 23, 193, 109])
reg = LinearRegression().fit(X, y)
print(reg.predict([[8]]))


x = [-2, -1, 0, 1, 2, 3, 4]
y = [-5, -3, -1, 1, 3, 5, 7]
w0 = w1 = 0
_w0 = _w1 = 0
alpha, data_len, check = 0.00001, len(x), 1
while check > 0.000001:
    for i in range(len(x)):
        check = 0
        check += (w0 + w1 * x[i] - y[i]) ** 2
        _w0 += (w0 + w1 * x[i] - y[i])
        _w1 += (w0 + w1 * x[i] - y[i]) * x[i]
    w0 -= alpha * 2 / data_len * _w0
    w1 -= alpha * 2 / data_len * _w1
print(w0 + 8*w1)
