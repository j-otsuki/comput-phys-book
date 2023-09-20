import numpy as np
import matplotlib.pyplot as plt
from newton import solve_newton  # newton.pyからsolve_newton関数を読み込む
from collections import namedtuple

def plot(results):
    fig, ax = plt.subplots(figsize=(6, 3.5), constrained_layout=True)
    for r in results:
        # namedtupleの各フィールドにはドットでアクセス
        ax.plot(r.xt, r.yt, marker='.', label=r.key)
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_aspect('equal')  # x軸とy軸を同じスケールにする
    ax.legend(fontsize='x-small')  # 凡例
    fig.savefig("newton_angles.pdf")

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

    # 各初期条件に対する結果をそれぞれnamedtupleとしてまとめる (*1)
    Result = namedtuple('Result', ['key', 'xt', 'yt'])
    results = []  # 異なるthetaの結果を格納するリスト

    for theta_degree in range(5, 90, 5):  # thetaを5°から85°まで5度間隔で変化
        theta = theta_degree * (np.pi / 180)  # 角度（ラジアン）

        # X0 = [x0, v0_x, y0, v0_y]
        X0 = np.array([0, v0 * np.cos(theta), 0, v0 * np.sin(theta)])

        # ニュートン方程式を解いて、結果x(t), y(t)を取得
        xt, _, yt, _ = solve_newton(eq_params=(m, g, b), X0=X0, t_range=(t_start, t_end), n_t=n_t)

        # 結果をnamedtupleにまとめ、リストに追加 (*2)
        results.append(Result(str(theta_degree), xt, yt))

    plot(results)

if __name__ == '__main__':
    main()
