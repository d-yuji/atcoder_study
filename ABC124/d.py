# coding:utf-8

def main():
    N,K = map(int,input().split())
    S = input()

    ans = N
    able = False
    if "0" in S:
        while ans >= K :
            for i in range(N-ans+1):
                sub_s = S[i:i+ans]
                # print(sub_s)
                if not "0" in sub_s:
                    able = True
                    break
                else:
                    index = sub_s.index("0")
                    temp = "0"
                    count = 0
                    # print(index)
                    for j in range(index,len(sub_s)):
                        if temp != sub_s[j]:
                            temp = sub_s[j]
                            count += 1
                    if temp == "1":
                        count -= 1
                    # print(count)
                    if count <= K:
                        able = True
                        break
            if able:
                break
            else:
                ans -= 1
    print(ans)

if __name__ == "__main__":
    main()