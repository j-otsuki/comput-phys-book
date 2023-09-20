import numpy as np
from scipy.integrate import solve_ivp
from differential import make_differential_ops  # differential.pyから関数をインポート

# シュレディンガー方程式
# u_{t} = -i [ -(1/2) u_{xx} + v u ]
def func_schr(t, u, df2, v):
    return -1.0j * (-0.5 * (df2 @ u) + v * u)  # (*1)

# 1次元シュレディンガー方程式を解く関数
def solve_schr(x_array, t_array, u0, v, basename='schr'):
    assert x_array.size == u0.size == v.size  # データサイズを確認 (*2)
    assert u0.dtype == complex  # データ型を確認

    print("Solve Schroedinger equation")
    print("x: (min, max, n) =", (x_array[0], x_array[-1], x_array.size))
    print("t: (min, max, n) =", (t_array[0], t_array[-1], t_array.size))

    dx = x_array[1] - x_array[0]
    print(f"dx = {dx:.8g}")
    _, op_df2, _ = make_differential_ops(x_array.size, dx)  # 差分行列D^2

    # 方程式を解く
    t_span = (t_array[0], t_array[-1])
    args = (op_df2, v)
    sol = solve_ivp(func_schr, t_span, u0, dense_output=True, args=args, rtol=1e-8)  # (*3)
    print(sol.message)
    print(" Number of time steps :", sol.t.size)  # 時間ステップ数
    print(" minimum time step    :", np.diff(sol.t).min())  # 最小時間刻み
    print(" Maximum time step    :", np.diff(sol.t).max())  # 最大時間刻み

    # 結果を取得（dense output）
    u_xt = sol.sol(t_array)  # u(x, t)
    u_tx = u_xt.T  # u(t, x)
    assert u_tx.shape == (t_array.size, x_array.size)

    # 結果をファイルに保存
    np.savez(basename, x=x_array, t=t_array, u_tx=u_tx, v=v)
    print(f"Saved into '{basename}.npz'")
