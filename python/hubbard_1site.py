import numpy as np
from scipy import linalg

# 生成・消滅演算子の表現行列を生成する関数
def make_local_ops():
    ops = {}  # 辞書を返す
    ops['c^+'] = np.array([[0, 0], [1, 0]])  # 生成演算子
    ops['c'] = np.array([[0, 1], [0, 0]])  # 消滅演算子
    ops['I'] = np.identity(2)  # 単位行列
    ops['F'] = np.diag([1, -1])  # フェルミオンの反交換を表す行列
    return ops

# 任意の個数の行列のクロネッカー積を計算
def kron(*ops):  # *opsは可変長引数 (*1)
    r = 1.0
    for op in ops:
        r = np.kron(r, op)
    return r

def solve_hubbard_1site(U, mu=0):
    # 生成・消滅演算子の2×2表現行列を生成（スピンなし）
    local_ops = make_local_ops()
    cdag = local_ops['c^+']
    I = local_ops['I']
    F = local_ops['F']
    assert cdag.shape == I.shape == F.shape == (2, 2)

    # スピンを考慮
    Cdag = {}  # 生成演算子
    Cdag['1u'] = kron(I, cdag)
    Cdag['1d'] = kron(cdag, F)
    assert Cdag['1u'].shape == Cdag['1d'].shape == (4, 4)

    C = {}  # 消滅演算子
    N = {}  # 粒子数演算子
    for key, cdag in Cdag.items():
        C[key] = cdag.conj().T  # エルミート共役
        N[key] = cdag @ C[key]

    hamil = U * N['1u'] @ N['1d'] - mu * (N['1u'] + N['1d'])
    print("H =\n", hamil)

    eigval, eigvec = linalg.eigh(hamil)  # 全対角化
    return eigval, eigvec

def main():
    U = 10.0
    mu = 2.0

    E, vec = solve_hubbard_1site(U, mu)
    print("E =\n", E)

    print("Eigenvectors =")
    for i in range(vec.shape[1]):
        print(vec[:, i])

if __name__ == '__main__':
    main()
