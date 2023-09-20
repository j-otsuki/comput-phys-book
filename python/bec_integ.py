import numpy as np
from scipy import integrate  # 数値積分
from scipy import special  # 特殊関数
import matplotlib.pyplot as plt

# ボーズ-アインシュタイン積分の被積分関数
def integrand(x, s, alpha):  # xは積分変数、s, alphaはパラメータ
    e = np.exp(-x-alpha)  # <= 1  (x+alpha > 0)
    return x**(s-1) * e / (1.0 - e)  # (*1)

# ボーズ-アインシュタイン積分
def bose_einstein_integral(s, alpha, verbose=False):
    y, err = integrate.quad(integrand, 0, np.inf, args=(s, alpha))
    y /= special.gamma(s)  # ガンマ関数
    if verbose:
        print(f"integral : {y:.8g}")
        print(f"error    : {err:.1e}")
    return y

def main():
    s = 1.5

    # alpha=0の結果を確認：F_s(0) = zeta(s)
    bose_einstein_integral(s, 0, verbose=True)

    alpha_min, alpha_max = 0, 4
    n_alpha = 401
    x = np.linspace(alpha_min, alpha_max, n_alpha)
    y = np.array([bose_einstein_integral(s, alpha) for alpha in x])  # (*2)

    # グラフ
    fig, ax = plt.subplots()
    ax.plot(x, y, '.-')
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"$F_{3/2}(\alpha)$")
    ax.axhline(y=0, color='k', linestyle='dashed', zorder=0)  # x軸
    fig.savefig("bec_integ.pdf")

if __name__ == '__main__':
    main()
