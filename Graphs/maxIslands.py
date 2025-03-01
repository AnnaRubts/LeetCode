# #695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

from collections import deque

# allowing changing the grid
def maxAreaOfIsland(grid):
    max_area = 0
    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                #start local BFS
                island_size = 1
                queue = deque()
                queue.append((r,c))
                grid[r][c] = 0 #visited-mark
                while queue:
                    cur_r, cur_c = queue.popleft()
                    for dir in directions:
                        new_r, new_c = cur_r + dir[0], cur_c + dir[1]
                        if 0 <= new_r <= len(grid)-1 and 0 <= new_c <= len(grid[0])-1 and grid[new_r][new_c] == 1:
                            island_size+=1
                            queue.append((new_r,new_c))
                            grid[new_r][new_c] = 0 #visited-mark
                if island_size > max_area:
                    max_area = island_size
    
    return max_area

if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print(maxAreaOfIsland(grid))

    grid0 = [[0,0,0,0,0,0,0,0]]
    print(maxAreaOfIsland(grid0))



