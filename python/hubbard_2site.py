import numpy as np
from scipy import linalg
from hubbard_1site import make_local_ops, kron  # hubbard_1site.pyから関数をインポート

# ハミルトニアンhを粒子数nの部分空間に射影
def projection(h, n):
    assert isinstance(n, int)  # nはint型
    from itertools import product
    # 粒子数がnの状態ベクトルのインデックス (*3)
    indices = [i for i, state in enumerate(product([0, 1], repeat=4)) if sum(state)==n]
    return h[np.ix_(indices, indices)]  # 2次元配列のスライス (*4)

# 2サイトハバード模型の固有値・固有ベクトルを計算
def solve_hubbard_2site(t, U, mu=0, n=None):
    # 生成・消滅演算子の2×2表現行列を生成（スピンなし）
    local_ops = make_local_ops()
    cdag = local_ops['c^+']
    I = local_ops['I']
    F = local_ops['F']
    assert cdag.shape == I.shape == F.shape == (2, 2)

    # スピン・サイトを考慮
    Cdag = {}  # 生成演算子 (*1)
    Cdag['1u'] = kron(I, I, I, cdag)
    Cdag['1d'] = kron(I, I, cdag, F)
    Cdag['2u'] = kron(I, cdag, F, F)
    Cdag['2d'] = kron(cdag, F, F, F)
    assert Cdag['1u'].shape == Cdag['1d'].shape == (16, 16)

    C = {}  # 消滅演算子
    N = {}  # 粒子数演算子
    for key, cdag in Cdag.items():
        C[key] = cdag.conj().T  # エルミート共役
        N[key] = cdag @ C[key]

    hamil = 0
    # t項
    for key1, key2 in [('1u', '2u'), ('1d', '2d'), ('2u', '1u'), ('2d', '1d')]:
        hamil += -t * Cdag[key1] @ C[key2]
    # U項
    for key1, key2 in [('1u', '1d'), ('2u', '2d')]:
        hamil += U * N[key1] @ N[key2]
    # mu項
    for n_op in N.values():
        hamil += -mu * n_op

    if n is not None:
        hamil = projection(hamil, n)  # ハミルトニアンを粒子数nの部分空間に射影 (*2)

    print("Size of Hamiltonian matrix =", hamil.shape)
    eigval, eigvec = linalg.eigh(hamil)  # 全対角化
    return eigval, eigvec

def main():
    t = 1.0
    U = 4.0
    mu = 2.0

    E, vec = solve_hubbard_2site(t, U, mu)
    # E, vec = solve_hubbard_2site(t, U, mu, n=2)  # 粒子数射影をする場合
    print("E =\n", E)

if __name__ == '__main__':
    main()
