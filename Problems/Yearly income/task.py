# write your code here
with open('salary.txt', 'rt') as in_file:
    for monthly_line in in_file.readlines():
        with open('salary_year.txt', 'a') as out_file:
            year_salary = int(monthly_line.strip()) * 12
            out_file.write(str(year_salary) + '\n')
