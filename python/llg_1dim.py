import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def func_llg(t, m, h, gamma, lmd, J):
    m_3d = m.reshape(-1, 3)  # 2次元化
    h_eff = h + (J/2.) * (np.roll(m_3d, 1, axis=0) + np.roll(m_3d, -1, axis=0))  # 有効磁場 (*1)
    m_cross_h = np.cross(m_3d, h_eff)  # 外積 (*2)
    m_cross_m_cross_h = np.cross(m_3d, m_cross_h)  # 外積 (*3)
    dmdt = -gamma * m_cross_h - lmd * m_cross_m_cross_h
    return dmdt.reshape(-1)  # 1次元化

def solve_llg(eq_params, m0, h, t_range, n_t):
    gamma, alpha, J = eq_params  # タプルを展開 (unpack)
    gamma2 = 2 * np.pi * gamma / (1 + alpha**2)
    lmd = alpha * gamma2

    # 常微分方程式を解く
    m0_1d = m0.reshape(-1)  # 1次元化
    sol = solve_ivp(func_llg, t_range, m0_1d, args=(h, gamma2, lmd, J), dense_output=True)
    print(sol.message)

    # グラフ作成用のdense output
    t_start, t_end = t_range  # タプルを展開 (unpack)
    t = np.linspace(t_start, t_end, n_t)
    mt_1d = sol.sol(t)  # (3*N, n_t)
    mt = mt_1d.reshape(-1, 3, n_t)  # (N, 3, n_t)
    return t, mt

def plot(t, mt):
    N, _, _ = mt.shape
    x = np.arange(N)

    for i in range(0, t.size, 10):
        fig, ax = plt.subplots(figsize=(8, 1.5), constrained_layout=True)
        ax.axis('off')  # 軸を消去
        ax.axhline(0, lw=0.5, color='k')  # x軸
        ax.quiver(x, 0, mt[:, 0, i], mt[:, 1, i])  # x軸上に磁気モーメントのxy成分を矢印で描画 (*4)
        ax.text(0.05, 1.05, rf"$t / T_1 = {t[i]:.2f}$", transform=ax.transAxes)  # 時刻
        fig.savefig(f"llg_1dim_{i:03d}.pdf")
        plt.close()  # キャッシュをクリア

def make_anim(t, mt):
    N, _, _ = mt.shape
    x = np.arange(N)

    fig, ax = plt.subplots(figsize=(8, 1.5), constrained_layout=True)
    ax.axis('off')  # 軸を消去

    artists = []
    for i in range(t.size):
        artist = [ax.quiver(x, 0, mt[:, 0, i], mt[:, 1, i])]
        artist += [ax.axhline(0, lw=0.5, color='k')]
        artist += [ax.text(0.05, 1.05, rf"$t / T_1 = {t[i]:.2f}$", transform=ax.transAxes)]
        artists.append(artist)

    anim = animation.ArtistAnimation(fig, artists, interval=100, repeat=False)

    file_gif = "llg_1dim_anim.gif"
    anim.save(file_gif, writer="imagemagick")
    print(f"'{file_gif}' generated")

def main():
    N = 40  # 磁気モーメントの数
    gamma = 1.0  # 基準
    alpha = 0.1
    J = 1.0  # 基準

    t_start, t_end = 0, 40  # 時刻の範囲
    n_t = 201  # 時刻の刻み数（グラフ描画用）

    # 初期条件
    seed = 1  # 乱数の種
    rng = np.random.default_rng(seed=seed)  # 乱数生成器 (*5)
    m0 = rng.random(size=(N, 3)) * 2 - 1  # [-1:1)
    m_norm = np.sum(m0**2, axis=1)**0.5  # 磁化の大きさ
    assert m_norm.shape == (N,)
    m0 /= m_norm[:, None]  # 規格化
    assert m0.shape == (N, 3)  # 配列の形を確認

    h = np.array([0, 0.1, 0])  # 磁場

    # LLG方程式を解いて、結果m(t)を取得
    t, mt = solve_llg(eq_params=(gamma, alpha, J), m0=m0, h=h, t_range=(t_start, t_end), n_t=n_t)
    assert mt.shape == (N, 3, n_t)  # 配列の形を確認

    # グラフ作成
    plot(t, mt)
    make_anim(t, mt)

if __name__ == '__main__':
    main()
