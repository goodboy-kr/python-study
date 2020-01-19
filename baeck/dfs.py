world = {'A': set(['B']),
         'B': set(['A', 'D', 'E']),
         'C': set(),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['E'])}


def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(dfs(world,'A'))