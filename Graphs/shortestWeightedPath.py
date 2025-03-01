# follow-up for findShortestPath but now with weights between the cells in the graph

import heapq

def findShortstWeightedPath(grid):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (grid[0][0], 0, 0))

    shortest_paths = {(0,0): grid[0][0]}
    row_x = -1
    col_x = -1

    while heap:
        min_weight, cur_r, cur_c = heapq.heappop(heap)

        for dir in directions:
            new_r, new_c = cur_r + dir[0], cur_c + dir[1]

            if 0 <= new_r <= len(grid)-1 and 0 <= new_c <= len(grid[0])-1:
                # explore routes
                if grid[new_r][new_c] == 'X':
                    return min_weight
                    # this part is redundant since if we reach the treasure we reach it from the shortest path in heap, no shorter than this
                    # row_x, col_x = new_r, new_c
                    # if (new_r, new_c) in shortest_paths:
                    #     if min_weight < shortest_paths[(new_r, new_c)]:
                    #         shortest_paths[(new_r, new_c)] = min_weight
                    # else:
                    #     shortest_paths[(new_r, new_c)] = min_weight
                elif grid[new_r][new_c] != 'd':
                    if (new_r, new_c) in shortest_paths:
                        if min_weight+grid[new_r][new_c] < shortest_paths[(new_r, new_c)]:
                            shortest_paths[(new_r, new_c)] = min_weight+grid[new_r][new_c]
                            heapq.heappush(heap, (grid[new_r][new_c]+min_weight, new_r, new_c))
                    else:
                        shortest_paths[(new_r, new_c)] = min_weight+grid[new_r][new_c]
                        heapq.heappush(heap, (grid[new_r][new_c]+min_weight, new_r, new_c))
    
    return shortest_paths[(row_x, col_x)]


if __name__ == "__main__":
    matrix = [
    [ 1,  1,  2,  1],
    [ 4, 1, 'd', 1],
    [ 1,  12, 4,  1],
    ['d', 'X',1,  3],
    ]
    # shortest - 10 total

    print(findShortstWeightedPath(matrix))