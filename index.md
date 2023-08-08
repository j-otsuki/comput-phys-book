<!-- # 「Pythonによる計算物理」サポートページ -->

このページは、「Pythonによる計算物理」大槻純也 著（森北出版）のサポートページです。出版社のページはこちら。

## 本について

著者のWebサイト「Pythonで学ぶ計算物理」を書籍化したものです。
Webサイトとの主な違いは以下の通りです。

- アルゴリズムの解説を加えました。
- 物理や結果の解説を全体的に詳しくしました。
- コードを見直しました。（Python3を前提にしたり、なるべくNumPyを使うようにしたり）
- 例題を追加しました。（Webサイトで「作成中」と書いてある項目）

Webサイトと本でソースコードに違いがある場合は、ほとんどの場合、本の方が新しいです。書籍出版後の進展（Python3.10以降ではこういう書き方もできるよ、など）は、このページで取り入れていこうと思います。

## ソースファイルのダウンロード

### ファイル一覧

- 第2章 古典力学
    - logistic_euler.py
    - logistic_euler_mod.py
    - logistic_runge_kutta.py
    - logistic_solve_ivp.py
    - newton.py
    - newton_angles.py
    - llg_0dim.py
    - llg_1dim.py

- 第3章 振動・波動
    - differential.py
    - kdv_solve_ivp.py
    - kdv_anim_artist.py
    - kdv_anim_func.py 掲載なし
    - kdv_plot.py 掲載なし
    - schr.py
    - schr_wall.py
    - schr_plot.py
    - schr_anim.py 掲載なし
    - poisson.py
    - poisson_plot.py
    - poisson_circle.py
    - poisson_circle_plot.py 掲載なし

- 第4章　量子力学
    - anharmonic.py
    - spin.py
    - spin_diag.py
    - two_spins.py
    - three_spins.py
    - three_spins_chiral.py 掲載なし
    - hubbard_1site.py
    - hubbard_2site.py
    - hubbard_2site_Udep.py 掲載なし

- 第5章　量子統計力学
    - shannon.py
    - bec_integ.py
    - bec.py
    - bec_t.py
    - ising_mf.py
    - ising_mf_t.py
    - mc.py
    - mc_t.py
    - mc_plot_m.py


### GitHubからダウンロード（上級者向け）

GitHubリポジトリに全てのソースコードをおいてあります。

**https://github.com/j-otsuki/comput-phys-book**


## 正誤表

いまのところ誤植は見つかっていません。見つかり次第、ここに記載していきます。

## 問い合わせ

本の内容やソースコードに関する質問は、GitHubリポジトリの[**Issues**](https://github.com/j-otsuki/comput-phys-book/issues)に投稿してください。

質問と回答は公開されます。質問と回答を共有することで、同じ疑問を持った人が、その回答を参照できるようになることが大きなメリットです。また、著者が同じ質問に繰り返し答えなくて済むため、この形式での質問にご協力お願いします。

ひとりが疑問に思ったことは、他の人も疑問に思っています。みんなのためと思って質問してください。

過去の投稿の閲覧：
- [**Issues**](https://github.com/j-otsuki/comput-phys-book/issues)にアクセス。
- 「Open」以下に、未解決の質問一覧（まだありません）
- 「Closed」以下に、解決済みの質問一覧（まだありません）

投稿の手順：
- GitHubにアカウントを作成。
- [**Issues**](https://github.com/j-otsuki/comput-phys-book/issues)にアクセス。
- 緑色の「New issue」ボタンを押す。
- 「Title」に見出しを、「Write」以下に本文を書く。「Preview」で確認する。
- 緑色の「Submit new issue」ボタンを押して投稿。
