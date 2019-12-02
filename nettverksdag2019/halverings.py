def f(x):
    return 2*x + 1

a = -10
b = 5
m = (a+b)/2
tol = 1E-16

while abs(f(m)) > tol:
    if f(a)*f(m) < 0:
        b = m
    elif f(b)*f(m) < 0:
        a = m
    m = (a+b)/2

print("Nullpunktet:", m)
        
        
        
        
        