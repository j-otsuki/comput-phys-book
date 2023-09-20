import numpy as np
from mc import run_mc  # mc.pyから関数をインポート

def main():
    system = (8, 8)  # 系のサイズ
    tmin, tmax = 0.5, 5.0  # 温度範囲
    nt = 10  # 温度点の数
    n_measure = 1000  # ビンあたりの測定回数
    n_bin = 10  # ビンの数
    n_warmup = 100  # ウォームアップの回数
    filename = "mc_t.dat"  # 保存ファイル名

    ts = np.linspace(tmin, tmax, nt)  # 温度メッシュ
    qs = []  # 結果を保存するリスト
    for t in ts:
        print("\n================")
        print(f"T = {t}")
        n_mc = (n_bin, n_measure, n_warmup)
        q_mean, q_std = run_mc(system, J=1, beta=1/t, n_mc=n_mc)  # MC計算
        print(f"mean: {q_mean}")
        print(f"std : {q_std}")
        qs.append([q_mean, q_std])  # 結果をリストqsに追加

    print("\n================")
    print("finish")

    # リストqsをNumPy配列に変換して整形
    qs = np.array(qs)  # shape=(nt, 2, nq); nqは物理量の個数
    qs = np.transpose(qs, [0, 2, 1])  # -> (nt, nq, 2)
    qs = qs.reshape((nt, -1))  # -> (t, 2*nq)
    print(qs.shape)

    # 結果をテキストファイルに保存
    #   format: T q1_mean q1_std q2_mean q2_std ...
    np.savetxt(filename, np.hstack([ts[:, None], qs]))  # (*1)
    print(f"Output results into '{filename}'")

if __name__ == '__main__':
    main()
