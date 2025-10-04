import heapq

def dijkstra(n, graph, src):
    dist = [float('inf')]*n
    dist[src] = 0
    parent = [-1]*n
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent

def build_path(parent, target):
    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

def main():
    n = 6
    graph = [[] for _ in range(n)]
    edges = [
        (0,1,7),(0,2,9),(0,5,14),(1,2,10),(1,3,15),(2,3,11),(2,5,2),(3,4,6),(4,5,9)
    ]
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    dist, parent = dijkstra(n, graph, 0)
    print("Distances", dist)
    print("Path to 4", build_path(parent, 4))

if __name__ == "__main__":
    main()
