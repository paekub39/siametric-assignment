LAND_VALUE = "1"
NOTED_LAND_VALUE = "-1"


class Land:
    Row = None
    Column = None

    def __init__(self, row, column):
        self.Row = row
        self.Column = column


class Island:
    Lands = []

    def __init__(self, lands):
        self.Lands = lands

    def expand_island(self, land):
        self.Lands.append(land)

    def is_already_found_the_land(self, land):
        for l in self.Lands:
            if l.Row == land.Row and l.Column == land.Column:
                return True
        return False

    def expand_if_not_already_found(self, land):
        if not self.is_already_found_the_land(land):
            self.expand_island(land)

    def explore_and_expand_island(self, land, grid):
        if grid[land.Row][land.Column] == LAND_VALUE:
            self.expand_if_not_already_found(land)
            self.explore_island(land, grid)

    def explore_island(self, current_land, grid):
        r = current_land.Row
        c = current_land.Column
        grid[r][c] = NOTED_LAND_VALUE
        # Explore North
        if 0 < r < len(grid):
            new_land = Land(r-1, c)
            self.explore_and_expand_island(new_land, grid)
        # Explore South
        if 0 <= r < len(grid) - 1:
            new_land = Land(r + 1, c)
            self.explore_and_expand_island(new_land, grid)
        # Explore West
        if 0 < c < len(grid[r]):
            new_land = Land(r, c - 1)
            self.explore_and_expand_island(new_land, grid)
        # Explore East
        if 0 <= c < len(grid[r]) - 1:
            new_land = Land(r, c + 1)
            self.explore_and_expand_island(new_land, grid)


class World:
    def __init__(self, grid):
        self.Island = None
        self.Grid = grid
        self.explore_map()

    def get_grid_temp(self):
        grid = self.Grid
        new_grid = []
        for i in range(len(grid)):
            new_grid.append(grid[i].copy())
        return new_grid

    def explore_map(self):
        grid = self.get_grid_temp()
        islands = []
        for r in range(0, len(grid), 1):
            for c in range(0, len(grid[r]), 1):
                if grid[r][c] == LAND_VALUE:
                    land = Land(r, c)
                    island = Island([land])
                    island.explore_island(land, grid)
                    islands.append(island)

        self.Island = islands

    def count_island(self):
        return len(self.Island)


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    w = World(grid)
    print(w.count_island())
