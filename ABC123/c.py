# coding: utf-8
import copy

def main():
    N = int(input())
    people = []
    for i in range(5):
        people.append(int(input()))
    people.append(0)
    ans = 0
    temp = [0]*6
    temp[0] = N
    temp_next = copy.deepcopy(temp)
    print(people)
    # print(temp)
    while temp[5] < N:
        ans += 1
        move = [0]*6
        for i in range(5):
            if temp[i] > people[i]:
                move[i] = people[i]
            else:
                move[i] = temp[i]
        for i in range(6):
            if i == 0:
                temp_next[i] = temp[i] - move[i]
            else:
                temp_next[i] = temp[i] - move[i] + move[i-1]
        temp = copy.deepcopy(temp_next)

    print(ans)
    print(10000000007/2)




    print(ans)

if __name__ == "__main__":
    main()