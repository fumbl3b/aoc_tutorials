"""Utility functions for Advent of Code solutions."""

def read_grid(lines):
    """Convert lines into a 2D grid."""
    return [list(line) for line in lines]

def find_in_grid(grid, target):
    """Find all positions of target character in grid."""
    positions = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == target:
                positions.append((x, y))
    return positions

def get_neighbors(x, y, grid, diagonal=False):
    """Get valid neighboring coordinates."""
    height, width = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if diagonal:
        directions.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
    
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            neighbors.append((nx, ny))
    return neighbors

def manhattan_distance(pos1, pos2):
    """Calculate Manhattan distance between two points."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def extract_numbers(text):
    """Extract all numbers from a string."""
    import re
    return [int(x) for x in re.findall(r'-?\d+', text)]

def parse_ranges(line, separator='-'):
    """Parse ranges like '1-3,5-7' into list of tuples."""
    ranges = []
    for part in line.split(','):
        start, end = map(int, part.split(separator))
        ranges.append((start, end))
    return ranges