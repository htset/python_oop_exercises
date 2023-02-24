import copy
from pyrsistent import PClass, field
from enum import Enum
import math
import sys
import time
from chart import chart
import numpy as np
import pygame

class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4 

class BlockType(Enum):
    Wall = 1
    Point = 2
    Empty = 3 

class Block:
    type = field()
    entity = field()

class Map(PClass):
    maze = field()
    size_x = field()
    size_y = field()
    points_left = field()

class PacMan(PClass):
    x = field()
    y = field()
    direction = field()
    map = field()

class Ghost(PClass):
    x = field()
    y = field()
    map = field()

def initialize_map(pacman, ghosts, size_x, size_y):
    maze = np.empty((size_x, size_y), Block)
    points_left = 0
    for i in range(0, size_x):
        line = chart[i]
        for j in range(0, size_y):
            maze[i][j] = Block()
            maze[i][j].entity = None

            if line[j] == '.':
                maze[i][j].type = BlockType.Point
                points_left += 1
            elif line[j] == '*':
                maze[i][j].type = BlockType.Wall
            if line[j] == ' ':
                maze[i][j].type = BlockType.Empty

    maze[pacman.x][pacman.y].entity = copy.deepcopy(pacman)
    maze[ghosts[0].x][ghosts[0].y].entity = copy.deepcopy(ghosts[0])
    maze[ghosts[1].x][ghosts[1].y].entity = copy.deepcopy(ghosts[1])
    maze[ghosts[2].x][ghosts[2].y].entity = copy.deepcopy(ghosts[2])

    return Map(maze = maze, \
        size_x = size_x, \
        size_y = size_y, \
        points_left = points_left ) 

def play_pacman(pacman, map):
    candidates = []
    for i in range(pacman.x - 1, pacman.x + 2):
        for j in range(pacman.y - 1, pacman.y + 2):
            if i >= 0 and i < map.size_x \
                and j >= 0 and j < map.size_y \
                and not (i == pacman.x and j == pacman.y) \
                and map.maze[i][j].type != BlockType.Wall:
                    candidates.append((i, j))

    if pacman.direction == Direction.Up \
        and candidates.index((pacman.x - 1, pacman.y)) >= 0 \
            if (pacman.x - 1, pacman.y) in candidates else False:
        return move_entity(pacman, map, pacman.x - 1, pacman.y)
    elif pacman.direction == Direction.Right \
        and candidates.index((pacman.x, pacman.y + 1)) >= 0 \
            if (pacman.x, pacman.y + 1) in candidates else False:
        return move_entity(pacman, map, pacman.x, pacman.y + 1)
    elif pacman.direction == Direction.Down \
        and candidates.index((pacman.x + 1, pacman.y)) >= 0 \
            if (pacman.x + 1, pacman.y) in candidates else False:
        return move_entity(pacman, map, pacman.x + 1, pacman.y)
    elif pacman.direction == Direction.Left \
        and candidates.index((pacman.x, pacman.y - 1)) >= 0 \
            if (pacman.x, pacman.y - 1) in candidates else False: 
        return move_entity(pacman, map, pacman.x, pacman.y - 1)
    else:
        return (pacman, map)

def play_ghost(ghost, map, pacman):
    candidates = []
    distance_to_pacman = []
    for i in range(ghost.x - 1, ghost.x + 2):
        for j in range(ghost.y - 1, ghost.y + 2):
            if i >= 0 and i < map.size_x \
                and j >= 0 and j < map.size_y \
                and not (i == ghost.x and j == ghost.y) \
                and map.maze[i][j].type != BlockType.Wall:
                    candidates.append((i, j))
                    distance_to_pacman.append( \
                        math.sqrt(math.pow(i - pacman.x, 2) \
                            + math.pow(j - pacman.y, 2)))

    min_distance = min(distance_to_pacman)
    min_dist_index = distance_to_pacman.index(min_distance)

    if map.maze[candidates[min_dist_index][0]][candidates[min_dist_index][1]].entity != None:
        #move only if pacman is there
        if isinstance(map.maze[candidates[min_dist_index][0]][candidates[min_dist_index][1]].entity, PacMan):
            #move to pacman's place
            return move_entity(ghost, map, candidates[min_dist_index][0], candidates[min_dist_index][1])
        else:
            #do not move
            return (ghost, map)    
    else:
        return move_entity(ghost, map, candidates[min_dist_index][0], candidates[min_dist_index][1])

