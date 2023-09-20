import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ニュートン方程式 dX/dt = f(t, X)
def f_newton(t, X, m, g, b):
    # X = [x, v_x, y, v_y]
    dXdt = np.array([
        X[1],              # dx/dt = v_x
        -(b/m) * X[1],     # dv_x/dt = -(b/m) v_x
        X[3],              # dy/dt = v_y
        -(b/m) * X[3] - g  # dv_y/dt = -(b/m) v_y - g
    ])
    return dXdt

# ニュートン方程式を解く関数
#   eq_params: 方程式に含まれるパラメータ
#   X0: 初期条件
#   t_range: 時間の範囲
#   n_t: 時間の刻み数
def solve_newton(eq_params, X0, t_range, n_t):
    m, g, b = eq_params  # タプルを展開 (unpack) (*1)

    # 常微分方程式を解く
    sol = solve_ivp(f_newton, t_range, X0, args=(m, g, b), dense_output=True)  # (*2)
    print(sol.message)

    # グラフ作成用のdense output
    t_start, t_end = t_range  # タプルを展開 (unpack)
    t = np.linspace(t_start, t_end, n_t)
    Xt = sol.sol(t)  # (*3)
    assert Xt.shape == (4, n_t)  # 配列の形を確認 (*4)

    # x(t), v_x(t), y(t), v_y(t)
    return Xt[0, :], Xt[1, :], Xt[2, :], Xt[3, :]

def plot(xt, yt):
    fig, ax = plt.subplots(figsize=(6, 3.5), constrained_layout=True)
    ax.plot(xt, yt, marker='.')
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_aspect('equal')  # x軸とy軸を同じスケールにする
    fig.savefig("newton.pdf")

def main():
    # パラメーター (MKS単位系: m, kg, s)
    g = 9.8  # [m/s^2]
    m = 0.1  # [kg]
    b = 0.1  # [kg/s]

    t_start = 0  # 初期時刻 [s]
    t_end = 5.0  # 最終時刻 [s]
    n_t = 101  # 時刻の刻み数（グラフ描画用）

    # 初期条件
    v0 = 100.0 / 3.6  # 初速 [m/s]
    theta = 45 * (np.pi / 180)  # 角度（ラジアン）

    # X0 = [x0, v0_x, y0, v0_y]
    X0 = np.array([0, v0 * np.cos(theta), 0, v0 * np.sin(theta)])

    # ニュートン方程式を解いて、結果x(t), y(t)を取得 (*5)
    xt, _, yt, _ = solve_newton(eq_params=(m, g, b), X0=X0, t_range=(t_start, t_end), n_t=n_t)

    # グラフ作成
    plot(xt, yt)

if __name__ == '__main__':
    main()
