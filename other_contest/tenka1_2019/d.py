# coding:utf-8

def main():
    N = int(input())
    a = []
    MOD_X = 998244353
    R = 0
    G = 0
    B = 0
    ans = MOD_X

    for i in range(N):
        a.append(int(input()))
    
    S = sum(a)


    ans = ans % MOD_X
    print(ans)
    return


if __name__ == "__main__":
    main()