# write your code here
for number in range(1, 11):
    file_name = f"file{number}.txt"
    with open(file_name, 'a') as file:
        file.write(str(number))
