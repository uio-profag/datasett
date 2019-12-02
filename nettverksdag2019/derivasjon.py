def f(x):
    return x

def fder(f, x, dx=1E-8):
    der = (f(x + dx) - f(x))/dx
    return der

print(fder(f,1))