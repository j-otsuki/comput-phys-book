import numpy as np
from scipy import linalg
from spin import make_spin_ops  # spin.pyから関数をインポート

def main():
    # 1スピン演算子を取得
    sp_ops = make_spin_ops()
    sz = sp_ops['Sz']
    sp = sp_ops['S+']
    sm = sp_ops['S-']
    assert sz.shape == sp.shape == sm.shape == (2, 2)  # 行列サイズを確認

    # 2スピン系のハミルトニアンを生成
    hamil = np.kron(sz, sz) + (np.kron(sp, sm) + np.kron(sm, sp)) / 2.0
    assert hamil.shape == (4, 4)  # 行列サイズを確認
    print("H =\n", hamil)

    eigval, eigvec = linalg.eigh(hamil)  # 対角化

    print("Eigenvalues =\n", eigval)
    print("Eigenvectors =")
    for i in range(4):
        print(eigvec[:, i])  # 固有ベクトルは縦ベクトルであることに注意

if __name__ == '__main__':
    main()
