# coding:utf-8


def main():
    A, B, K = map(int, input().split())
    ans = []
    ans.append(1)
    for i in range(2, max(A, B)+1):
        if A % i == 0 and B % i == 0:
            ans.append(i)
    print(ans[-K])


if __name__ == "__main__":
    main()
