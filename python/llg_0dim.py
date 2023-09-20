import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def func_llg(t, m, h, gamma, lmd):
    m_cross_h = np.cross(m, h)  # 外積 (*1)
    m_cross_m_cross_h = np.cross(m, m_cross_h)  # 外積 (*2)
    return -gamma * m_cross_h - lmd * m_cross_m_cross_h

def solve_llg(eq_params, m0, h, t_range, n_t):
    gamma, alpha = eq_params  # タプルを展開 (unpack)

    gamma2 = 2 * np.pi * gamma / (1 + alpha**2)
    lmd = alpha * gamma2

    # 常微分方程式を解く
    sol = solve_ivp(func_llg, t_range, m0, args=(h, gamma2, lmd), dense_output=True)
    print(sol.message)

    # グラフ作成用のdense output
    t_start, t_end = t_range  # タプルを展開 (unpack)
    t = np.linspace(t_start, t_end, n_t)
    mt = sol.sol(t)
    assert mt.shape == (3, n_t)  # 配列の形を確認
    return t, mt

def plot(t, mt):
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(t, mt[0, :], marker='.', label=r"$m_x$")
    ax.plot(t, mt[1, :], marker='.', label=r"$m_y$")
    ax.plot(t, mt[2, :], marker='.', label=r"$m_z$")
    ax.set_xlabel(r'$t / T_0$')
    ax.set_ylabel(r'$m_{\xi}(t)$')
    ax.legend()
    fig.savefig("llg_0dim_mt.pdf")

def plot3D(t, mt):
    fig = plt.figure(constrained_layout=True)
    ax = fig.add_subplot(projection='3d')  # 3次元プロット用のAxesを取得 (*3)
    opt = dict(length=1, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, mt[0, 0], mt[1, 0], mt[2, 0], **opt)  # 初期ベクトル
    ax.quiver(0, 0, 0, mt[0, -1], mt[1, -1], mt[2, -1], **opt)  # 最終ベクトル
    ax.plot(mt[0, :], mt[1, :], mt[2, :])  # 軌跡
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel(r'$m_x$')
    ax.set_ylabel(r'$m_y$')
    ax.set_zlabel(r'$m_z$')
    fig.savefig("llg_0dim_3D.pdf")

def main():
    gamma = 1.0  # 基準
    alpha = 0.1

    t_start, t_end = 0, 8  # 時刻の範囲
    n_t = 401  # 時刻の刻み数（グラフ描画用）

    m0 = np.array([1, 0, 0])  # 初期条件
    h = np.array([0, 0, 1])  # 磁場（基準）

    # LLG方程式を解いて、結果m(t)を取得
    t, mt = solve_llg(eq_params=(gamma, alpha), m0=m0, h=h, t_range=(t_start, t_end), n_t=n_t)
    assert mt.shape == (3, n_t)  # 配列の形を確認

    # グラフ作成
    plot(t, mt)
    plot3D(t, mt[:, :200])

if __name__ == '__main__':
    main()
