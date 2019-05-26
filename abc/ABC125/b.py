# coding:utf-8


def main():
    N = int(input())
    value = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    ans = 0
    for i in range(len(value)):
        if value[i] > cost[i]:
            ans += (value[i]-cost[i])
    print(ans)


if __name__ == "__main__":
    main()
