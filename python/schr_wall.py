import numpy as np
from schr import solve_schr  # schr.pyから関数solve_schrをインポート

# x座標
x_min, x_max = -50.0, 50.0
nx = 1000
x = np.linspace(x_min, x_max, nx, endpoint=False)

# 初期条件
k = 4
x0 = -20.0
delta = 4.0
u0 = np.exp(1.0j * k * x - 0.5 * ((x-x0) / delta)**2)  # (*1)
dx = x[1] - x[0]
integ = np.sum(np.absolute(u0)**2) * dx  # 積分 (*2)
u0 /= np.sqrt(integ)  # 規格化
assert u0.shape == (nx,)  # u0が想定通りのshapeになっているか確認

# ポテンシャル
v_height = 10.0
width = 1.0
v = np.where(np.abs(x)<width, v_height, 0)  # (*3)
assert v.shape == (nx,)  # vが想定通りのshapeになっているか確認

# 時刻tの配列（動画作成用）
t_max = 16.0
nt = 81
t = np.linspace(0, t_max, nt)

# solve equation
solve_schr(x, t, u0, v, basename='schr')
