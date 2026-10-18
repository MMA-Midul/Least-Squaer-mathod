import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
n = len(x)

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)


a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - a * sum_x) / n


print(f"Slope (a): {a:.2f}")
print(f"Intercept (b): {b:.2f}")


y_pred = a * x + b


plt.scatter(x, y, color="red", label="Data points")
plt.plot(x, y_pred, color="blue", label="Best fit line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Least Squares Regression")
plt.legend()
plt.show() 