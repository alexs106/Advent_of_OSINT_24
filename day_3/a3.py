import re

with open("input_3.txt") as data:
    data = data.read(); 

def part_1(data):
    return sum(int(a) * int(b) for a, b in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', data))

def part_2(data):
    mults = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', data)
    do = True
    res = 0
    for m in mults:
        if m == "do()":
            do = True
        elif m == "don't()":
            do = False
        elif do:
            a, b = re.search(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', m).groups()
            res += int(a) * int(b)
    return res

print(part_1(data))
print(part_2(data))