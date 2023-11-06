from __future__ import annotations
from typing import TypeVar

from dataclasses import dataclass
from enum import Flag, auto

from functools import wraps

N = 9
def singleton(cls):
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
    
    
    parent: Node | None = None

    is_in_closed_set: bool = False
    
    @property
    def minimal_path(self) -> list[tuple[int,int]]:
        if (self.x, self.y) == (0, 0):
            return [(0, 0)]
        if self.parent is None:
            raise ValueError()
        return self.parent.minimal_path + [(self.x, self.y)]
    
    @property
    def heuristic(self) -> float:
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

def predefined_move(path: list[tuple[int, int]]):
    #print(*path)
    for x, y in path:
        print(f'm {x} {y}')
        n = int(input())
        for _ in range(n):
            input()
    return path[-1]

field = [[Node(x, y) for x in range(N)] for y in range(N)]


# first pseudo-move, preparation for zero step in A-star 
field[0][0].node_type = NodeType.E
field[0][0].cost = 0
field[0][0].is_in_closed_set = True
x, y = 0, 0


while True:
    if field[y][x].node_type is not None and field[y][x].node_type in NodeType.DangerZone: # type: ignore
        print('e -1')
    
    print(f'm {x} {y}')

    field[y][x].is_in_closed_set = True
    
    n = int(input())
    for _ in range(n):
        x0, y0, node_type = input().split()
        x0, y0 = int(x0), int(y0)
        
        field[y0][x0].node_type = NodeType[node_type]
        
    if field[y][x] == goal:
        print(f'e {goal.cost}')
        break
        
    for x0, y0 in moore_neighborhood(x, y):
        if field[y0][x0].node_type is None:
            field[y0][x0].node_type = NodeType.E
    
    for x0, y0 in von_neumann_neighborhood(x,y):
        if not field[y0][x0].is_in_closed_set:
            if field[y][x].cost + field[y0][x0].distance(field[y][x]) < field[y0][x0].cost:
                field[y0][x0].cost = field[y][x].cost + field[y0][x0].distance(field[y][x])
                field[y0][x0].parent = field[y][x]
                # print(f'cost of {x0} {y0} is {field[y0][x0].cost} + {field[y0][x0].heuristic}')
                # print(f'parent of {x0} {y0} is {x} {y}')
        
    
    min_f = float('inf')
    
    
    x_n, y_n = x, y
    for x0 in range(N):
        for y0 in range(N):
            if field[y0][x0].is_in_closed_set:
                continue
            
            f = field[y0][x0].cost + field[y0][x0].heuristic
            if f < min_f:
                min_f = f
                x_n, y_n = x0, y0
            elif f == min_f:
                if field[y0][x0].heuristic < field[y_n][x_n].heuristic:
                    x_n, y_n = x0, y0
                    
    if min_f == float('inf'):
        print('e -1')
        break
    elif field[y_n][x_n].parent != field[y][x]:
        target = field[y_n][x_n].minimal_path
        current = field[y][x].minimal_path
        
        # print("FROM", current)
        # print("TO", target)
        
        path = create_path(current, target)
        predefined_move(path)
    x, y = x_n, y_n
                    
    # for line in field:
    #     for node in line:
    #         print(f'{node.cost} {node.heuristic}', end='\t')
    #     print()