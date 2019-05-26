# coding:utf-8

Black = "#"
White = "."

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def main():
    H, W = map(int, input().split())
    step = 0
    count = W*H
    memo = [[-1]*W for i in range(H)]
    steplist = []

    for y in range(H):
        temp_in = input()
        for x in range(W):
            if temp_in[x] == Black:
                memo[y][x] = 0
                count -= 1
                steplist.append([y, x])

    while count > 0:
        step += 1
        next_list = []
        for l_yx in steplist:
            for i in range(4):
                temp_x = l_yx[1] + dir_x[i]
                temp_y = l_yx[0] + dir_y[i]
                if temp_x >= 0 and temp_x < W and temp_y >= 0 and temp_y < H:
                    if memo[temp_y][temp_x] < 0:
                        memo[temp_y][temp_x] = step
                        count -= 1
                        next_list.append([temp_y, temp_x])
        steplist = next_list
    print(step)


if __name__ == "__main__":
    main()
