import numpy as np
from scipy import sparse  # 疎行列クラス
from scipy.sparse.linalg import spsolve  # 疎行列用ソルバー
from scipy.linalg import lu_factor, lu_solve  # 密行列用ソルバー
from differential import make_differential_ops  # differential.pyから関数をインポート

# 1次元空間における1階微分および2階微分を表す行列D1, D2を生成
def make_diff_matrix(_x):
    dx = _x[1] - _x[0]
    nx = _x.size
    D1, D2, _ = make_differential_ops(nx, dx)  # 差分行列を取得
    assert isinstance(D1, sparse.spmatrix)  # D1は疎行列
    assert isinstance(D2, sparse.spmatrix)  # D2は疎行列
    I = sparse.identity(nx)  # 単位行列
    return I, D1, D2

# 境界条件付き連立方程式 A.x=b を解く関数
def solve_eq_with_boundary(A, b, boundary):
    print(f"A.shape = {A.shape}")  # (N, N)
    print(f"b.shape = {b.shape}")  # (N,)
    assert A.shape == b.shape + b.shape
    assert b.shape == boundary.shape

    not_boundary = np.logical_not(boundary)  # 境界以外でTrue (*1)

    # 境界領域を行列Aとベクトルbから除く
    A_reduced = A[np.ix_(not_boundary, not_boundary)]
    b_reduced = b[not_boundary]
    print(f"A_reduced.shape = {A_reduced.shape}")
    print(f"b_reduced.shape = {b_reduced.shape}")

    # 疎行列用のソルバーを使って方程式 A.x=b を解く
    x = spsolve(A_reduced, b_reduced)

    # 密行列用のソルバーを使って方程式 A.x=b を解く場合
    # lu = lu_factor(A_reduced.toarray())  # LU分解
    # x = lu_solve(lu, b_reduced)

    # 方程式の解xをphiに代入して返す
    phi = np.zeros(b.shape, dtype=float)
    phi[not_boundary] = x  # 境界領域を除いた部分にxを代入 (*2)
    return phi

# ポアソン方程式を解く関数
def solve_poisson_2d(x, y, rho, boundary):
    nx, ny = x.size, y.size  # x座標, y座標の点の数
    assert rho.shape == (nx, ny)  # rhoのshapeを確認
    assert boundary.shape == (nx, ny)  # boundaryのshapeを確認
    N = nx * ny  # 座標点の総数

    # x座標, y座標のそれぞれ1次元空間に対して差分行列と単位行列を取得
    id_x, d1_x, d2_x = make_diff_matrix(x)
    id_y, d1_y, d2_y = make_diff_matrix(y)

    # 2次元空間に作用する差分行列を生成 (*3)
    D1x = sparse.kron(d1_x, id_y)
    D1y = sparse.kron(id_x, d1_y)
    D2x = sparse.kron(d2_x, id_y)
    D2y = sparse.kron(id_x, d2_y)
    assert D1x.shape == D1y.shape == D2x.shape == D2y.shape == (N, N)

    # 2次元のラプラシアンD2を計算
    D2 = D2x + D2y
    assert D2.shape == (N, N)

    # 2次元配列を1次元配列に変換
    rho = rho.reshape(-1)
    boundary = boundary.reshape(-1)
    assert rho.shape == boundary.shape == (N,)

    # 境界条件付き連立方程式 D2.phi=-rho を解く
    phi = solve_eq_with_boundary(A=D2, b=(-1)*rho, boundary=boundary)
    assert phi.shape == (N,)

    # 電場 E = -grad phi を計算 (*4)
    Ex = -D1x @ phi
    Ey = -D1y @ phi
    assert Ex.shape == Ey.shape == (N,)

    # 1次元配列を2次元配列に変換 (*5)
    phi = phi.reshape((nx, ny))
    Ex = Ex.reshape((nx, ny))
    Ey = Ey.reshape((nx, ny))

    # 結果をファイルに保存 (*6)
    np.savez("poisson", phi=phi, Ex=Ex, Ey=Ey, x=x, y=y)

# 電荷分布を生成する関数
def make_rho(x, y):
    dx, dy = x[1] - x[0], y[1] - y[0]
    nx, ny = x.size, y.size
    nx0, ny0 = nx // 2, ny // 2  # 中心座標
    # デルタ関数
    rho = np.zeros((nx, ny), dtype=float)
    rho[nx0, ny0] = 1 / (dx * dy)  # 離散座標なのでデルタ関数は有限値になる
    return rho

# 境界条件を生成する関数
def make_boundary(x, y):
    nx, ny = x.size, y.size
    # 境界領域でTrue, それ以外でFalse
    boundary = np.full((nx, ny), False)
    boundary[0, :] = True
    boundary[-1, :] = True
    boundary[:, 0] = True
    boundary[:, -1] = True
    return boundary

def main():
    Lx, Ly = 1.0, 1.0  # 系の一辺の長さ
    nx, ny = 51, 51  # グリッドの数
    print(f"(nx, ny) = {nx, ny}")

    # x座標、y座標を離散化した配列を生成
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    print(f"dx = {x[1] - x[0]}")
    print(f"dy = {y[1] - y[0]}")

    # 電荷密度を生成
    rho = make_rho(x, y)
    assert rho.shape == (nx, ny)  # 得られたrhoのサイズを確認

    # 境界条件を生成
    boundary = make_boundary(x, y)
    assert boundary.shape == (nx, ny)  # 得られたboundaryのサイズを確認

    # ポアソン方程式を解く
    solve_poisson_2d(x, y, rho, boundary)

if __name__ == '__main__':
    main()
