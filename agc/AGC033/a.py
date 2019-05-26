# coding:utf-8

import copy

Black = "#"
White = "."

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def main():
    H, W = map(int, input().split())
    masu = []
    for i in range(H):
        masu.append(input().rstrip())
    step = 0
    count = W*H
    memo = [[-1]*W for i in range(H)]

    steplist = []
    for y in range(H):
        for x in range(W):
            if masu[y][x] == Black:
                memo[y][x] = 0
                count -= 1
                steplist.append([y, x])

    while count > 0:
        temp_step = step
        step += 1
        next_list = []
        for l in steplist:
            y = l[0]
            x = l[1]
            for i in range(4):
                temp_x = x + dir_x[i]
                temp_y = y + dir_y[i]
                if temp_x >= 0 and temp_x < W and temp_y >= 0 and temp_y < H and memo[temp_y][temp_x] < 0:
                    memo[temp_y][temp_x] = step
                    count -= 1
                    next_list.append([temp_y, temp_x])
        steplist = copy.deepcopy(next_list)
    print(step)


if __name__ == "__main__":
    main()
