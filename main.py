import math

"""
normalise distances to positive integers
work out the number of grids needed as a proportion of max lat and long
create dictionary entries starting from 0,0
for any coordinate x, it's square is given by: round( x - minimum / the size of the square)

"""


def main():
    lat_longs = [
        (0, 0),
        (1, 1),
        (0,1),
        (1,0 ),
        (5,5),
        (5,4)
    ]
    distance = 1
    normalised_lat_longs = normalise_lat_longs(lat_longs)

    grid_info = create_grid_info_dict(normalised_lat_longs, distance)

    filled_grid, filled_squares = get_filled_grid_and_filled_squares(create_grid_dict(grid_info), grid_info)

    print(group_by_adjacent_tiles(filled_squares))


def group_lat_long(lat_longs: [(float, float)], distance: float) -> [[(float, float)]]:
    pass


def create_grid_dict(grid_info: dict):
    min_long, max_long = grid_info["min_long"], grid_info["max_long"]
    min_lat, max_lat = grid_info["min_lat"], grid_info["max_lat"]
    distance = grid_info["distance"]
    rows = (math.ceil((max_lat - min_lat) / distance)) + 1
    cols = (math.ceil((max_long - min_long) / distance)) + 1
    d = {}
    for i in range(cols):
        for j in range(rows):
            d[(i, j)] = []
    return d


def normalise_lat_longs(lat_longs: [(float, float)]) -> [(int, int)]:
    return list(map(lambda x: (int((x[0] + 90)), int((x[1] + 180))), lat_longs))


def get_filled_grid_and_filled_squares(grid: dict, grid_info: dict) -> (dict, set):
    min_long, min_lat = grid_info["min_long"], grid_info["min_lat"]
    distance = grid_info["distance"]
    filled_squares = set()
    for lat, long in grid_info["lat_longs"]:
        grid_lat = math.floor((lat - min_lat) / distance)
        grid_long = math.floor((long - min_long) / distance)
        if (grid_lat, grid_long) in grid:
            grid[(grid_lat, grid_long)].append((lat, long))
            filled_squares.add((grid_lat, grid_long))
    return grid, filled_squares


def group_by_adjacent_tiles2(filled_squares: set) -> [set]:
    groups = [set()]
    nesw = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for square in filled_squares:
        for direction in nesw:
            adjacent_square = tuple(map(lambda x: x[0] + x[1], zip(direction, square)))
            for group in groups:
                if adjacent_square in group:  # if this square has a neighbor in the group
                    group.update(square)
                    break
                else:
                    groups.append({square})
                    break
    return groups


def group_by_adjacent_tiles(filled_squares: set) -> [set]:
    visited = set()

    def helper(current_square, group=None):

        if group is None:
            group = set()

        if current_square not in filled_squares or current_square in visited:
            return None
        visited.add(current_square)
        nesw = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for direction in nesw:
            new_coord = tuple(map(lambda x: x[0] + x[1], zip(direction, current_square)))
            group.add(current_square)
            helper(new_coord, group)
        return group
    return [helper(square) for square in filled_squares]


def create_grid_info_dict(lat_longs: [(float, float)], distance: float):
    lat, long = zip(*lat_longs)
    min_long, max_long = min(long), max(long)
    min_lat, max_lat = min(lat), max(lat)
    return {
        "lat_longs": lat_longs,
        "min_long": min_long,
        "max_long": max_long,
        "min_lat": min_lat,
        "max_lat": max_lat,
        "distance": distance
    }


main()