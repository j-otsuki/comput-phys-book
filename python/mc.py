import numpy as np
from collections import namedtuple

# メトロポリス法の判定式（更新を行う場合にはTrueを返す）
def accept(p, rand):
    return p > rand  # rand=[0:1) なので、p>=1 ならつねにTrue

# サイトiのスピンを反転
def flip(_state, i):
    _state[i] ^= True

# 確率 p = e^{-beta*E_1} / e^{-beta*E_0}
def prob_flip(_mc, i):
    state = _mc.state
    state_nn = state[_mc.indices_nn[i]]  # 最近接サイトのスピン配置
    num_up = np.count_nonzero(state_nn)  # 最近接サイトのアップスピンの数
    if state[i]:  # spin up
        return _mc.prob_up[num_up]
    else:  # spin down
        return _mc.prob_dn[num_up]

# スイープを行う関数
def sweep(_mc):
    state = _mc.state

    # 事前に必要な数だけ乱数を生成しておく
    randn = _mc.rng.random(state.size)  # 乱数 [0:1)
    sites = _mc.rng.permutation(state.size)  # サイトのインデックスをランダムに並び替えた配列

    # すべてのスピンを1回づつランダムに選んで反転の試行を行う
    for i, rand in zip(sites, randn):
        p = prob_flip(_mc, i)  # 更新確率
        if accept(p, rand):  # 更新をするかどうか
            flip(state, i)  # 更新

# 物理量を測定して、結果を1次元配列として返す関数
def measure(_mc):
    state = _mc.state
    m = 2 * np.count_nonzero(state) - state.size  # 全スピン
    m /= state.size  # 1スピンあたり
    return np.array([m, m**2])

# 最近接格子点のインデックスを生成
def gen_indices_nn(system):
    ndim = len(system)  # 空間次元
    size = np.prod(system)  # サイトの総数
    z = 2 * ndim  # 最近接格子の数

    # サイトの通し番号（0からsize-1）
    index = np.arange(size).reshape(system)  # (nx, ny) for ndim=2

    # 最近接格子点の番号を取得
    indices_nn = []
    for axis in range(ndim):
        indices_nn.append(np.roll(index, 1, axis=axis))
        indices_nn.append(np.roll(index, -1, axis=axis))
    indices_nn = np.array(indices_nn)  # リストをNumPy配列に変換
    assert indices_nn.shape == (z,) + system  # (z, nx, ny)

    indices_nn = np.moveaxis(indices_nn, 0, -1)  # (z, nx, ny) → (nx, ny, z)
    assert indices_nn.shape == system + (z,)

    indices_nn = indices_nn.reshape(-1, z)  # (nx, ny, z) → (nx*ny, z)
    assert indices_nn.shape == (size, z)

    return indices_nn

# MC計算で使用する変数を1つにまとめておく (*1)
MC = namedtuple('MC', ['state', 'indices_nn', 'rng', 'prob_up', 'prob_dn'])

# 初期化
def mc_init(system, J, beta, seed):
    size = np.prod(system)  # サイトの総数

    # スピン配置（アップならTrue, ダウンならFalse）
    state = np.full(size, True, dtype=bool)  # すべてアップスピン

    # 乱数生成器
    rng = np.random.default_rng(seed)

    # 最近接サイトのインデックス
    indices_nn = gen_indices_nn(system)

    # 更新確率 e^{-2 K s_i sum_j s_j} を事前に計算
    # prob_up, prob_dn のインデックスは最近接サイトのアップスピンの数
    prob_up = []  # s_i = up の場合
    prob_dn = []  # s_j = down の場合
    K = J * beta  # 無次元化した相互作用
    z = 2 * len(system)  # 最近接格子点の数
    for num_up in range(z+1):
        sum_sigma = 2 * num_up - z  # sum_j s_j
        prob_up.append(np.exp(-2 * K * sum_sigma))
        prob_dn.append(np.exp(2 * K * sum_sigma))

    return MC(state, indices_nn, rng, prob_up, prob_dn)

# MC計算を行う関数（この関数をmainから呼ぶ）
def run_mc(system: tuple, J, beta, n_mc, seed=1):
    n_bin, n_measure, n_warmup = n_mc

    print("Initializing MC...")
    mc_data = mc_init(system, J, beta, seed)

    print("Warming up...")
    for _ in range(n_warmup):  # ウォームアップ
        sweep(mc_data)

    print("Measuring...")
    quant = []  # 各ビンごとの結果を入れるリスト
    for _ in range(n_bin):
        quant_bin = []  # 測定データを入れるリスト
        for _ in range(n_measure):
            sweep(mc_data)  # スイープ
            quant_bin.append(measure(mc_data))  # 測定
        quant.append(np.array(quant_bin).mean(axis=0))  # ビン内で平均
    quant = np.array(quant)
    print(f"  obtained data shape: {quant.shape}")

    quant_mean = quant.mean(axis=0)  # ビンごとに平均化
    quant_std = quant.std(axis=0)  # 標準偏差
    return quant_mean, quant_std

def main():
    system = (8, 8)  # 系のサイズ
    t = 4  # 温度（k_B=1）
    n_measure = 1000  # サンプル数
    n_bin = 10  # ビンの数
    n_warmup = 100  # ウォームアップ数
    n_mc = (n_bin, n_measure, n_warmup)
    q_mean, q_std = run_mc(system, J=1, beta=1/t, n_mc=n_mc)  # MC計算
    print(f"mean: {q_mean}")
    print(f"std : {q_std}")

if __name__ == '__main__':
    main()
