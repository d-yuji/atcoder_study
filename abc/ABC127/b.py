def main():
    r, d, x = map(int, input().split())
    a = d/(1-r)
    ans = [x]
    for i in range(10):
        ans.append(r*(ans[-1])-d)
    # print(ans[1:])
    for i in range(1, 11):
        print(ans[i])


if __name__ == "__main__":
    main()
