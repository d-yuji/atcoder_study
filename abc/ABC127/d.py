def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    # A.sort()
    all_list = []
    for a in A:
        all_list.append([a,1])
    
    for i in range(M):
        bi, ci = map(int, input().split())
        all_list.append([ci,bi])
    all_list.sort(reverse=True)
    count = N
    while count > 0:
        # index = binary_search(ci, A)
        # A[index:index] = l
        # for j in range(bi):
        #     A.append(ci)
    # A.sort(reverse=True)
    # ans = sum(A[-N:])
    print(ans)


def binary_search(key, l):
    left = 0
    right = len(l)-1
    while(right >= left):
        mid = int(left + (right - left)/2)
        if l[mid] == key:
            return mid
        elif l[mid] > key:
            right = mid - 1
        elif l[mid] < key:
            left = mid + 1
    return left


if __name__ == "__main__":
    main()
