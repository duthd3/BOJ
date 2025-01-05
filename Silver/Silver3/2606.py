# dfs 가 한번 끝나면 +1

c_count = int(input())
twin_count = int(input())

graph = [ [] for i in range(c_count + 1)]

for i in range(0, twin_count):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
count = 0

visited = [0] * (c_count + 1)

def virus_dfs(graph, v, visited):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            virus_dfs(graph, i, visited)


virus_dfs(graph, 1, visited)
print(sum(visited) - 1)
