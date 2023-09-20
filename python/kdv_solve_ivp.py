import numpy as np
from scipy.integrate import solve_ivp
from differential import make_differential_ops  # differential.pyから関数をインポート

# KdV方程式 u_{t} = -6 u u_{x} - u_{xxx}
def f_kdv(t, u, df1, df3):
    u_x = df1 @ u  # 行列-ベクトル積
    u_xxx = df3 @ u  # 行列-ベクトル積
    return -6 * u * u_x - u_xxx  # u*u_x は成分ごとの掛け算

def solve_kdv(x, u0, t_range, nt):
    nx = x.size
    dx = x[1] - x[0]
    print("dx =", dx)

    # 微分を表す行列
    op_df1, _, op_df3 = make_differential_ops(nx, dx)  # (*1)
    assert op_df1.shape == op_df3.shape == (nx, nx)  # 配列のshapeを確認

    print("Solving equation...")
    sol = solve_ivp(f_kdv, t_range, u0, dense_output=True, args=(op_df1, op_df3), rtol=1e-8)  # (*2)
    print(sol.message)
    print(" Number of time steps :", sol.t.size)  # 時間ステップ数
    print(" minimum time step    :", np.diff(sol.t).min())  # 最小時間刻み
    print(" Maximum time step    :", np.diff(sol.t).max())  # 最大時間刻み

    # 動画作成用のu(t, x)を取得（dense output）
    t_min, t_max = t_range
    t = np.linspace(t_min, t_max, nt)
    dt = t[1] - t[0]
    print("dt =", dt)

    u_xt = sol.sol(t)  # u(x, t)を取得  (*3)
    assert u_xt.shape == (nx, nt)  # 配列のshapeを確認
    u_tx = u_xt.T  # 転置をとってu(t, x)に変換
    assert u_tx.shape == (nt, nx)  # 配列のshapeを確認
    print("shape of u(t, x) :", u_tx.shape)

    # 結果をファイルに保存
    np.savez("kdv_solve_ivp", x=x, t=t, u_tx=u_tx)  # (*4)

def main():
    # x座標の離散化
    nx = 1000
    x_max = 100.0
    x = np.linspace(0, x_max, nx, endpoint=False)  # 周期境界 (*5)

    u0 = np.sin(x * (2 * np.pi / x_max))  # 初期条件 u_0(x) (*6)
    assert u0.shape == (nx,)  # 配列のshapeを確認

    nt = 101  # 時刻tの数（動画作成用）
    t_max = 10.0  # 最終時刻

    solve_kdv(x=x, u0=u0, t_range=(0, t_max), nt=nt)

if __name__ == '__main__':
    main()
