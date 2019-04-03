# coding:utf-8

def main():
    s = input()
    ans = 0
    for i in range(len(s)+1):
        for j in range(i,len(s)+1):
            temp = s[i:j]
            # print(i,j)
            # print(temp)
            if atgc_check(temp) and len(temp) > ans:
                ans = len(temp)
    print(ans)

def atgc_check(sub_s):
    for si in sub_s:
        if not si in ["A","T","G","C"]:
            return False
    return True

if __name__ == "__main__":
    main()