---
layout: default
---

<!-- このページは、書籍「**Pythonによる計算物理**」大槻純也 著（森北出版）のサポートページです。本に掲載されているソースコードや更新情報を提供します。
出版社のページは[こちら](https://www.morikita.co.jp/books/mid/017081)。 -->

<!-- ![表紙](9784627170810.jpg) -->
<!-- <img src="9784627170810.jpg" width=300px> -->


<!-- * TOC
{:toc} -->

## 本について

著者のWebサイト[「pythonで学ぶ計算物理」](https://www.physics.okayama-u.ac.jp/~otsuki/lecture/CompPhys2/index.html)を元に書籍化したものです。
Webサイトとの主な違いは以下の通りです。

- アルゴリズムの解説をしています。
- 物理や結果の解説を全体的に詳しくしました。
- コードを見直しました。（Python3を前提にしたり、なるべくNumPyを使うようにしたり）
- 例題を追加しました。（Webサイトで「作成中」と書いてある項目）
- 例題の最後に「課題」があります。

Webサイトと本でソースコードに違いがある場合は、ほとんどの場合、本の方が新しいです。書籍出版後の進展（Python3.10以降ではこういう書き方もできるよ、など）は、このページで取り入れていこうと思います。

森北出版のページは[こちら](https://www.morikita.co.jp/books/mid/017081)。

## ダウンロード

本に掲載してるPythonプログラムのソースコードを掲載します。
なお、編集段階で行った修正（主にコメント部分）は、ファイルには反映されていない場合があるのでご了承ください。

説明欄に「非掲載」と書かれているものは、本に掲載されていない関連プログラムです。プログラムの詳細は説明欄を見てください。

まとめてダウンロードしたい場合には「一括ダウンロード」、個別にダウンロードしたい場合またはファイルを閲覧したい場合には「個別ダウンロード」を参照してください。

### 一括ダウンロード

[GitHubリポジトリ](https://github.com/j-otsuki/comput-phys-book)に全てのソースコード（このページのソースも含む）を置いてあります。
緑色の「Code」ボタン → 「Download ZIP」でダウンロードできます。

### 個別ダウンロード

以下のファイル一覧からファイル名をクリックすると、GitHub上でファイルを閲覧できます。ダウンロードしたい場合には、そのページで右上のダウンロードボタン（下矢印のアイコン）をクリックしてください。

| 掲載場所 | ファイル名 | 説明 |
| -----   | ---------- | --- |
| 2.3節 | [logistic_euler.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/logistic_euler.py) | ロジスティックス方程式（オイラー法） |
| | [logistic_euler_mod.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/logistic_euler_mod.py) | 【非掲載】（P.27に一部掲載）logistic_euler.pyの``step_forward``関数を修正オイラー法に変更したもの |
| | [logistic_runge_kutta.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/logistic_runge_kutta.py) | 【非掲載】（P.27に一部掲載）logistic_euler.pyの``step_forward``関数を4次のルンゲ・クッタ法に変更したもの |
| | [logistic_solve_ivp.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/logistic_solve_ivp.py) | ロジスティックス方程式（SciPyの``solve_ivp``関数を使用） |
| 2.4節 | [newton.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/newton.py) | ニュートン方程式 |
| | [newton_angles.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/newton_angles.py) | 初期角度を変化 |
| 2.5節 | [llg_0dim.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/llg_0dim.py) | LLG方程式（単一磁気モーメント） |
| | [llg_1dim.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/llg_1dim.py) | LLG方程式（1次元） |
| 3.4節 | [differential.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/differential.py) | 差分法 |
| | [kdv_solve_ivp.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/kdv_solve_ivp.py) | KdV方程式 |
| | [kdv_anim_artist.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/kdv_anim_artist.py) | アニメーション作成 |
| | [kdv_anim_func.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/kdv_anim_func.py) | 【非掲載】kdv_anim_artist.pyで``ArtistAnimation``クラスの代わりに``FuncAnimation``クラスを使用した場合 |
| | [kdv_plot.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/kdv_plot.py) | 【非掲載】アニメーションの全てのコマを連番の画像ファイルとして出力するプログラム（図3.5の作成に使用） |
| 3.5節 | [schr.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/schr.py) | 時間依存シュレディンガー方程式（関数のみ） |
| | [schr_wall.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/schr_wall.py) | 時間依存シュレディンガー方程式（ポテンシャル障壁） |
| | [schr_plot.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/schr_plot.py) | コマ毎のグラフを作成 |
| | [schr_anim.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/schr_anim.py) | 【非掲載】時間依存シュレディンガー方程式の解からアニメーションを作成するプログラム（図3.7の動画） |
| 3.8節 | [poisson.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/poisson.py) | ポアソン方程式（点電荷） |
| | [poisson_plot.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/poisson_plot.py) | グラフ作成 |
| | [poisson_circle.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/poisson_circle.py) | ポアソン方程式（点電荷＋導体円柱） |
| | [poisson_circle_plot.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/poisson_circle_plot.py) | 【非掲載】導体円柱がある場合のポアソン方程式の解を図示するプログラム（図3.14の作成に使用） |
| 4.3節 | [anharmonic.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/anharmonic.py) | 時間に依存しないシュレディンガー方程式（非調和振動子） |
| 4.4節 | [spin.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/spin.py) | スピン演算子の交換関係 |
| | [spin_diag.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/spin_diag.py) | スピン演算子の対角化 |
| 4.5節 | [two_spins.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/two_spins.py) | ハイゼンベルグ模型（2スピン） |
| | [three_spins.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/three_spins.py) | ハイゼンベルグ模型（3スピン） |
| 4.6節 | [hubbard_1site.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/hubbard_1site.py) | ハバード模型（1サイト） |
| | [hubbard_2site.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/hubbard_2site.py) | ハバード模型（2サイト） |
| | [hubbard_2site_Udep.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/hubbard_2site_Udep.py) | 【非掲載】2サイトハバード模型のUを変化させて計算し、結果を図示するプログラム（図4.6の作成に使用） |
| 5.2節 | [shannon.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/shannon.py) | シャノンの情報エントロピー |
| 5.4節 | [bec_integ.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/bec_integ.py) | ボーズ・アインシュタイン積分 |
| 5.6節 | [bec.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/bec.py) | ボーズ・アインシュタイン凝縮 |
| | [bec_t.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/bec_t.py) | 温度変化 |
| 5.7節 | [ising_mf.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/ising_mf.py) | イジング模型の平均場近似 |
| | [ising_mf_t.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/ising_mf_t.py) | 温度変化 |
| 5.8節 | [mc.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/mc.py) | イジング模型のモンテカルロ法 |
| | [mc_t.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/mc_t.py) | 温度変化 |
| | [mc_plot_m.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/mc_plot_m.py) | グラフ作成 |

## 正誤表

[PDFファイル（2024年1月10日時点）](corrections/corrections.pdf)

## 問い合わせ

本の内容やソースコードに関する質問は、GitHubリポジトリの[Issues](https://github.com/j-otsuki/comput-phys-book/issues)に投稿してください。

質問と回答は公開されます。質問と回答を共有することで、同じ疑問を持った人が、その回答を参照できるようになることが大きなメリットです。また、著者が同じ質問に繰り返し答えなくて済むため、この形式での質問にご協力お願いします。

ひとりが疑問に思ったことは、他の人も疑問に思っています。みんなのためと思って、ぜひ質問お願いします。

過去の投稿の閲覧：
- [Issues](https://github.com/j-otsuki/comput-phys-book/issues)にアクセス。
- 「Open」以下に、未解決の質問一覧
- 「Closed」以下に、解決済みの質問一覧

投稿の手順：
- GitHubにアカウントを作成。
- [Issues](https://github.com/j-otsuki/comput-phys-book/issues)にアクセス。
- 緑色の「New issue」ボタンを押す。
- 「Title」に見出しを、「Write」以下に本文を書く。「Preview」で確認する。
- 緑色の「Submit new issue」ボタンを押して投稿。
