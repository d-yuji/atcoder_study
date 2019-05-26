# coding:utf-8


def main():
    N = int(input())
    ans = 0
    divisors = make_divisors(N)
    for d in divisors:
        m = d - 1
        if m > 0 and N % m == N//m:
            ans += m
    print(ans)
    return


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


if __name__ == "__main__":
    main()
