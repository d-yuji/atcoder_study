# coding:utf-8


def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = []
    dp.append([0, -10**9-1])

    for i in range(0, N):
        temp_0 = max(dp[i][0]+A[i], dp[i][1]-A[i])
        temp_1 = max(dp[i][0]-A[i], dp[i][1]+A[i])
        dp.append([temp_0, temp_1])

    # print(dp)
    ans = dp[N][0]
    print(ans)


if __name__ == "__main__":
    main()
