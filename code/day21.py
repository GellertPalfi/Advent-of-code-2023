from collections import deque

from common import read_input


def get_start(grid):
    for i, string in enumerate(grid):
        if 'S' in string:
            return i, string.index('S')

def solution_1(grid, sr, sc, steps):   
    seen = {(sr, sc)}
    ans = set()
    q = deque([(sr, sc,steps)])
    while  q:
        r, c, s = q.popleft()
        
        if s % 2 == 0:
            ans.add((r,c))
        if s == 0:
            continue
        
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in seen:
                continue
            seen.add((nr,nc))
            q.append((nr,nc,s-1))
    
    return len(ans)
            
def solution_2(size, steps, grid):
    sr, sc = get_start(grid)
    grid_width = steps // size -1 
    odd = (grid_width // 2 * 2 + 1) ** 2
    even = ((grid_width + 1) // 2 * 2) ** 2

    odd_points = solution_1(grid,sr, sc, size * 2 + 1)
    even_points = solution_1(grid,sr, sc, size * 2)
    
    corner_t = solution_1(grid,size - 1, sc, size - 1)
    corner_r = solution_1(grid,sr, 0, size - 1)
    corner_b = solution_1(grid,0, sc, size - 1)
    corner_l = solution_1(grid,sr, size - 1, size - 1)

    small_tr = solution_1(grid,size - 1, 0, size // 2 - 1)
    small_tl = solution_1(grid,size - 1, size - 1, size // 2 - 1)
    small_br = solution_1(grid,0, 0, size // 2 - 1)
    small_bl = solution_1(grid,0, size - 1, size // 2 - 1)

    large_tr = solution_1(grid,size - 1, 0, size * 3 // 2 - 1)
    large_tl = solution_1(grid,size - 1, size - 1, size * 3 // 2 - 1)
    large_br = solution_1(grid,0, 0, size * 3 // 2 - 1)
    large_bl = solution_1(grid,0, size - 1, size * 3 // 2 - 1)
    
    print(
    odd * odd_points +
    even * even_points +
    corner_t + corner_r + corner_b + corner_l +
    (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) +
    grid_width * (large_tr + large_tl + large_br + large_bl)
    )
    
if __name__ == "__main__":
    grid = read_input("inputs/day21.txt")
    sr, sc = get_start(grid)
    print(solution_1(grid, sr, sc, 64))
    size = len(grid)
    steps = 26501365
    solution_2(size, steps, grid)
    