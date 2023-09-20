import numpy as np
from scipy import linalg
from spin import make_spin_ops  # spin.pyから関数をインポート

# 3つの1スピン演算子から3スピン演算子を生成
def kron3(s1, s2, s3):
    return np.kron(s1, np.kron(s2, s3))

def main():
    sp_ops = make_spin_ops()
    sz = sp_ops['Sz']
    sp = sp_ops['S+']
    sm = sp_ops['S-']
    s0 = sp_ops['I']
    assert sz.shape == sp.shape == sm.shape == s0.shape == (2, 2)  # 行列サイズを確認

    # 3スピン系のハミルトニアンを生成
    hamil = kron3(sz,sz,s0) + (kron3(sp,sm,s0) + kron3(sm,sp,s0)) / 2 \
          + kron3(s0,sz,sz) + (kron3(s0,sp,sm) + kron3(s0,sm,sp)) / 2 \
          + kron3(sz,s0,sz) + (kron3(sm,s0,sp) + kron3(sp,s0,sm)) / 2
    assert hamil.shape == (8, 8)  # 行列サイズを確認
    # print("H =\n", hamil)

    eigval, eigvec = linalg.eigh(hamil)

    print("Eigenvalues =\n", eigval)
    # print("Eigenvectors =")
    # for i in range(8):
    #     print(eigvec[:, i])  # 固有ベクトルは縦ベクトルであることに注意

if __name__ == '__main__':
    main()
