# coding: utf-8

def main():
    time = []
    time_zero = []
    for i in range(5):
        temp = int(input())
        if temp%10 == 0:
            time_zero.append(temp)
        else:
            time.append([temp,temp%10])
    sort_list = sorted(time, key=lambda x:x[1],reverse=True)

    # print(sort_list)
    ans = 0
    
    for i in time_zero:
        ans += i    
    for i in sort_list:
        if ans > 0 and ans%10 > 0:
            ans +=  (10 - ans%10)
        ans += i[0]
    print(ans)


if __name__ == "__main__":
    main()