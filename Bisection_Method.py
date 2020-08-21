import math
import matplotlib.pyplot as plt
import numpy as np
y = str(input("enter an equation in terms of x\t"))
func = lambda x: eval(y)
def bisection(x, y, z):
    if (func(x) * func(y) >= 0):
        print("You have not assumed right\n")
        return
    A = np.linspace(x, y, 1000000)
    B = [func(i) for i in A]
    plt.plot(A, B, label='function')
    t = x
    while True:
        t = (x + y) / 2
        if (func(t) == 0.0 or abs(func(t)) < z):
            plt.scatter(t, func(t), color = 'r', label=f'solution: {t}')
            break
        if (func(t) * func(x) < 0):
            y = t
        else:
            x = t
    print("The value of root is: ", t)
    plt.legend()
    plt.show()
a = float(input("enter A point\t"))
b = float(input("enter B point\t"))
c = float(input("enter tolerance\t"))
bisection(a, b, c)
