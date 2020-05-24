# read sums.txt
def sum_line(line: str):
    number1: int = int(line.split()[0])
    number2: int = int(line.split()[1])
    return number1 + number2


file = open('sums.txt')
for line in file:
    print(sum_line(line))
file.close()
