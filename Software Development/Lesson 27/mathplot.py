import matplotlib.pyplot as plt

xAxis = []
yAxis = []

for x in range(-100, 101):
    xAxis.append(x)
    yAxis.append((3 * x ** 6) + (5 * x ** 5) + (3 * x ** 4)+ (1 * x ** 3)+ (8 * x ** 2)+ (7 * x) + 1)

plt.plot(xAxis, yAxis)
 
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('First Graph!')
plt.grid(True)

plt.show()

