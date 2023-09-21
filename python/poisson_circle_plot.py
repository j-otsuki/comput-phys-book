import numpy as np
import matplotlib.pyplot as plt

npz = np.load("poisson.npz")
print(npz.files)
phi = npz['phi']
Ex, Ey = npz['Ex'], npz['Ey']
x, y = npz['x'], npz['y']

# Make grid: [y, x] x runs first
xx, yy = np.meshgrid(x, y)
print(f"xx.shape = {xx.shape}")  # (ny, nx)
print(f"yy.shape = {yy.shape}")  # (ny, nx)

# [x, y] -> [y, x]
phi = phi.transpose()
Ex = Ex.transpose()
Ey = Ey.transpose()

# Check shapes
assert xx.shape == yy.shape == phi.shape == Ex.shape == Ey.shape

# plot E using quiver
fig, ax = plt.subplots(figsize=(8, 5))
im = ax.pcolormesh(xx, yy, phi, shading='nearest', cmap='OrRd')
ax.quiver(xx, yy, Ex, Ey)
ax.set_xlim(0.1, 1.0)
ax.set_ylim(0.2, 0.8)
ax.set_aspect(1)
ax.add_patch(plt.Circle((0.4, 0.5), 0.1, color='gray', lw=0, zorder=3))  # 円
fig.colorbar(im, ax=ax)
fig.savefig("elecfield_circle_1.pdf")

# plot E using streamplot
fig, ax = plt.subplots(figsize=(8, 5))
im = ax.pcolormesh(xx, yy, phi, shading='nearest', cmap='OrRd')
ax.streamplot(xx, yy, Ex, Ey, color='black', linewidth=1, density=3)
ax.set_xlim(0.1, 1.0)
ax.set_ylim(0.2, 0.8)
ax.set_aspect(1)
ax.add_patch(plt.Circle((0.4, 0.5), 0.1, color='gray', lw=0, zorder=3))  # 円
fig.colorbar(im, ax=ax)
fig.savefig("elecfield_circle_2.pdf")
