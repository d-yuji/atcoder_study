# coding:utf-8

def main():
    A,B,C = map(int,input().split())

    if A >= C and B <= C:
        print("Yes")
    elif A <= C and B >= C:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()