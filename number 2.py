class Studentiki:
    pass

f = open("students (1).csv", encoding='utf-8')
students = []
f.readline()

for i in f:
    students.append(i[:-1])
studentik1 = []
A = int(input())

for i in range(len(students)):
    studentik1.append(Studentiki())
for i in range(len(students)):
    s = students[i].split(",")
    studentik1[i].idd = s[0]
    studentik1[i].name = s[1]
    studentik1[i].tidd = s[2]
    studentik1[i].clas = s[3]
    if s[4] == "None":
        s[4] = '0'
    studentik1[i].score = s[4]
print(A, "класс:")
k=0
for i in range(len(studentik1)):
    t = studentik1[i]
    j = i - 1
    while j >= 0 and t.score > studentik1[j].score:
        studentik1[j+1] = studentik1[j]
        j -= 1
    studentik1[j+1] = t
for i in range(1,len(students)):
    if studentik1[i].clas[:-1] == str(A):
        k += 1
        print(k, "место", studentik1[i].name)
    if k == 3:
        break