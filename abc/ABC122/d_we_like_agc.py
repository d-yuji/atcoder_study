# coding:utf-8

# ACGTからなる
# 部分文字列AGCを持たない
    # AGC
# 隣接する2文字の入れかえを1回することでうえの条件に違反しない
    # ACG
    # GAC
    # A-GC
    # AG-C

# 4^N個の通り

# 動的計画法
    # 違反があったやつの打ち切り
    # すでに組み合わせの通りが分かっているやつの省略
# 再帰


DNA = ["A","C","G","T"]
ng3 = ["AGC","ACG","GAC"]
ng4 = ["ACGC","AGGC","ATGC","AGAC","AGTC"]
MOD = 10**9 +7

def main():
    N = int(input())
    memo = [{} for i in range(N+1)]

    ans = string_check("",0,N,memo)
    # print(memo)
    print(ans%MOD)


def string_check(nowstr,i,N,memo):
    # print(nowstr)
    slen = len(nowstr)
    if slen == 3:
        if nowstr in ng3:
            return 0
    if slen == 4:
        if nowstr[-3:] in ng3:
            return 0
        elif nowstr in ng4:
            return 0
    elif slen > 4:
        if nowstr[-3:] in ng3:
            return 0
        elif nowstr[-4:] in ng4:
            return 0
    if nowstr[-3:] in memo[i]:
        return memo[i][nowstr[-3:]]
    elif slen == N:
        return 1
    else:
        count = 0
        for s in DNA:
            count += string_check(nowstr+s,i+1,N,memo)
        if slen >= 4:
            memo[i][nowstr[-3:]] = count
        return count


if __name__ == "__main__":
    main()