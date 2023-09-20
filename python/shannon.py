import os
import sys
import argparse
import numpy as np
from collections import Counter  # 要素の個数を数えるコンテナクラス
from itertools import chain

# テキストファイルを読み込む関数
def read_file(filename):
    # ファイルの存在をチェック
    if not os.path.isfile(filename):  # (*1)
        print(f"{filename!r} does not exist")
        sys.exit(1)

    # テキストファイルを読み込み
    with open(filename, 'r', encoding='utf-8') as f:  # (*2)
        text = f.readlines()
    return text

# 情報エントロピーを計算する関数
def calc_entropy(text):
    print(f"Number of lines      : {len(text)}")

    chars = list(chain.from_iterable(text))  # 1文字ごとにバラす
    total = len(chars)  # 文字数
    print(f"Number of characters : {total}")

    c = Counter(chars)  # コンテナクラスCounterに文字のリストを与える (*3)
    assert total == np.sum(list(c.values()))  # 文字数を確認

    # 情報エントロピーを計算
    prob = np.array([n for n in c.values()]) / float(total)  # 確率 (*4)
    entropy = np.sum(-prob * np.log2(prob))  # (*5)
    print(f"Shannon entropy = {entropy:.4f}")

    # 文字の統計を出力
    print("Statistics of characters")
    for key, n in c.most_common():  # 文字とその出現回数を多い順に取り出す
        p = n / float(total) * 100
        print(f" {repr(key):6}  {n:7d}  {p:8.2f}%")  # (*6)

def main():
    # コマンドライン引数を解析
    parser = argparse.ArgumentParser()  # (*7)
    parser.add_argument('filename', help="filename of a text file.")
    args = parser.parse_args()
    print(args)

    txt = read_file(args.filename)  # テキストファイルを読み込み
    calc_entropy(txt)  # 情報エントロピーを計算

if __name__ == '__main__':
    main()
