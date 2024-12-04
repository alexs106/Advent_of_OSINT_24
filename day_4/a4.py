with open("input_4.txt") as data:
    data = data.read()

def count(word,data):
    return data.count(word)

print(count("XMAS",data))
print(count("SAMX",data))