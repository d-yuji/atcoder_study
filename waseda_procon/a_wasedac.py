# coding: utf-8

# pythonのstrは文字単位で置き換えすると処理に時間がかかる
# 配列の添え字がｰ1になるとループしてしまうことに注意する

def main():
    s = input()
    i = 0
    s_list = list(s)
    while i < len(s)-1:
        if s_list[i] == "W" and s_list[i+1] == "A":
            s_list[i] = "A"
            s_list[i+1] = "C"
            if i > 0:
                i -= 1
        else:
            i += 1
    s = "".join(s_list)
    print(s)


if __name__ == "__main__":
    main()