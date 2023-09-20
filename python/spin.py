import numpy as np

# スピン行列を生成する関数
def make_spin_ops():
    ops = {}  # 辞書型にまとめて返す

    # S^x, S^y, S^z
    ops['Sx'] = np.array([[0, 1], [1, 0]]) / 2
    ops['Sy'] = np.array([[0, -1j], [1j, 0]]) / 2
    ops['Sz'] = np.array([[1, 0], [0, -1]]) / 2

    # S^+, S^-
    ops['S+'] = np.array([[0, 1], [0, 0]])
    ops['S-'] = np.array([[0, 0], [1, 0]])

    # 単位行列
    ops['I'] = np.identity(2)
    return ops

# 交換関係
def commutation(mat1, mat2):
    return mat1 @ mat2 - mat2 @ mat1

def main():
    # スピン行列を生成
    sp_ops = make_spin_ops()
    sx = sp_ops['Sx']
    sy = sp_ops['Sy']
    sz = sp_ops['Sz']

    # スピン行列を出力
    print("Sx =\n", sx)
    print("Sy =\n", sy)
    print("Sz =\n", sz)

    # 交換関係を計算して出力
    print("\nCommutation relations")
    print("[Sx, Sy] =\n", commutation(sx, sy))  # = i Sz
    print("[Sy, Sz] =\n", commutation(sy, sz))  # = i Sx
    print("[Sz, Sx] =\n", commutation(sz, sx))  # = i Sy

if __name__ == '__main__':
    main()
