import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.exp(np.sin(2 * x))
def df(x):
    return 2 * np.exp(np.sin(2 * x)) * np.cos(2 * x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = f(x)
x_tangent = np.pi / 4
y_tangent = f(x_tangent)
slope = df(x_tangent)
b = y_tangent - slope * x_tangent
tangent_line = slope * x + b
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = e^(sin(2x))', color='blue')
plt.plot(x, tangent_line, label='Касательная', color='red', linestyle='--')
plt.scatter(x_tangent, y_tangent, color='green')
plt.text(x_tangent, y_tangent, f'({x_tangent:.2f}, {y_tangent:.2f})', fontsize=10, verticalalignment='bottom')
plt.title('График функции e^(sin(2x)) с одной из касательных и одной из точек касания')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
