import re2

with open("input_4.txt") as data:
    data = data.read()

def part1(data):
    regex = ["XMAS", "X...\n.M..\n..A.\n...S"]
    return sum(len(re2.findall(regex, data, rotate=True))for pattern in regex)

def part2(data):
    return len(re2.findall("M.M\n.A.\nS.S", data, rotate=True))

