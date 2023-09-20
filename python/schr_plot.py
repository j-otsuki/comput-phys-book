import numpy as np
import matplotlib.pyplot as plt

def save_figures(x, t, rho_tx, v, xlim, ylim, basename):
    for i in range(t.size):  # すべての時刻tにおける図を作成
        fig, ax = plt.subplots(figsize=(6, 3), constrained_layout=True)
        ax.set_xlabel(r"$x$")
        ax.set_ylabel(r"$|\psi(x)|^2$")
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.plot(x, rho_tx[i, :], '-b', lw=1, zorder=4)  # 確率密度
        ax.fill_between(x, rho_tx[i, :], color="lightblue", alpha=0.5, zorder=3)  # (*1)
        ax.plot(x, v, color='k', lw=1, zorder=2)  # ポテンシャル
        ax.fill_between(x, v, color="lightgray", alpha=0.5, zorder=1)
        ax.text(0.05, 1.05, f"t = {t[i]:.2f}", transform=ax.transAxes)
        fig.savefig(f"{basename}_{i:03}.pdf")  # ファイル名 ~_001.pdf
        plt.close()  # キャッシュをクリア

def main():
    basename = 'schr'
    npz = np.load(basename + ".npz")  # npzファイルからデータを読み込む
    print("npz.files =", npz.files)

    x, t, v = npz['x'], npz['t'], npz['v']
    u_tx = npz['u_tx']
    rho = np.absolute(u_tx)**2  # 確率密度
    print("x.shape =", x.shape)
    print("t.shape =", t.shape)
    print("u_tx.shape =", u_tx.shape)

    # グラフを作成
    print("Making figures...")
    save_figures(x, t, rho, v, xlim=(-30, 30), ylim=(0, 0.4), basename=basename)

if __name__ == '__main__':
    main()
