# coding:utf-8

def main():
    N,M = map(int,input().split())
    stores = []
    cost = 0
    number = 0

    for i in range(N):
        A,B = map(int,input().split())
        stores.append([A,B])
    stores.sort()

    for store in stores:
        if number + store[1] >= M:
            cost += (M - number)*store[0]
            break
        else:
            number += store[1]
            cost += store[0]*store[1]

    print(cost)

if __name__ == "__main__":
    main()