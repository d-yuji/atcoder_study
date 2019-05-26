# coding:utf-8

moji = ["L", "R", "U", "D"]

dir_y = [0, 0, -1, 1]
dir_x = [-1, 1, 0, 0]


def main():
    H, W, N = map(int, input().split())
    sy, sx = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()
    takahashi_count = {}
    aoki_count = {}
    for i in moji:
        takahashi_count[i] = 0
        aoki_count[i] = 0

    for i in range(N):
        takahashi_count[s[i]] += 1
        aoki_count[t[i]] += 1

    print(takahashi_count)
    print(aoki_count)

    # 最適に行動
    # 互いにN回行動
    # 相手の文字列を知っている
    # 行動するかしないか
    # 青木くん=相手の行動の逆

    # スタートからのそれぞれの方向の距離
    len_l = sx
    len_r = W-sx
    len_u = sy
    len_d = H - sy
    print(len_l, len_r, len_u, len_d)


if __name__ == "__main__":
    main()
