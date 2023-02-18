import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y, z = 0.10, 0.2, 0.10
rho = 28
sigma = 10
beta = 8 / 3
# scale = 1 # scale of attractor 
time = 0.01 # time ttaken to draw 
# print(f"{sigma * (y - x)}  {x * (rho - z) - y } {x * y - beta * z}")
i = 0
lx = []
ly = []
lz = []
while 1:
    # equations
    dx = (sigma * (y - x)) * time
    dy = (x * (rho - z) - y) * time
    dz = (x * y - beta * z) * time

    x = x + dx
    y = y + dy
    z = z + dz
    # print(f"x={x} , y={y} , z={z}")

    lx.append(x)
    ly.append(y)
    lz.append(z)
    i= i+1
    if i == 10000:
        break
# print(lx)
# print(ly)
# print(lz)


# Prepare data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 4, 5, 6]
# z = [3, 4, 5, 6, 7]

# Create a 3D plot
fig = plt.figure(figsize=(10 , 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(lx, ly, lz )

# Show plot
plt.show()