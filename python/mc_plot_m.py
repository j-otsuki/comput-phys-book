import numpy as np
import matplotlib.pyplot as plt

file_dat = "mc_t.dat"
file_fig = "mc_t.pdf"

data = np.loadtxt(file_dat)  # テキストファイルからデータを読み込み
print(data.shape)

# スライスを使って、2次元配列から1次元配列を抜き出す
t = data[:, 0]  # 温度
m_mean = np.absolute(data[:, 1])  # 磁化の平均値
m_std = data[:, 2]  # 統計誤差

# グラフ作成
fig, ax = plt.subplots()  # オブジェクト指向インターフェース
opt = dict(
    linestyle = 'solid',  # 線の種類
    linewidth = 1,  # 線の幅
    color = 'blue',  # 線の色
    ecolor = 'dimgray',  # 誤差棒の色
    elinewidth = 1,  # 誤差棒の線幅
    capsize = 2,  # 誤差棒の端の横棒の長さ
    marker = 'o',  # マーカーの種類
    markersize = 6,  # マーカーのサイズ
    markeredgewidth = 1,  # マーカーの淵の線幅
    markeredgecolor = 'darkblue',  # マーカーの淵の色
    markerfacecolor = 'lightblue',  # マーカーの内側の色
)
ax.errorbar(t, m_mean, m_std, **opt)  # 誤差棒付きグラフ
ax.axhline(y=0, color='k')  # x軸
# ax.set_xlim(left=0)
ax.set_xlabel(r"$t$")  # xラベル
ax.set_ylabel(r"$m$")  # yラベル
fig.savefig(file_fig)  # グラフをファイルに保存
