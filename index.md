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

## ダウンロード（出版後にダウンロード可）

### 一括ダウンロード

[GitHubリポジトリ](https://github.com/j-otsuki/comput-phys-book)に全てのソースコード（このページのソースも含む）を置いてあります。
緑色の「Code」ボタン → 「Download ZIP」でダウンロードできます。

### 個別ダウンロード

以下のファイル一覧からファイル名をクリックすると、GitHub上でファイルを閲覧できます。ダウンロードしたい場合には、そのページで右上のダウンロードボタン（下矢印のアイコン）をクリックしてください。

| 掲載場所 | ファイル名 | 説明 |
| -----   | ---------- | --- |
| **第2章 古典力学** |
| 2.3節 | [logistic_euler.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/logistic_euler.py) | |
| | logistic_euler_mod.py | 一部掲載 |
| | logistic_runge_kutta.py | 一部掲載 |
| | [logistic_solve_ivp.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/logistic_solve_ivp.py) |    |
| 2.4節 | [newton.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/newton.py) |    |
| | [newton_angles.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/newton_angles.py) |    |
| 2.5節 | [llg_0dim.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/llg_0dim.py) |    |
| | [llg_1dim.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/llg_1dim.py) |    |
| **第3章 振動・波動** |
| 3.4節 | [differential.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/differential.py) |    |
| | [kdv_solve_ivp.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/kdv_solve_ivp.py) |    |
| | [kdv_anim_artist.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/kdv_anim_artist.py) |    |
| | kdv_anim_func.py | 掲載なし |
| | kdv_plot.py | 掲載なし |
| 3.5節 | [schr.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/schr.py) |    |
| | [schr_wall.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/schr_wall.py) |    |
| | [schr_plot.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/schr_plot.py) |    |
| | schr_anim.py | 掲載なし |
| 3.8節 | [poisson.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/poisson.py) |    |
| | [poisson_plot.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/poisson_plot.py) |    |
| | [poisson_circle.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/poisson_circle.py) |    |
| | poisson_circle_plot.py | 図3.14   |
| **第4章 量子力学** |
| 4.3節 | [anharmonic.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/anharmonic.py) |    |
| 4.4節 | [spin.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/spin.py) |    |
| | [spin_diag.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/spin_diag.py) |    |
| 4.5節 | [two_spins.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/two_spins.py) |    |
| | [three_spins.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/three_spins.py) |    |
| 4.6節 | [hubbard_1site.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/hubbard_1site.py) |    |
| | [hubbard_2site.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/hubbard_2site.py) |    |
| | hubbard_2site_Udep.py | 掲載なし |
| **第4章 量子統計力学** |
| 5.2節 | [shannon.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/shannon.py) |    |
| 5.4節 | [bec_integ.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/bec_integ.py) |    |
| 5.6節 | [bec.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/bec.py) |    |
| | [bec_t.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/bec_t.py) |    |
| 5.7節 | [ising_mf.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/ising_mf.py) |    |
| | [ising_mf_t.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/ising_mf_t.py) |    |
| 5.8節 | [mc.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/mc.py) |    |
| | [mc_t.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/mc_t.py) |    |
| | [mc_plot_m.py](https://github.com/j-otsuki/comput-phys-book/blob/main/python/mc_plot_m.py) |    |

## 正誤表

いまのところ誤植は見つかっていません。見つかり次第、ここに記載していきます。

## 問い合わせ

本の内容やソースコードに関する質問は、GitHubリポジトリの[Issues](https://github.com/j-otsuki/comput-phys-book/issues)に投稿してください。

質問と回答は公開されます。質問と回答を共有することで、同じ疑問を持った人が、その回答を参照できるようになることが大きなメリットです。また、著者が同じ質問に繰り返し答えなくて済むため、この形式での質問にご協力お願いします。

ひとりが疑問に思ったことは、他の人も疑問に思っています。みんなのためと思って、ぜひ質問お願いします。

過去の投稿の閲覧：
- [Issues](https://github.com/j-otsuki/comput-phys-book/issues)にアクセス。
- 「Open」以下に、未解決の質問一覧（まだありません）
- 「Closed」以下に、解決済みの質問一覧（まだありません）

投稿の手順：
- GitHubにアカウントを作成。
- [Issues](https://github.com/j-otsuki/comput-phys-book/issues)にアクセス。
- 緑色の「New issue」ボタンを押す。
- 「Title」に見出しを、「Write」以下に本文を書く。「Preview」で確認する。
- 緑色の「Submit new issue」ボタンを押して投稿。
