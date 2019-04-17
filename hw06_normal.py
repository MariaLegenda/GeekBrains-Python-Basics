
__author__ = 'Потапова Мария'

# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Student:
	def __init__(self, surname, name, patronymic, school_class, mother, father):
		self.name = name
		self.surname = surname
		self.patronymic = patronymic
		self.school_class = school_class
		self.mother = mother
		self.father = father
	
	def student_name(self):
		return '{} {}. {}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())
	
	def student_parents(self):
		return 'Отец: {}, мать: {}'.format(self.mother, self.father)
	
	def student_classes(self):
		return self.school_class 


class Teacher:
	def __init__(self, tname, tsurname, subject, classes):
		self.tname = tname
		self.tsurname = tsurname
		self.subject = subject
		self.classes = list(classes)

	
	def ttname(self):
		return '{} {}'.format(self.tname, self.tsurname)

	def tsubject(self):
		return self.subject 


		

teachers_list = [Teacher('Антон', 'Чехов', 'Русский язык', ['10Б', '11А']),
 Teacher('Васко', 'да Гамма', 'География', ['10А', '10Б', '11А', '11Б']),
 Teacher('Давид', 'Микеланджело', 'Искусство', ['10А', '10Б', '11А', '11Б']), 
 Teacher('Уильям', 'Шекспир', 'Литература', ['10А', '11Б']), 
 Teacher('Эрнест', 'Хемингуэй', 'Литература', ['10Б', '11А'])]


students_list = [Student('Шин', 'Тун', 'Яу', '10А', 'Шин А.А.', 'Шин Б.Б.'), 
Student('Раджгопал', 'Даббала', 'Редли', '10А', 'Даббала Л.Н.', 'Даббала Л.П.'),
Student('Коэн', 'Клод', 'Тануджи', '11А', 'Коэн П.О.', 'Коэн А.Н.'),
Student('Цуи', 'Дэниел', 'Физикович', '11А', 'Цуи О.П.', 'Цуи Н.А.'),
Student('Концевич', 'Максим', 'Янезнаювич', '10Б', 'Концевич А.С.', 'Концевич М.С.'),
Student('Сен', 'Амартия', 'Индиевич', '10Б', 'Морозова К. Е.', 'Морозов Г. М.'),
Student('Зевейл', 'Ахмед', 'Химович', '11Б', 'Зевейл П.О.', 'Зевейл А.Н.'),
Student('Физиков', 'Химик', 'Математикович', '11Б', 'Физиков Г.И.', 'Физикова Е.К.')]


# 1. Получить полный список всех классов школы

classes = []
for i in [st.student_classes() for st in students_list]:
    if i not in classes:
        classes.append(i)
print('\n1. Классы в школе: ', sorted(classes))

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")

info_class = '10А'
print('2. Ученики {} класса: '.format(info_class))
for st in students_list:
	if st.school_class == info_class:
		print('{:>45}'.format(st.student_name()))

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

info_student = 'Сен Амартия Индиевич'
for st in students_list:
	if  st.surname == info_student.split()[0] and st.name == info_student.split()[1] and st.patronymic == info_student.split()[2]:
		print("3. Класс ученика {} - {}:".format(info_student, st.student_classes() ))
	
print('4. Учителя указанного ученика: ')
for st in students_list:
	if st.surname == info_student.split()[0] and st.name == info_student.split()[1] and st.patronymic == info_student.split()[2]:
		st.student_classes()
		for t in teachers_list:
			for i in t.classes:
				if st.student_classes() == i:
					print('{:>45}'.format(t.ttname()))
					

print('5. Предметы указанного ученика: ')
for st in students_list:
	if st.surname == info_student.split()[0] and st.name == info_student.split()[1] and st.patronymic == info_student.split()[2]:
		st.student_classes()
		for t in teachers_list:
			for i in t.classes:
				if st.student_classes() == i:
					print('{:>45}'.format(t.tsubject()))


# 4. Узнать ФИО родителей указанного ученика

info_student = 'Физиков Химик Математикович'
print("6. ФИО родителей ученика {}:".format(info_student))
for st in students_list:
    if st.surname == info_student.split()[0] and st.name == info_student.split()[1] and st.patronymic == info_student.split()[2] :
        print('{:>45}'.format(st.student_parents()))

# 5. Получить список всех Учителей, преподающих в указанном классе

info_class = '10Б'
print('7. Учителя в {} классе : '.format(info_class))
for t in teachers_list:
	for i in t.classes:
		if i == info_class:
			print('{:>45}'.format(t.ttname()))
