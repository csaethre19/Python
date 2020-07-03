import numpy as np
import matplotlib.pyplot as plt

# f = lambda t: np.sin(t)
# t = np.linspace(0,5,500)
# plt.plot(t,f(t))
# plt.show()

f = input("Enter function: ")
ft = lambda t: eval(f)
l = np.array([])

for i in range(1,4):
    l = np.append(l, ft(i))
    i = i+1
print(l)
