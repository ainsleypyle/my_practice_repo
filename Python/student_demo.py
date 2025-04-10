from student import Student

student1=Student("Emily", "Smith", '123')
print(student1)
student1.greeting()
print(student1.get_energy_level())
student1.take_exam()
print(student1.get_energy_level())

student2=Student("John", "Smith", '456')
print(student2)
print(student2.get_energy_level())
student2.take_exam()
student2.take_exam()
print(student1.get_energy_level())
print(student2.get_energy_level())
