import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def save_animation(x, t, u_tx, ymin, ymax, filename):
    fig, ax = plt.subplots()  # オブジェクト指向インターフェース

    # すべてのグラフに共通の設定
    ax.set_xlabel(r"$x$")  # LaTeX記法
    ax.set_ylabel(r"$u(x)$")
    ax.set_ylim(ymin, ymax)

    artists = []  # 全時刻のグラフを保存するリスト
    for i in range(t.size):
        # i番目のグラフを作成
        artist = ax.plot(x, u_tx[i, :], '-b')  # (*1)
        artist += [ax.text(0.05, 1.05, f"t = {t[i]:.2f}", transform=ax.transAxes)]  # (*2)
        artists.append(artist)

    # アニメーションを作成
    anim = animation.ArtistAnimation(fig, artists, interval=100, repeat=False)  # (*3)

    # ファイルに保存
    anim.save(filename, writer="pillow")  # writer="pillow" or "imagemagick" for GIF
    print(f"saved as '{filename}'")

def main():
    # データをファイルから読み込む
    npz = np.load("kdv_solve_ivp.npz")  # (*4)
    print("npz.files =", npz.files)

    x = npz['x']
    t = npz['t']
    u_tx = npz['u_tx']
    print("x.shape =", x.shape)
    print("t.shape =", t.shape)
    print("u_tx.shape =", u_tx.shape)

    print("Making animation...")
    save_animation(x, t, u_tx, ymin=-1.5, ymax=3.0, filename="kdv_solve_ivp.gif")

if __name__ == '__main__':
    main()
