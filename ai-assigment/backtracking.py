from __future__ import annotations
from dataclasses import dataclass
from enum import Flag, auto
from functools import wraps
from typing import TypeVar
N = 9

def singleton(cls):
    """Singleton decorator
    
    cls(x, y) is cls(x, y)
    """
    instances = {}
    def get_instance(*args, **kwargs):
        # Here args[0], args[1] are considered as x and y, the unique pair for instantiation.
        key = (args[0], args[1])
        if key not in instances:
            # Only x, y are passed for the creation of a new instance
            instances[key] = cls(*args, **kwargs)
        return instances[key]
    return get_instance


class NodeType(Flag):
    E = auto()
    """Empty"""
    S = auto()
    """Captain America's shield"""
    I = auto()
    """The Infinity stone"""
    
    
    P = auto()
    """Perception zone of an enemy"""
    H = auto()
    """Hulk"""
    T = auto()
    """Thor"""
    M = auto()
    """Captain Marvel"""
    

    DangerZone = P | H | T | M
    

@singleton
@dataclass
class Node:
    x: int
    y: int
    node_type: NodeType | None = None
    cost: float = float('inf')
    
    visited: bool = False

    @property
    def heuristic(self) -> float:
        """distance to goal. only defined for nodes with type, in other case -1
        
        return float('inf'), if DangerZone  
        """
        if self.node_type is None:
            return -1
        if self.node_type not in NodeType.DangerZone:
            return self.distance(goal)
        else:
            return float('inf')
        
    def distance(self, destination: Node) -> int:
        return abs(self.x - destination.x) + abs(self.y - destination.y)


perception_variant = int(input())

goal = Node(*map(int, input().split()), node_type=NodeType.I)

def filter_field(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return filter(lambda p: N > p[0] >= 0 and N > p[1] >= 0, func(*args, **kwargs))
    return wrapper


@filter_field
def moore_neighborhood(x: int, y: int):
    result = [(x+dx, y+dy) for dy in (-1,0, 1) for dx in (-1,0,1) if (x+dx, y+dy) != (x,y)]
    if perception_variant == 2:
        result.extend([(x+dx,y+dy) for dx in (-2,2) for dy in (-2,2)])    
    return result

@filter_field
def von_neumann_neighborhood(x: int, y: int, *, rangee=1):
    return [(x+dx, y+dy) for dy in range(-rangee,rangee+1) for dx in range(-rangee,rangee+1) if 0 < abs(dx)+abs(dy) <= rangee]
    
    
    
T = TypeVar('T')
def create_path(current_path: list[T], target_path: list[T]) -> list[T]:
    min_length = min(len(current_path), len(target_path))
    for i in range(min_length):
        if current_path[i] != target_path[i]:
            diverging_index = i
            break
    else:
        diverging_index = min_length
        
    path = current_path[-2:diverging_index-1:-1]
    path += target_path[diverging_index-1:-1]
    return path

def move(x, y):
    """prosedure of movement. discard information from iterator"""
    print(f'm {x} {y}')
    n = int(input())
    for _ in range(n):
        input()


field = [[Node(x, y) for x in range(N)] for y in range(N)]


# first pseudo-move, preparation for zero step in A-star 
field[0][0].node_type = NodeType.E
field[0][0].cost = 0
field[0][0].visited = True
x, y = 0, 0


min_result = float('inf')

def backtraking(x, y, cost = 0):
    """find minimal path from x, y to a goal.
    
    update global variable 'min_result'"""
    
    global min_result
    
    print(f'm {x} {y}')

    n = int(input())
    for _ in range(n):
        x0, y0, node_type = input().split()
        x0, y0 = int(x0), int(y0)
        
        field[y0][x0].node_type = NodeType[node_type]
    
    
    # vision
    for x0, y0 in moore_neighborhood(x, y):
        if field[y0][x0].node_type is None:
            field[y0][x0].node_type = NodeType.E

    
    if field[y][x] == goal:
        if cost < min_result:
            min_result = cost
            #print(f'{min_result=}')
        return
    
    for x0, y0 in sorted(von_neumann_neighborhood(x,y), key=lambda p: field[p[1]][p[0]].heuristic):
        if not field[y0][x0].visited and field[y0][x0].node_type not in NodeType.DangerZone: # type: ignore
            if cost+1 < field[y0][x0].cost:
                field[y0][x0].cost = cost+1
            
                field[y0][x0].visited = True
                backtraking(x0, y0, cost+1)
                field[y0][x0].visited = False
                move(x,y)
    
    
backtraking(0, 0)
print(f'e {min_result if min_result != float("inf") else -1}')