import numpy as np
import matplotlib.pyplot as plt

# dy/dt=f(y)の定義
def f_logistic(y):
    return y * (1.0 - y)  # ロジスティック方程式

# オイラー法による時間発展
def step_forward(f, y, dt):
    return y + f(y) * dt

# 常微分方程式を解く関数
#   f: 関数f(y)
#   y0: 初期値
#   tmax: 終了時刻
#   nt: 時間の分割数
def solve_ode(f, y0, tmax, nt):
    t = np.linspace(0, tmax, nt)  # 時間の等間隔メッシュを生成 (*1)
    dt = t[1] - t[0]
    y = [y0,]  # 結果を格納するリスト (*2)
    for _ in range(nt-1):  # 時刻のループ
        y.append(step_forward(f, y[-1], dt))  # 時刻を1つ進めて結果をyに追加  (*3)
    return t, np.array(y)  # 結果をNumPy配列として返す (*4)

def main():
    # ロジスティック方程式を解く
    t, y = solve_ode(f_logistic, y0=1e-3, tmax=20, nt=101)

    # グラフを描画
    fig, ax = plt.subplots()
    ax.plot(t, y, '.')
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    fig.savefig("logistic.pdf")  # ファイルに保存

if __name__ == '__main__':  # (*5)
    main()
