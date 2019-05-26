# coding:utf-8
import math

def main():
    N = int(input())
    facilities = []
    for i in range(5):
        facilities.append(int(input()))
    citys = [0]*6
    citys[0] = N

    ans = 0
    while citys[5] < N :
        for i in reversed(range(5)):
            if citys[i] >= facilities[i]:
                citys[i+1] += facilities[i]
                citys[i] -= facilities[i]
            elif citys[i] > 0 :
                citys[i+1] += citys[i]
                citys[i] = 0
        ans += 1
        # print(citys)
    print(ans)


if __name__ == "__main__":
    main()