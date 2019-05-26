# coding: utf-8

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    K = int(input())
    # print(A,B,C,D,E,K)
    if E - A <= K: 
        print("Yay!")
    else:
        print(":(")


if __name__ == "__main__":
    main()