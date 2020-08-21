import math
import matplotlib.pyplot as plt
import numpy as np

func = lambda x: eval(y)

def regulaFalsi(a, b, e):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1
    A = np.linspace(a, b, 1000000)
    B = [func(i) for i in A]
    plt.plot(A, B, label='function')
    while(True):
        c = (a * func(b) - b * func(a))/ (func(b) - func(a))
        if func(c) == 0 or abs(func(c)) < e:
            plt.scatter(c, func(c), color='r', label=f'solution is: {c}')
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print(f'root is: {c}')
    plt.legend()
    plt.show()

y = str(input("enter the equation:\t"))
a = float(input("enter the A element:\t"))
b = float(input("enter the A element:\t"))
e = float(input("enter the tolerance:\t"))

regulaFalsi(a, b, e)

