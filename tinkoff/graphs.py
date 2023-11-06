n, m = map(int, input().split())

graph = dict[int, list[tuple[int,int]]]
G: graph = {}
G_s: graph = {}

def get_connected_components(G: graph):
    marked = set()
    result = []
    for v in G:
        if v in marked:
            continue        
        marked.add(v)
        
        current_component = [v,]
        
        stack = [v]
        
        while len(stack) > 0:
            v = stack.pop()
            for (u, w) in G[v]:
                if u not in marked:
                    stack.append(u)
                    marked.add(u)
                    current_component.append(u)
        result.append(current_component)
        
    return result            
        



for _ in range(m):
    v, u, w = map(int, input().split())
    if v in G:
        G[v].append((u, w))
    else:
        G[v] = [(u, w)]
        
    if u in G:
        G[u].append((v, w))
    else:
        G[u] = [(v, w)]
        
components = get_connected_components(G)

min_max_edge = float('inf')
for component in components:
    edges = []
    for v in component:
        for edge in G[v]:
            edges.append((v,) + edge)
    edges.sort(key=lambda x: x[-1], reverse=True)
    
    marked = set()
    
    max_edge = -1
    
    for edge in edges:
        if edge[0] in marked and edge[1] in marked:
            continue
        
        marked.update(edge[:-1])
        max_edge = edge[-1]
        
        if len(marked) == len(component):
            if max_edge < min_max_edge:
                min_max_edge = max_edge
            
            break
        
print(min_max_edge - 1)