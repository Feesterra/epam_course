# amount of students and tasks
students_count = None
tasks_count = None
while (type(students_count) != int) | (type(tasks_count) != int):
    try:
        print("Input number of students and number of tasks:")
        students_count = int(input())
        tasks_count = int(input())
    except ValueError as e:
        print("Please try again. Use integers.")

# table filling
table = [[None] * (tasks_count + 1) for i in range(students_count + 1)]
table[0][0] = 'Names\\Tasks'

# tasks' headings
for j in range(1, tasks_count + 1):
    table[0][j] = "T" + str(j)

# students' names input (only letters are correct)
print("Students' names are:")
for i in range(1, students_count+1):
    while not (str(table[i][0]).isalpha()) & (table[i][0] is not None):
        print('Type name of student {}'.format(i))
        table[i][0] = input().title()


# marks input (integers between 1 and 10)
for i in range(1, students_count+1):
    print("Marks of student " + str(table[i][0]))
    for j in range(1, tasks_count+1):
            while type(table[i][j]) != int:
                try:
                    table[i][j] = int(input())
                    if (table[i][j] < 1) | (table[i][j] > 10):
                        table[i][j] = None
                        print("Use integers between 1 and 10")
                except ValueError as e:
                    print("Use integers between 1 and 10")

# printing table of marks
for row in table:
    print(row)
rate_tasks = []

# counting tasks' rating
for j in range(1, tasks_count + 1):
    sum = 0
    for i in range(1, students_count+1):
        sum += table[i][j]
    rate_tasks.append(sum)

# checking tasks' rating
# print(rate_tasks)

# TOP-3 difficult tasks counting
print("TOP-3 tasks: ")
ind = 0
k = 0
while k < 3:
    if rate_tasks[ind] == min(rate_tasks):
        print(table[0][ind + 1])
        rate_tasks[ind] = 999
        k += 1
    if ind < len(rate_tasks)-1:
        ind += 1
    else:
        ind = 0

# students' rating counting
rate_students = []
for i in range(1, students_count + 1):
    summ = 0
    for j in range(1, tasks_count+1):
        summ += table[i][j]
    rate_students.append(summ)

# checking students' rating
# print(rate_students)

# TOP-3 students counting (maximal score)
print("TOP-3 students: ")
ind = 0
count = 0
while count < 3:
    if rate_students[ind] == max(rate_students):
        print(table[ind + 1][0])
        rate_students[ind] = -999
        count += 1
    if ind < len(rate_students)-1:
        ind += 1
    else:
        ind = 0
