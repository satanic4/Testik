class Studentki:
    pass


f = open('students(2).csv', encoding='utf-8')
a = f.readlines()
students = []
for i in a[1:]:
    inf = Studentki()
    inn = i.split('.')
    inf_id = inn[0]
    inf.fio = inn[1]
    inf.prid = int(inn[2])
    inf.clas = inn[3]
    inf.score = inn[4]
    students.append(inf)

index_chela = int(input())
if index_chela > 500:
    print('ты шо, куку?')
else:
    for j in students:
        if j.prid == index_chela:
            print('Проект № ', j.prid, 'делал ', j.fio, 'он получил оценку', j.score)