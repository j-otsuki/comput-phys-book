import numpy as np
from scipy import optimize

# 自己無撞着方程式
def func(m, zj, beta, h):
    return m - np.tanh(beta * (zj * m + h))

# 自己無撞着方程式を満たす解mを返す関数
def find_solution(zj, t, h, bracket=(1e-6, 1), verbose=False):
    beta = np.inf if t==0 else 1./t  # 逆温度beta
    sol = optimize.root_scalar(func, args=(zj, beta, h), method='brentq', bracket=bracket)
    if verbose:
        print(sol)  # 結果のまとめを出力
    return sol.root  # 解を返す

# エントロピーを返す関数
def calc_entropy(m):
    if abs(m)==1:  # m=1は別扱い
        return 0
    s = 0
    for x in [(1.0+m)/2.0, (1.0-m)/2.0]:
        s -= x * np.log(x)
    return s

# 比熱を返す関数
def calc_specific_heat(m, zj, t):
    if abs(m)==1:  # m=1は別扱い
        return 0
    t_tc = t / zj  # T / T_c
    c = m**2 * (1.0-m**2) / (t_tc * (t_tc - (1.0-m**2)))
    return c

def main():
    t = 0.5  # 温度T
    zj = 1.0  # 相互作用zJ
    h = 0.0  # 外部磁場H
    m = find_solution(zj, t, h, verbose=True)  # 自己無撞着方程式を解く
    s = calc_entropy(m)  # エントロピーを計算
    c = calc_specific_heat(m, zj, t)  # 比熱を計算
    print(f"zJ = {zj:.8g}")
    print(f"T  = {t:.8g}")
    print(f"h  = {h:.8g}")
    print(f"m  = {m:.8g}")
    print(f"S  = {s:.8g}")
    print(f"C  = {c:.8g}")

if __name__ == '__main__':
    main()
