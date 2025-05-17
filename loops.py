students = ['anand','sachin','naveen','raj','abhi']
failedStudents=['anand','sachin']

print('Printing all Students :',students)
for student in students:
    if student in failedStudents:
        print('Student failed',student)
        students.remove(student)

print(students)
## Out is coming as wrong as the existing array got modified and hence gave stale data
print('Fixing the loop issue############################# :')
students1 = ['anand','sachin','naveen','raj','abhi']
print('Printing all Students1 :',students1)
failedStudents1=['anand','sachin']
############################################

for student1 in students1[:]:
    if student1 in failedStudents1:
        print('Student failed',student1)
        students1.remove(student1)

print(students1)
#########################################