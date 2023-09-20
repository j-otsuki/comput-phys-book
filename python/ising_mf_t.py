import numpy as np
# ising_mf.pyファイルから関数をインポート
from ising_mf import find_solution, calc_entropy, calc_specific_heat

def main():
    h = 0
    tmin, tmax = 0, 1
    n = 201
    for t in np.linspace(tmin, tmax, n):
        try:  # 例外処理 (*1)
            m = find_solution(1., t, h)
            s = calc_entropy(m)
            c = calc_specific_heat(m, 1., t)
        except ValueError as e:  # 例外ValueErrorをキャッチ
            print(f"# {t:.4f} {e}")
        else:  # エラーが出なかった場合
            print(f"{t:.4f} {m:.5e} {s:.5e} {c:.5e}")

if __name__ == '__main__':
    main()
