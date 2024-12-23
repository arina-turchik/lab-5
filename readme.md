# Лабораторная работа №5
## Задача
### Разобраться в работе с библиотеками `matploitlib` и `numpy`
## Ход работы
1. Понять алгоритм работы с `matplotlib`,`numpy` и виртуальным окружением. Установить библиотеки, нужные для работы.
2. Выполнить уроки 1-3 в [книге](https://evil-teacher.on-fleek.app/books/prog_pm/matplotlib.pdf).
3. Написать программу, рисующую график к непрерывной функции из Лаб. Работы №2.
4. Переместить в репозиторий на `gihub` результаты работы.

## Работа с книгой

```
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,2,3,4,5])
plt.show()
```
<image src = Figure_1.png alt="1">

```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = x
plt.title('Линейная зависимость y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()      
plt.plot(x, y)
plt.show()
```
<image src = Figure_2.png alt="2">

```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x 
y2 = [i**2 for i in x]
plt.title('Зависимость: y1 = x, y2 = x^2')
plt.xlabel('x')
plt.ylabel('y1, y2')
plt.grid()
plt.plot(x, y1, x, y2)
plt.show()
```
<image src = Figure_3.png alt="3">

```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x
y2 = [i**2 for i in x]
plt.figure(figsize=(9, 9))
plt.subplot(2, 1, 1)
plt.plot(x, y1)          
plt.title('Зависимости: y1 = x, y2 = x^2')
plt.ylabel('y1', fontsize=14)
plt.grid(True)
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.xlabel('x', fontsize=14)
plt.ylabel('y2', fontsize=14)
plt.grid(True)         
plt.show()
```
<image src = Figure_4.png alt="4">

```
import matplotlib.pyplot as plt

fruits = ['apple', 'peach', 'orange', 'bannana', 'melon']
counts = [34, 25, 43, 31, 17]
plt.bar(fruits, counts)
plt.title('Fruits!')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```
<image src = Figure_5.png alt="5">

```
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, label = 'steel price')
plt.xlabel('Day', fontsize=15, color='blue')
plt.title('График', fontsize=17)
plt.ylabel('Price', fontsize=15, color='blue')
plt.legend()
plt.grid(True)
plt.text(15, 4, 'grow up!')
plt.show()
```
<image src = Figure_6.png alt="6">

```
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, '--r')
plt.show()
```
<image src = Figure_7.png alt="7">

```
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.figure(figsize=(12, 7))
plt.subplot(2, 2, 1)
plt.plot(x, y1, '-')
plt.subplot(2, 2, 2)
plt.plot(x, y2, '--')
plt.subplot(2, 2, 3)
plt.plot(x, y3, '-.')
plt.subplot(2, 2, 4)
plt.plot(x, y4, ':')
plt.show()
```
<image src = Figure_8.png alt="8">

```
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.', x, y4, ':')
plt.show()
```
<image src = Figure_9.png alt="9">

```
import matplotlib.pyplot as plt

locs = ['best', 'upper right', 'upper left', 'lower left',
'lower right', 'right', 'center left', 'center right',
'lower center', 'upper center', 'center']
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]
plt.figure(figsize=(12, 12))
for i in range(3):
    for j in range(4):
        if i*4+j < 11:
           plt.subplot(3, 4, i*4+j+1)
           plt.title(locs[i*4+j])
           plt.plot(x, y1, 'o-r', label='line 1')
           plt.plot(x, y2, 'o-.g', label='line 2')
           plt.legend(loc=locs[i*4+j])
        else:
            break
plt.show()
```
<image src = Figure_10.png alt="10">

## Работа с непрерывной функцией моего варианта (9) из лабораторной работы №2
```
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
```
<image src = Figure_myvar.png alt="myvar">

## Источники

1. [evil-teacher](https://evil-teacher.on-fleek.app/prog_pm/term1/lab05/)
2. [Devpractice Team. Библиотека Matplotlib](https://evil-teacher.on-fleek.app/books/prog_pm/matplotlib.pdf)
