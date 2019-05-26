#include <string>
#include <iostream>
#include <cstdio>
#include <queue>
#include <tuple>

using namespace std;

char Black = '#';
char White = '.';
int dir_x[4] = {1, 0, -1, 0};
int dir_y[4] = {0, 1, 0, -1};

int main(int argc, char const *argv[])
{
    int H = 0;
    int W = 0;
    int step = 0;
    if (scanf("%d %d", &H, &W) < 2)
    {
        fprintf(stderr, "error: ill-formed fraction.\n");
        exit(1);
    }
    int memo[1001][1001] = {};
    int count = H * W;
    queue<tuple<int, int>> q;
    // printf("debug");
    for (int y = 0; y < H; y++)
    {
        string temp;
        cin >> temp;
        for (int x = 0; x < W; x++)
        {
            if (temp[x] == Black)
            {
                memo[y][x] = 0;
                q.push(make_tuple(y, x));
                count--;
            }
            else
            {
                memo[y][x] = -1;
            }
        }
    }
    // printf("debug");
    while (count > 0)
    {
        step++;
        queue<tuple<int, int>> next_queue;
        while (!q.empty())
        {
            tuple<int, int> temp_tuple = q.front();
            q.pop();
            int ly = get<0>(temp_tuple);
            int lx = get<1>(temp_tuple);
            for (int i = 0; i < 4; i++)
            {
                int temp_x = lx + dir_x[i];
                int temp_y = ly + dir_y[i];
                if (temp_x >= 0 && temp_x < W && temp_y >= 0 && temp_y < H)
                {
                    if (memo[temp_y][temp_x] < 0)
                    {
                        memo[temp_y][temp_x] = step;
                        count -= 1;
                        next_queue.push(make_tuple(temp_y, temp_x));
                    }
                }
            }
        }
        q = next_queue;
    }

    printf("%d\n", step);
    return 0;
}
