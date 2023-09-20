import numpy as np
# bec.pyから関数をインポート
from bec import calc_alpha, calc_specific_heat

def main():
    tmin, tmax = 0, 3
    n = 301
    for t in np.linspace(tmin, tmax, n):  # tに関するループ
        alpha = calc_alpha(t, verbose=False)  # alphaを計算
        c = calc_specific_heat(alpha, t)  # 比熱Cを計算
        print(f"{t:.4f} {alpha:.5e} {c:.5e}")

if __name__ == '__main__':
    main()
