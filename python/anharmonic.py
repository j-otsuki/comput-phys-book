import numpy as np
from scipy import linalg
from scipy import sparse
from differential import make_differential_ops  # differential.pyから関数をインポート

# 量子非調和振動子の固有エネルギーと固有関数を求める関数
def solve_anharmonic(x_max, nx, anharmonicity, file_val="eigenval.dat", file_vec="eigenvec.dat", n_vec=10):

    print("making Hamiltonian...")
    x = np.linspace(-x_max, x_max, nx)  # x点の配列を生成
    assert x.shape == (nx,)  # 配列のshapeを確認 (*1)
    dx = x[1] - x[0]
    print("dx =", dx)

    # ポテンシャル項
    v_diag = 0.5 * x**2 + anharmonicity * x**4  # 対角成分 (*2)
    v_matrix = sparse.diags(v_diag)  # 対角行列を生成
    assert v_matrix.shape == (nx, nx)  # 配列のshapeを確認

    # 運動エネルギー項 -(1/2) d^2/dx^2
    _, deriv2, _ = make_differential_ops(nx, dx)  # 2階微分を表す行列D^2 (*3)
    assert isinstance(deriv2, sparse.spmatrix)  # deriv2は疎行列クラス
    kin_matrix = -0.5 * deriv2  # 疎行列からNumPy配列に変換
    assert kin_matrix.shape == (nx, nx)  # 配列のshapeを確認

    # ハミルトニアン行列
    h_matrix = v_matrix + kin_matrix

    # 対角化
    print("diagonalizing Hamiltonian...")
    eigval, eigvec = linalg.eigh(h_matrix.toarray())  # 対角化 (*4)
    assert eigval.shape == (nx,)
    assert eigvec.shape == (nx, nx)
    eigvec /= np.sqrt(dx)  # 固有ベクトルを規格化（結果がdxに依存しないように）(*5)

    # 固有値・固有ベクトルをファイルに保存
    print("saving results...")
    np.savetxt(file_val, eigval)
    np.savetxt(file_vec, np.hstack([x[:, None], eigvec[:, :n_vec]]))  # (*6)

    return eigval, eigvec

def main():
    nx = 1001  # x点の数
    x_max = 10  # xの範囲 [-x_max: x_max]
    anharmonicity = 0  # 非調和パラメータ alpha'
    eigval, _ = solve_anharmonic(x_max, nx, anharmonicity, n_vec=61)

    # 固有値を出力
    for i in range(4):
        print(f"E[{i}] = {eigval[i]:.8f}")  # 小数点以下8桁まで出力

if __name__ == '__main__':
    main()
