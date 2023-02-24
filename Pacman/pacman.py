from abc import ABC, abstractmethod
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
    def __init__(self) -> None:
        self.type = BlockType.Empty
        self.entity = None

class Map:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([500, 500])

        self.map = np.empty((32, 28), Block)
        self.size_x = 32
        self.size_y = 28 
        self.game_active = True
        self.pacman_location = None
        self.points_left = 0
        self.exit = False

        for i in range(0, 32):
            line = chart[i]
            for j in range(0, 28):
                self.map[i][j] = Block()
                self.map[i][j].entity = None

                if line[j] == '.':
                    self.map[i][j].type = BlockType.Point
                    self.points_left += 1
                elif line[j] == '*':
                    self.map[i][j].type = BlockType.Wall
                if line[j] == ' ':
                    self.map[i][j].type = BlockType.Empty

        self.player = []
        self.player.append(PacMan(self, 23, 13))
        self.map[23][13].entity = self.player[0]
        self.pacman_location = (23, 13)

        self.player.append(Ghost(self, 5, 5))
        self.map[5][5].entity = self.player[1]

        self.player.append(Ghost(self, 5, 20))
        self.map[5][20].entity = self.player[2]

        self.player.append(Ghost(self, 8, 5))
        self.map[8][5].entity = self.player[3]

    def run(self):
        while self.game_active == True and self.exit != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player[0].direction = Direction.Up
                    if event.key == pygame.K_DOWN:
                        self.player[0].direction = Direction.Down
                    if event.key == pygame.K_LEFT:
                        self.player[0].direction = Direction.Left
                    if event.key == pygame.K_RIGHT:
                        self.player[0].direction = Direction.Right

            for i in range(0, 3):
                self.player[i].play()

            self.draw()
            time.sleep(0.5)

    def draw(self):
        width = 10
        for i in range(0, 32):
            for j in range(0, 28):
                if self.map[i][j].entity != None:
                    if self.map[i][j].entity.type == "pacman":
                        pygame.draw.rect(self.screen, (150, 150, 150), \
                            (j * width, i * width, (j+1)*width, (i+1)*width))
                    elif self.map[i][j].entity.type == "ghost":
                        pygame.draw.rect(self.screen, (255, 255, 255), \
                            (j * width, i * width, (j+1)*width, (i+1)*width))
                else:
                    if self.map[i][j].type == BlockType.Wall:
                        pygame.draw.rect(self.screen, (0, 255, 0), \
                            (j* width, i* width, (j+1)*width, (i+1)*width))
                    elif self.map[i][j].type == BlockType.Point:
                        pygame.draw.rect(self.screen, (255, 0, 0), \
                            (j* width, i* width, (j+1)*width, (i+1)*width))
                    elif self.map[i][j].type == BlockType.Empty:
                        pygame.draw.rect(self.screen, (0, 0, 0), \
                            (j* width, i* width, (j+1)*width, (i+1)*width))

        pygame.display.update()

class Entity(ABC):
    def __init__(self, map, x = 0, y = 0, type = "") -> None:
        self.map = map
        self.x = x
        self.y = y
        self.direction = Direction.Left
        self.type = type

    def move(self, newX, newY):
        if newX == self.x and newY == self.y:
            print("error")
        self.map.map[newX][newY].entity = self.map.map[self.x][self.y].entity
        self.map.map[self.x][self.y].entity = None
        self.x = newX
        self.y = newY

    @abstractmethod
    def play():
        pass   
 
class PacMan(Entity):
    def __init__(self, map, x=0, y=0, type="pacman") -> None:
        super().__init__(map, x, y, type)

    def play(self):
        candidates = []
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if i >= 0 and i < self.map.size_x \
                    and j >= 0 and j < self.map.size_y \
                    and not (i == self.x and j == self.y) \
                    and self.map.map[i][j].type != BlockType.Wall:
                        candidates.append((i, j))
    
        if self.direction == Direction.Up \
            and candidates.index((self.x - 1, self.y)) >= 0 \
                if (self.x - 1, self.y) in candidates else False:
            self.move(self.x - 1, self.y)
        elif self.direction == Direction.Right \
            and candidates.index((self.x, self.y + 1)) >= 0 \
                if (self.x, self.y + 1) in candidates else False:
            self.move(self.x, self.y + 1)
        elif self.direction == Direction.Down \
            and candidates.index((self.x + 1, self.y)) >= 0 \
                if (self.x + 1, self.y) in candidates else False:
            self.move(self.x + 1, self.y)
        elif self.direction == Direction.Left \
            and candidates.index((self.x, self.y - 1)) >= 0 \
                if (self.x, self.y - 1) in candidates else False: 
            self.move(self.x, self.y - 1)

        self.map.pacman_location = (self.x, self.y)
        if self.map.map[self.x][self.y].type == BlockType.Point:
            self.map.map[self.x][self.y].type = BlockType.Empty
            self.map.points_left -= 1
            if self.map.points_left == 0:
                self.map.game_active = False

class Ghost(Entity):
    def __init__(self, map, x=0, y=0, type="ghost") -> None:
        super().__init__(map, x, y, type)

    def play(self):
        candidates = []
        distance_to_pacman = []
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if i >= 0 and i < self.map.size_x \
                    and j >= 0 and j < self.map.size_y \
                    and not (i == self.x and j == self.y) \
                    and self.map.map[i][j].type != BlockType.Wall:
                        candidates.append((i, j))
                        distance_to_pacman.append( \
                            math.sqrt(math.pow(i - self.map.pacman_location[0], 2) \
                                + math.pow(j - self.map.pacman_location[1], 2)))

        min_distance = min(distance_to_pacman)
        min_dist_index = distance_to_pacman.index(min_distance)

        if self.map.map[candidates[min_dist_index][0]][candidates[min_dist_index][1]].entity != None:
            #move only if pacman is there
            if self.map.map[candidates[min_dist_index][0]][candidates[min_dist_index][1]].entity.type == "pacman":
                #eat pacman
                self.map.map[candidates[min_dist_index][0]][candidates[min_dist_index][1]].entity = None
                self.map.game_active = False
                self.move(candidates[min_dist_index][0], candidates[min_dist_index][1])
        else:
            self.move(candidates[min_dist_index][0], candidates[min_dist_index][1])


def main():
    game = Map()
    game.run()

if __name__ == "__main__":
    main()        