import numpy as np
import matplotlib.pyplot as plt

# 計算結果の数値データを読み込み (*1)
npz = np.load("poisson.npz")
print(npz.files)  # 読み込んだデータの一覧を表示
phi = npz['phi']
Ex, Ey = npz['Ex'], npz['Ey']
x, y = npz['x'], npz['y']

# 2次元グリッドを生成 (*2)
xx, yy = np.meshgrid(x, y)  # yを固定してxを動かす2次元配列（[y, x]と表す）
print(f"xx.shape = {xx.shape}")  # (ny, nx)
print(f"yy.shape = {yy.shape}")  # (ny, nx)

# [x, y] から [y, x] に変換 (*3)
phi = phi.transpose()
Ex = Ex.transpose()
Ey = Ey.transpose()

# 配列のshapeがすべて一致しているか確認
assert xx.shape == yy.shape == phi.shape == Ex.shape == Ey.shape

# pcolormeshを使ってphiを図示 (*4)
fig, ax = plt.subplots()
im = ax.pcolormesh(xx, yy, phi, shading='nearest', cmap='OrRd')
# shading = 'nearest', 'gouraud'
ax.set_aspect(1)
fig.colorbar(im, ax=ax)
fig.savefig("phi_1.pdf")

# contourfを使ってphiを図示 (*5)
fig, ax = plt.subplots()
im = ax.contourf(xx, yy, phi, levels=20, cmap='OrRd')
ax.set_aspect(1)
fig.colorbar(im, ax=ax)
fig.savefig("phi_2.pdf")

# quiverを使って電場Eを図示（phiに重ねて描く） (*6)
fig, ax = plt.subplots()
im = ax.pcolormesh(xx, yy, phi, shading='nearest', cmap='OrRd')
ax.quiver(xx, yy, Ex, Ey)
ax.set_aspect(1)
fig.colorbar(im, ax=ax)
fig.savefig("elecfield_1.pdf")

# streamplotを使って電場Eを図示（phiに重ねて描く） (*7)
fig, ax = plt.subplots()
im = ax.pcolormesh(xx, yy, phi, shading='nearest', cmap='OrRd')
ax.streamplot(xx, yy, Ex, Ey, color='black', linewidth=1)
ax.set_aspect(1)
fig.colorbar(im, ax=ax)
fig.savefig("elecfield_2.pdf")
