# coding:utf-8

def main():
    N = int(input())
    s = input()
    count_white = 0
    count_black = 0
    count_border = N

    if (not "." in s) or (not "#" in s):
        print(0)
        return

    for i in s:
        if i == ".":
            count_white += 1
        elif i == "#":
            count_black += 1

    patern_border_white = 0
    patern_border_black = 0
    temp_border_white = 0
    temp_border_black = 0
    
    for i in range(N-1):
        if i == 0:
            if s[0] == "#":
                temp_border_white = 1
                temp_border_black = count_white

            else:
                temp_border_white = 0
                temp_border_black = count_white -1

        else :
            if s[i] == "#":
                temp_border_white = patern_border_white + 1
                temp_border_black = patern_border_black
            else :
                temp_border_white = patern_border_white
                temp_border_black = patern_border_black - 1

        if count_border > temp_border_white + temp_border_black :
            count_border = temp_border_white + temp_border_black

        patern_border_white = temp_border_white
        patern_border_black = temp_border_black

    print(min(count_white,count_black,count_border))
    return

if __name__ == "__main__":
    main()