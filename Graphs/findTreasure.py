# You have a map that marks the location of a treasure island. Some of the map areas have jagged rocks and dangerous reefs. Other areas are safe to sail in.
# There are other explorers trying to find the treasure, so you must figure out the shortest route to the treasure island.
# Assume the map area is a two-dimensional grid, represented by a matrix of characters.
# You must start from the top-left corner of the map and can move one block up, down, left, or right at a time. # type: ignore
# The treasure island is marked as 'X' in a block of the matrix. 'X' will not be at the top-left corner.
# Any block with dangerous rocks or reefs will be marked as 'D'. You must not enter dangerous blocks. You cannot leave the map area.
# Other areas 'O' are safe to sail in. The top-left corner is always safe.
# Output the minimum number of steps to get to the treasure.

from collections import deque

# allowing changing the grid
def findShortestPath(grid):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    #start BFS from top left corner
    if grid[0][0] == 'D':
        return -1
    
    queue = deque()
    queue.append((0,0,0)) # row, col, curr_distance passed
    grid[0][0] = 1 #visited-mark

    while queue:
        cur_r, cur_c, cur_distance = queue.popleft()

        for dir in directions:
            new_r, new_c = cur_r + dir[0], cur_c + dir[1]

            if 0 <= new_r <= len(grid)-1 and 0 <= new_c <= len(grid[0])-1:
                # explore routes
                if grid[new_r][new_c] == 'O':
                    queue.append((new_r, new_c, cur_distance+1))
                    grid[new_r][new_c] = 1 #visited-mark

                # we found the treasure    
                if grid[new_r][new_c] == 'X':
                    return cur_distance+1
                
    # otherwise, no route found to treasure, treasure is blocked
    return -1

if __name__ == "__main__":
    matrix = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O'],
    ]

    print(findShortestPath(matrix))