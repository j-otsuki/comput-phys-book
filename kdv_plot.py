import numpy as np
import matplotlib.pyplot as plt
import os

def save_figures(x, t, u_tx, ymin, ymax, basename):
    # ディレクトリを作成
    os.makedirs(os.path.dirname(basename), exist_ok=True)

    for i in range(t.size):
        # i番目のグラフを作成
        fig, ax = plt.subplots()
        ax.set_xlabel(r"$x$")
        ax.set_ylabel(r"$u(x)$")
        ax.set_ylim(ymin, ymax)
        ax.plot(x, u_tx[i, :], '-b')
        ax.text(0.05, 1.05, f"t = {t[i]:.2f}", transform=ax.transAxes)
        fig.savefig(f"{basename}_{i:03}.pdf")
        plt.close()

def main():
    # データをファイルから読み込む
    npz = np.load("kdv_solve_ivp.npz")
    print("npz.files =", npz.files)

    x = npz['x']
    t = npz['t']
    u_tx = npz['u_tx']
    print("x.shape =", x.shape)
    print("t.shape =", t.shape)
    print("u_tx.shape =", u_tx.shape)

    # グラフを作成
    print("Making figures...")
    save_figures(x, t, u_tx, ymin=-1.5, ymax=3.0, basename="kdv/kdv")

if __name__ == '__main__':
    main()
