def ascending(row): 
    return all(row[i] < row[i+1] for i in range(len(row)-1))

def descending(row): 
    return all(row[i] > row[i+1] for i in range(len(row)-1))

def order(row):
    wrong = 0
    for i in range(len(row)-1):
        if row[i] >= row[i+1]:
            wrong += 1
    if wrong <= 1:
        return 'asc_with_exception'
    
    wrong = 0
    for i in range(len(row)-1):
        if row[i] <= row[i+1]:
            wrong += 1
    if wrong <= 1:
        return 'desc_with_exception'
    return False

# Main

with open("input_2.txt", "r") as data:
    rows = []
    a = []
    res = 0

    for line in data:
        row = [int(elem) for elem in line.split()]
        rows.append(row)
    
    for row in rows:
        if order(row) != False:
            a.append(row)

    print("Filtered rows:", a)
    for row in a:
        print("Current row:", row)
        differences = [] 
        valid_row = True 
        for i in range(len(row)-1):
            diff = row[i] - row[i+1]
            if abs(diff) <= 3:
                differences.append(abs(diff))
            else:
                valid_row = False
                break

        if valid_row and all(x <= 3 for x in differences):
            res += 1
            print(row)

    print("Result:", res)
