class Person():
    pass

class Cat():

    pass

class Dog:
    pass
class Student:
    school='beijingjiaoyu'

    def __init__(self,xm,age):
        self.name=xm
        self.age=age
    def show(self):
        print(f'wojiao{self.name},jinnian{self.age}')

    @staticmethod
    def sm():
        print('zheshiyigejingtaifangfa ,buneng diaoyong shilishux ')

    @classmethod
    def cm(cls  ):
        print('leifangfa,bunengdiaoyng')



stu=Student('yes','18')

print(stu.name,stu.age)
print(Student.school)
stu.show()
stu.cm()
Student.cm()