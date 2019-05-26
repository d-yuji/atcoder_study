def main():
    N, M = map(int, input().split())
    li_max = 0
    ri_min = 10 ** 5
    for i in range(M):
        li, ri = map(int, input().split())
        if li > li_max:
            li_max = li
        if ri < ri_min:
            ri_min = ri
    ans = ri_min - li_max + 1
    if ans < 0:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()
