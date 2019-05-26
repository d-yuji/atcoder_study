# coding: utf-8

def main():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    # print(B)
    ans = 0
    for i in range(N):
        temp_A = list(map(int,input().split()))
        temp = 0
        for j in range(M):
            temp += temp_A[j]*B[j]
        if temp + C > 0:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()