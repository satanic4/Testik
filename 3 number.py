class Studentiki:
    pass

f = open('students.csv', encoding='utf-8')
students = []

for i in range(501):
    students.append(Studentiki)
    s = f.readline().split(',')
    if s[4] == None:
        s[4] = '0'
    students[i].id = s[0]
    students[i].fio = s[1]
    students[i].classs = s[2]
    students[i].score = s[3]

idd = input()

for i in range(1, len(students)):
    if students[i].id == str(idd):
        print('Проект № ', students[i].id, 'делал ', students[i].fio, 'он получил оценку - ', students[i].score)
        exit()