def move_entity(entity, map, newX, newY):
    new_entity = entity.set(x = newX, y = newY)
    new_maze = copy.deepcopy(map.maze)
    new_maze[newX][newY].entity = copy.deepcopy(new_maze[entity.x][entity.y].entity)
    new_maze[entity.x][entity.y].entity = None
    new_map = map.set(maze = new_maze)

    return(new_entity, new_map)  

def check_if_pacman_is_eaten(pacman, ghosts):
    for i in range(0, 3):
        if pacman.x == ghosts[i].x \
            and pacman.y == ghosts[i].y:
            return True
    return False

def check_if_game_over(map):
    if map.points_left == 0:
        return True
    else:
        return False

def set_direction(pacman, direct):
    return pacman.set(direction = direct)

def draw(map, screen):
    width = 10
    for i in range(0, map.size_x):
        for j in range(0, map.size_y):
            if map.maze[i][j].entity != None:
                if isinstance(map.maze[i][j].entity ,PacMan):
                    pygame.draw.rect(screen, (150, 150, 150), \
                        (j * width, i * width, (j+1)*width, (i+1)*width))
                elif isinstance(map.maze[i][j].entity, Ghost):
                    pygame.draw.rect(screen, (255, 255, 255), \
                        (j * width, i * width, (j+1)*width, (i+1)*width))
            else:
                if map.maze[i][j].type == BlockType.Wall:
                    pygame.draw.rect(screen, (0, 255, 0), \
                        (j* width, i* width, (j+1)*width, (i+1)*width))
                elif map.maze[i][j].type == BlockType.Point:
                    pygame.draw.rect(screen, (255, 0, 0), \
                        (j* width, i* width, (j+1)*width, (i+1)*width))
                elif map.maze[i][j].type == BlockType.Empty:
                    pygame.draw.rect(screen, (0, 0, 0), \
                        (j* width, i* width, (j+1)*width, (i+1)*width))

    pygame.display.update()

def remove_point_if_needed(map, pacman):
    if map.maze[pacman.x][pacman.y].type == BlockType.Point:
        map.maze[pacman.x][pacman.y].type = BlockType.Empty
        return map.set(points_left = map.points_left - 1)
    else:
        return map

def main():
    pygame.init()
    screen = pygame.display.set_mode([500, 500])

    pacman = PacMan(x=23, y=13, direction=Direction.Left)
    ghosts = []
    ghosts.append(Ghost(x=5, y=5))
    ghosts.append(Ghost(x=5, y=20))
    ghosts.append(Ghost(x=8, y=5))

    map = initialize_map(pacman, ghosts, 32, 28)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman = set_direction(pacman, Direction.Up)
                if event.key == pygame.K_DOWN:
                    pacman = set_direction(pacman, Direction.Down)
                if event.key == pygame.K_LEFT:
                    pacman = set_direction(pacman, Direction.Left)
                if event.key == pygame.K_RIGHT:
                    pacman = set_direction(pacman, Direction.Right)

        pacman, map = play_pacman(pacman, map)
        map = remove_point_if_needed(map, pacman)

        for i in range(0, 3):
            ghosts[i], map = play_ghost(ghosts[i], map, pacman)

        draw(map, screen)
        
        if check_if_game_over(map) or check_if_pacman_is_eaten(pacman, ghosts):
            sys.exit()

        time.sleep(0.5)


if __name__ == "__main__":
    main()        