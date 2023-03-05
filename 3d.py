#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建x和y的网格
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算z和c的值
Z = -np.abs(Y)
C = Z / Z.min()

# 创建3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制表面图
surf = ax.plot_surface(X, Y, Z, facecolors=plt.cm.YlGn_r(C), linewidth=0)

# 显示图形
plt.show()
