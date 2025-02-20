grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

def numberOfIslands():
    rows, cols = len(grid), len(grid[0])
    offsets = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = set()
    count = 0

    def withinBounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def markVisited(ri,ci):
        if grid[ri][ci] == '0' or (ri,ci) in visited:
            return 0

        visited.add((ri,ci))
        for dx,dy in offsets:
            if withinBounds(ri+dx,ci+dy):
                markVisited(ri+dx,ci+dy)

        return 1

    for ri,rv in enumerate(grid):
        for ci,cv in enumerate(rv):
            if (ri,ci) not in visited and cv == '1':
                count += 1
                markVisited(ri,ci)
    
    return count

numberOfIslands()
