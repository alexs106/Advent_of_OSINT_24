from pathlib import Path
 
 
def get_data(filepath: Path) -> str:
    with open(filepath, "r") as f:
        data = f.read()
    return data
 
 
def parse_data(data: str) -> list[list[int]]:
    output = []
    for row in data.strip().split("\n"):
        output.append(list(map(int, row.split())))
    return output
 
 
def is_part_a_safe(row) -> bool:
    asc = row[0] < row[1]
    for i, n in enumerate(row[1:], start=1):
        diff = abs(n - row[i - 1])
        if (diff >= 4) or (diff == 0):
            return False
        if asc:
            if row[i - 1] > n:
                return False
        else:
            if row[i - 1] < n:
                return False
    return True
 
 
def is_safe_removing_one_level(row) -> bool:
    for i in range(len(row)):
        new_row = row[:i] + row[i + 1:]
        if is_part_a_safe(new_row):
            return True
    return False
 
 
def part_a_example_1():
    ex1 = Path(r"input_2.txt")
    data_str = get_data(ex1)
    data = parse_data(data_str)
    safe = 0
    for r in data:
        if is_part_a_safe(r):
            safe += 1
    print(safe)
 
 
def part_b_example_1():
    ex1 = Path(r"input_2.txt")
    data_str = get_data(ex1)
    data = parse_data(data_str)
    safe = 0
    for r in data:
        if is_part_a_safe(r):
            safe += 1
        else:
            if is_safe_removing_one_level(r):
                safe += 1
    print(safe)
 
 
def part_a():
    fp = Path(r"input_2.txt")
    data_str = get_data(fp)
    data = parse_data(data_str)
    safe = 0
    for r in data:
        if is_part_a_safe(r):
            safe += 1
    print(safe)
 
 
def part_b():
    fp = Path(r"input_2.txt")
    data_str = get_data(fp)
    data = parse_data(data_str)
    safe = 0
    for r in data:
        if is_part_a_safe(r):
            safe += 1
        else:
            if is_safe_removing_one_level(r):
                safe += 1
    print(safe)
 
 
if __name__ == '__main__':
    part_a()
    part_b()
 