# read test_file.txt
file = open('test_file.txt', encoding='utf-16', mode='rt')
print(file.readline())
file.close()
