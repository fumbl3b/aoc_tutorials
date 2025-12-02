from input_data import input
# from utils import read_grid, find_in_grid, get_neighbors, manhattan_distance, extract_numbers, parse_ranges

def parse_input():
    """Parse the input data into a useful format."""
    lines = input.strip().splitlines()
    return lines

def part1(data):
    """Solve part 1 of the problem."""
    # TODO: Implement part 1 solution here
    return None

def part2(data):
    """Solve part 2 of the problem.""" 
    # TODO: Implement part 2 solution here
    return None

def main():
    """Main function to run both parts."""
    data = parse_input()
    
    print("=== Advent of Code Solution ===")
    print(f"Input has {len(data)} lines")
    print()
    
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
