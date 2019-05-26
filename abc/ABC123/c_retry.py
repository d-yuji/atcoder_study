# coding:utf-8
import math

# [考えること]
# シミュレーションで出来そうか考える
# Nの値から、計算量が無理そうなのを考える(貪欲法でやってもサンプル3が通らない)
# 計算量を減らす方法(動的計画法、MOD、二分探索、データ構造、定式化など)を考える
# シミュレーションの対として定式化を考える


def main():
    N = int(input())
    facilities = []
    for i in range(5):
        facilities.append(int(input()))
    print(math.ceil(N/min(facilities))+4)


if __name__ == "__main__":
    main()