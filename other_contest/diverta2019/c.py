# coding:utf-8


def main():
    N = int(input())
    s_list = []
    for i in range(N):
        s_list.append(input().rstrip())

    ans = 0
    a_last = 0
    ab_count = 0
    b_start = 0
    for si in s_list:
        if si[0] == "B" and si[-1] == "A":
            ab_count += 1
        elif si[0] == "B":
            b_start += 1
        elif si[-1] == "A":
            a_last += 1

        for i in range(len(si)-1):
            if si[i] == "A" and si[i+1] == "B":
                ans += 1

    if ab_count > 0:
        ans += ab_count - 1
        if a_last == 0 and b_start == 0:
            pass
        else:
            ans = ans + min(a_last, b_start) + 1
    else:
        ans = ans + min(a_last, b_start)
    # print(ab_count, a_last, b_start)
    print(ans)


if __name__ == "__main__":
    main()
