# coding:utf-8


def main():
    S = input()
    RED = "0"
    BLUE = "1"
    red_count = 0
    blue_count = 0
    ans = 0

    for si in S:
        if si == RED:
            red_count += 1
        else:
            blue_count += 1

    if red_count == 0 or blue_count == 0:
        ans = 0
    else:
        ans = 2 * min(red_count, blue_count)

    print(ans)


if __name__ == "__main__":
    main()
