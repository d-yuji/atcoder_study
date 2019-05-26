# coding:utf-8

# memo = []

def main():
    N,Q = map(int,input().split())
    S = input()
    t = [0] *(N+1)
    for i in range(N):
        if S[i:i+2] == "AC":
            t[i+1] = t[i] + 1
        else:
            t[i+1] = t[i]
    # for i in range(N-1):
    #     if S[i:i+2] == "AC":
    #         memo.append(i)
    # print(memo)

    for i in range(Q):
        li,ri = map(int,input().split())
        print(t[ri-1] - t[li-1])
        # count = len(memo)
        # 両方の範囲に入る最初と最後
        # print(li,ri)
        # for i in range(li-1,ri-1):
        #     # print("debug"+str(i))
        #     if S[i] == "A" and S[i+1] == "C":
        #         count += 1
        #         start = i
        #         break
        # if start < 0:
        #     count = 0
        # else: 
        #     for i in reversed(range(li-1,ri+1)):
        #         if S[i-1] == "A" and S[i] == "C":
        #             end = i-1
        #             break
        #     print(start,end)
        #     count = memo.index(end) - memo.index(start) + 1


        # for i in range(len(memo)):
        #     if ac_check(i,li,ri):
        #         start = i
        #         break
        # if start < 0:
        #     count = 0
        # else:
        #     for i in reversed(range(len(memo))):
        #         if ac_check(i,li,ri):
        #             end = i
        #             break
        #     # print(start,end)
        #     count = count - (start) - (len(memo)-end) + 1
        # print(count)

# def ac_check(i,li,ri):
#     if memo[i] >= li-1 and memo[i]+1 <= ri-1:
#         return True
#     return False

# def ac_check(sub_s):
#     count = 0
#     for i in range(len(sub_s)-1):
#         if sub_s[i:i+2] == "AC":
#             count += 1
#     return count


if __name__ == "__main__":
    main()