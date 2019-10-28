import collections


def visit(n):
    print(n)

def bfs(graph, root):
    seen, queue = set([root]), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)



if __name__ == '__main__':
    graph = {0: [1, 2, 3], 1: [2, 0], 2: [], 3:[]} 
    bfs(graph, 0)