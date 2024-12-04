#Part 1
res1 = []
res2 = []

with open("input.txt") as input:
    col1 = []
    col2 = []

    for line in input:
        val = line.split()

        col1.append(int(val[0]))
        col2.append(int(val[1]))

col1.sort()
col2.sort()

while col1 and col2:
    one = col1[0]
    two = col2[0]

    left1 = abs(one-two)
    res1.append(left1)

    del col1[0]
    del col2[0]

print(sum(res1))

#Part 2        
while col1:
    val1 = col2.count(col1[0])
    left2 = val1 * col1[0]
    res2.append(left2)

print(sum(res2))