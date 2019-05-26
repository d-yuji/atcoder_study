import random
import csv


def main():
    W = 50
    H = 50
    N = 3
    min_i = 1
    max_i = 10**3
    path_w = "mytest"

    output = []
    output.append([W, H, N])

    for i in range(H):
        output.append([random.randint(min_i, max_i) for i in range(W)])

    with open(path_w, mode='w') as f:
        writer = csv.writer(f, delimiter=" ")
        writer.writerows(output)

    print("finish")


if __name__ == "__main__":
    main()
