# coding:utf-8

def main():
    s = input()
    one_start = 0
    zero_start = 0

    for i in range(len(s)):
        if i%2 == 0:
            if s[i] != "0":
                one_start += 1
        else:
            if s[i] != "1":
                one_start += 1

    for i in range(len(s)):
        if i%2 == 0:
            if s[i] != "1":
                zero_start += 1
        else:
            if s[i] != "0":
                zero_start += 1

    print(min(one_start,zero_start))

if __name__ == "__main__":
    main()