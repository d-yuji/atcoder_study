def main():
    A, B = map(int, input().split())
    ans = 0
    if A <= 5:
        ans = 0
    elif A >= 6 and A <= 12:
        ans = int(B/2)
    else:
        ans = B
    print(ans)


if __name__ == "__main__":
    main()
