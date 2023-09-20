import numpy as np
from poisson import solve_poisson_2d, make_rho, make_boundary  # 別ファイルから関数をインポート

# 中心(x0, y0), 半径rの円の中でTrueを持つ2次元配列を生成
def make_circle(x, y, x0, y0, r):
    boundary = ((x[:, None] - x0)**2 + (y[None, :] - y0)**2)**0.5 < r  # (*1)
    return boundary

def main():
    Lx, Ly = 1.4, 1.0
    nx, ny = 141, 101
    print(f"(nx, ny) = {nx, ny}")

    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    print(f"dx = {x[1] - x[0]}")
    print(f"dy = {y[1] - y[0]}")

    # 電荷分布
    rho = make_rho(x, y)
    assert rho.shape == (nx, ny)

    # 端における境界条件
    boundary = make_boundary(x, y)
    assert boundary.shape == (nx, ny)

    # 円柱における境界条件 (*2)
    boundary_circle = make_circle(x, y, x0=0.4, y0=0.5, r=0.1)
    assert boundary_circle.shape == (nx, ny)

    # 論理和（or）をとって2つの境界条件を合成 (*3)
    boundary |= boundary_circle

    solve_poisson_2d(x, y, rho, boundary)

if __name__ == '__main__':
    main()
