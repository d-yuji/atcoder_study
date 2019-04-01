# coding: utf-8
def main():
    N = int(input())
    s = input()
    rcount = 0
    # bcount = 0

    for si in s:
        if si == 'R':
            rcount += 1
        # elif si == 'B':
        #     bcount += 1

    # 逐一チェックするより補集合をとったほうが少し早い
    bcount = N - rcount
    if rcount > bcount:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()