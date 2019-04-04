# coding:utf-8

# 2*M  mod 10 = 0だからMは5の倍数
# 0~9

# すべてが0でないもしくは5がない -> No
# 1*2 mod 10 2
# 2*2 mod 10 4
# 3*2 mod 10 6
# 4*2 mod 10 8
# 5*2 mod 10 0

# 6*2 mod 10 2 (1)
# 7*2 mod 10 4 (1)
# 8*2 mod 10 6 (2)
# 9*2 mod 10 8 (3)

# 5がのこるように書き換える

def main():
    H,W = map(int,input().split())
    masu=[]
    for i in range(H):
        temp = input().split()
        masu.append([int(s) for s in temp])
    # print(masu)

    all_zero_flag = True
    for i in masu:
        if sum(i) > 0:
            all_zero_flag = False
            break
    if all_zero_flag:
        print("Yes 0")
        return

    five_exist_flag = False
    for i in masu:
        if 5 in i:
            five_exist_flag = True
            break
    if not five_exist_flag:
        print("No")
        return

    ans = 99

    if H == 1 and W == 1:
        ans = 1
    elif H == 1:
        for i in range(W):
            if masu[0][i] == 5:
                a = max(masu[0][:i])
                b = max(masu[0][i+1:])
                ans = compare_num_of_operation(a,b,ans)
    elif W == 1:
        for i in range(H):
            if masu[i][0] == 5:
                a = max(masu[:i])
                b = max(masu[i+1:])
                ans = compare_num_of_operation(a[0],b[0],ans)
    else:
        masu_max = 5
        for i in masu:
            if masu_max < max(i):
                masu_max = max(i)
        ans = calc_operation(masu_max)+1
    print("Yes "+str(ans))

def compare_num_of_operation(a,b,ans):
    temp_min = calc_operation(a) + calc_operation(b)+1
    if ans > temp_min:
        return temp_min
    else: 
        return ans

def calc_operation(masu_max):
    if masu_max in [6,7]:
        return 1
    elif masu_max == 8:
        return 2
    elif masu_max == 9:
        return 3
    else:
        return 0

if __name__ == "__main__":
    main()