numbers = [1234, 5678, 90]
numbers = [str(number) for number in numbers]
numbers = '\n'.join(numbers)
# save this list in `file_with_list.txt`
file = open('file_with_list.txt', 'wt')
# file.writelines(numbers)
file.write(numbers)
# print(*numbers, file=file, sep='\n', end='', flush=True)
file.close()
