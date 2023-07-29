import numpy as np


def strassen(u, v):
    if u.size == 1 or v.size == 1:
        return u * v

    s = u.shape[0]

    if s % 2 == 1:
        u = np.pad(u, (0, 1), mode='constant')
        v = np.pad(v, (0, 1), mode='constant')

    r = int(np.ceil(s / 2))
    a = u[: r, : r]
    b = u[: r, r:]
    c = u[r:, : r]
    d = u[r:, r:]
    e = v[: r, : r]
    f = v[: r, r:]
    g = v[r:, : r]
    h = v[r:, r:]
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)
    ans = np.zeros((2 * r, 2 * r), dtype=np.int32)
    ans[: r, : r] = p5 + p4 - p2 + p6
    ans[: r, r:] = p1 + p2
    ans[r:, : r] = p3 + p4
    ans[r:, r:] = p1 + p5 - p3 - p7

    return ans[: s, : s]


x= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
y= np.array([[16,15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]]) 
print(strassen(x, y))