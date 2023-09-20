import numpy as np
from scipy import linalg
from spin import make_spin_ops  # spin.pyから関数をインポート

def main():
    # スピン行列を生成
    sp_ops = make_spin_ops()
    sx = sp_ops['Sx']
    sy = sp_ops['Sy']
    sz = sp_ops['Sz']

    # Sxを対角化
    eigval, eigvec = linalg.eigh(sx)  # 対角化 (*1)
    print("Eigenvalues =\n", eigval)
    print("Eigenvectors (column vectors)=\n", eigvec)

    # U = <z|x>
    #   |x> : Sxの固有ベクトル
    #   |z> : Szの固有ベクトル
    u = eigvec

    # 量子化軸をzからxに変更（表現行列を変換）(*2)
    sx_2 = u.conj().T @ sx @ u
    sy_2 = u.conj().T @ sy @ u
    sz_2 = u.conj().T @ sz @ u
    print("\nAfter basis transform")
    print("Sx' =\n", sx_2.round(10))  # 四捨五入 (*3)
    print("Sy' =\n", sy_2.round(10))
    print("Sz' =\n", sz_2.round(10))

if __name__ == '__main__':
    main()
