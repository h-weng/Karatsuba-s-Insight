"""

    Karatsuba's Insight
    ===================
    
    To compute x * y we divide into 3 subproblems:

        a = x.l y.l 
        d = x.r y.r
        e = (x.l + x.r)(y.l + y.r) - a - d
        xy = ar^n + er^(n/2) + d

    Computation time:
    
        T(n) = 3T(n/2) + O(n)

"""

def karatsuba(x,y):
    
    xs = str(x) 
    ys = str(y)
    lx = len(xs)
    ly = len(ys)

    if lx == 1 and ly == 1:
        return x * y

    m = max(lx, ly)
    xs = '0' * (m - lx) + xs
    ys = '0' * (m - ly) + ys

    n1 = (m + 1)//2
    n2 = m//2

    xl = int(xs[:n1])
    xr = int(xs[n1:])

    yl = int(ys[:n1])
    yr = int(ys[n1:])

    a = karatsuba(xl, yl)
    d = karatsuba(xr, yr)
    e = karatsuba(xl + xr, yl + yr) - a - d

    return a * 10**(2*n2) + e * 10**n2 + d

value = karatsuba(1234, 5678)
print(value)
