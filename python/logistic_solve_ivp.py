import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# dy/dt=f(t, y)の定義
def f_logistic(t, y):
    return y * (1.0 - y)  # ロジスティック方程式

# 厳密解
def logistic_func(y0, t):
    return y0 / (y0 + (1-y0) * np.exp(-t))

# グラフ作成
def plot(t_sparse, y_sparse, t_dense, y_dense, y_exact):
    fig, ax = plt.subplots()
    ax.plot(t_sparse, y_sparse, 'o', zorder=2, color='r', markerfacecolor='None', label="selected time points")
    ax.plot(t_dense, y_dense, '.', zorder=1, color='b', label="dense output")
    ax.plot(t_dense, y_exact, '-', zorder=1.5, color='c', label="Exact")
    ax.axhline(y=0, color='k', linestyle='dashed', zorder=0)  # 横線
    ax.axhline(y=1, color='k', linestyle='dashed', zorder=0)  # 横線
    ax.set_xlabel(r'$t$')  # xラベル（LaTeX表記）
    ax.set_ylabel(r'$y$')  # yラベル（LaTeX表記）
    ax.legend()  # 凡例
    fig.savefig("logistic.pdf")  # ファイルに保存

def main():
    y0 = np.array([1e-3,], dtype=float)  # 初期値（1成分のNumPy配列）
    t_start = 0  # 初期時刻
    t_end = 20.0  # 最終時刻

    # 常微分方程式を解く
    sol = solve_ivp(f_logistic, (t_start, t_end), y0, dense_output=True)  # (*1)
    print(sol.message)  # ソルバーのメッセージを表示
    print("sol.t.shape =", sol.t.shape)  # (n_points,)
    print("sol.y.shape =", sol.y.shape)  # (1, n_points)

    # グラフ描画用のデータ（dense output）
    nt = 101
    t = np.linspace(t_start, t_end, nt)  # 時刻tの等間隔メッシュを生成 (*2)
    y = sol.sol(t)  # メッシュ点上の時刻tにおけるy(t)の値を取得 (*3)
    print("t.shape =", t.shape)  # (nt,)
    print("y.shape =", y.shape)  # (1, nt)

    # グラフ作成
    plot(sol.t, sol.y[0], t, y[0], logistic_func(y0, t))

if __name__ == '__main__':
    main()
