# coding:utf-8
def main():
    N, M = map(int, input().split())
    bridges = []
    ans = [0] * M

    checklist = {}
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            checklist[(i, j)] = False

    for i in range(M):
        Ai, Bi = map(int, input().split())
        bridges.append([Ai, Bi])

    ans[M-1] = int(N*(N-1)/2)
    print(ans)
    states = [False]*(N+1)
    # all_states =  [[False]*(N+1) for i in range(N+1)]
    # print(all_states)
    # print(states)
    # for i in range(1,N+1):
    #     states = dfs(bridges,i,states)

    # print(states)
    print(checklist)
    print(bridges)


def dfs(graph, start, now, checklist):
    if start <= now:
        checklist[(start, now)] = True
    else:
        checklist[(now, start)] = True

    for node in graph[now]:
        if not states[node]:
            states = dfs(graph, node, states)
    return states


if __name__ == "__main__":
    main()
