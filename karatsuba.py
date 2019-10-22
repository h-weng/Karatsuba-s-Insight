"""Karatsuba's Insight"""

"""
    To compute x * y
    
    We divide into 3 subproblems (this is the standard formula):

    a = x.l y.l 
    d = x.r y.r
    e = (x.l + x.r)(y.l + y.r) - a - d
    xy = ar^n + er^(n/2) + d

    T(n) = 3T(n/2) + O(n)

"""

def karatsuba(x, y):
    """convert to string to enumerate the indexes for the digits"""
    xs = str(x) 
    ys = str(y)

    if len(xs) == 1 and len(ys) == 1:
        return int(xs) * int(ys)

    n2 = len(xs)
    n1 = n2//2 

    """divide evenly number of digits: x on right, and x on the left"""
    xl = int(xs[:n1])
    xr = int(xs[n1:])

    yl = int(ys[:n1])
    yr = int(ys[n1:])

    a = karatsuba(xl, yl)
    d = karatsuba(xr, yr)
    k = karatsuba(xl + xr, yl + yr)
    e = k - a - d
    return a * 10**n2 + e * 10**n1 + d

value = karatsuba(num1, num2)
print(value)
