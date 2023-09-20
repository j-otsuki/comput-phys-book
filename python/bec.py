import numpy as np
from scipy import optimize  # 非線形方程式
from scipy import special  # 特殊関数
from bec_integ import bose_einstein_integral  # ボーズ-アインシュタイン積分

# alphaの満たす方程式
def func_alpha(alpha, t):
    return bose_einstein_integral(1.5, alpha) * t**1.5 - special.zeta(1.5)

# alphaを計算
def calc_alpha(t, a_min=0, a_max=100, verbose=False):
    if t <= 1:
        return 0
    sol = optimize.root_scalar(func_alpha, args=(t,), method='brentq', bracket=(a_min, a_max))
    if verbose:
        print(sol)  # 結果のまとめを出力
    return sol.root

# 比熱を計算
def calc_specific_heat(alpha, t):
    if t<=1:
        z52 = special.zeta(2.5)  # ゼータ関数
        z32 = special.zeta(1.5)
        return 15. * z52 / (4. * z32) * t**1.5
    else:
        f12 = bose_einstein_integral(0.5, alpha)
        f32 = bose_einstein_integral(1.5, alpha)
        f52 = bose_einstein_integral(2.5, alpha)
        return 15. * f52 / (4. * f32) - 9. * f32 / (4. * f12)

def main():
    t = 1.5  # 無次元温度T/T_c
    alpha = calc_alpha(t, verbose=True)  # alphaを計算
    c = calc_specific_heat(alpha, t)  # 比熱Cを計算
    print(f"alpha = {alpha:.8g}")
    print(f"c = {c:.8g}")

if __name__ == '__main__':
    main()
