# coding:utf-8
def main():
    # print("start")
    A,B = map(int,input().split())
    # print(A%4)
    point_A = A
    point_B = B
    if A%4 > 0:
        point_A = A - (A%4) + 4
    if B%4 > 0:
        point_B = B - (B%4)

    # print(point_A,point_B)
    # print()
    ans = 0
    for i in range(A,point_A):
        ans = ans ^ i

    for i in range(point_B,B+1):
        ans = ans ^ i
    print(ans)


if __name__ == "__main__":
    main()