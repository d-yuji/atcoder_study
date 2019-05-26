# coding:utf-8


def main():
    R, G, B, N = map(int, input().split())
    ans = 0
    rgb_list = [R, G, B]
    rgb_list.sort()
    for r in range(int(N/rgb_list[-1])+1):
        tempN = N - r * rgb_list[-1]
        # print(r)
        if tempN == 0:
            ans += 1
            # print(r, 0, 0)
            continue
        for g in range(int(N/rgb_list[-2])+1):
            # print(g)
            tempN2 = tempN - g * rgb_list[-2]
            if tempN2 == 0:
                ans += 1
                continue
            elif tempN2 < 0:
                break
            else:
                if tempN2 % rgb_list[0] == 0:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
