# coding:utf-8
import fractions


def main():
    N = int(input())
    num = list(map(int, input().split()))

    gcd_max = 0
    gcd_list_front = []
    gcd_list_back = []

    gcd_list_front.append(num[0])
    gcd_list_back.append(num[-1])

    for i in range(1, N-1):
        gcd_list_front.append(fractions.gcd(gcd_list_front[i-1], num[i]))
        gcd_list_back.append(fractions.gcd(gcd_list_back[i-1], num[-i-1]))

    gcd_list_back.reverse()
    gcd_max = max(gcd_list_back.pop(0), gcd_list_front.pop(-1))

    for i in range(len(gcd_list_front)):
        temp_gcd = fractions.gcd(gcd_list_front[i], gcd_list_back[i])
        if temp_gcd > gcd_max:
            gcd_max = temp_gcd

    print(gcd_max)
    return


if __name__ == "__main__":
    main()
