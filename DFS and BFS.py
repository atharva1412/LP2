g = {'A': ['B', 'C', 'D'], 
     'B': ['A', 'E', 'F'], 
     'C': ['A', 'G', 'H'], 
     'D': ['A', 'I'], 
     'E': ['B', 'J'], 
     'F': ['B', 'K'], 
     'G': ['C', 'L'], 
     'H': ['C', 'M'], 
     'I': ['D', 'N', 'O'], 
     'J': ['E'], 
     'K': ['F'], 
     'L': ['G'], 
     'M': ['H'], 
     'N': ['I'], 
     'O': ['I']
}
print("DFS of the graph is")
def dfs(g,s):
    vis[s]=1
    print (s)
    for c in g[s]:
        if not vis[c]:
            dfs(g,c)
vis = {node: 0 for node in g}
dfs(g,'A')


print("BFS of the graph is")
from collections import deque

def bfs(g, s):
    queue, vis = deque([s]), set([s])
    while queue:
        cur = queue.popleft()
        print(cur)
        for neighbor in g[cur]:
            if neighbor not in vis:
                queue.append(neighbor)
                vis.add(neighbor)

bfs(g, 'A')