# read test.txt
file1 = open('test.txt', mode='rt')
lines = file1.readlines()

for line in lines:
    print(line[0])

file1.close()
