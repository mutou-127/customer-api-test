class Student:
    school='beijingjiaoyu'

    def __init__(peo,xm,age):
        peo.name=xm
        peo.age=age
    def show(self):
        print(f'wojiao{self.name},jinnian{self.age}')

stu=Student('ysj','18')
stu2=Student('cmm','20')
stu3=Student('ml','23')


print(type(stu))

Student.school='python'

lst=[stu,stu2,stu3]
for i in lst:
    i.show()
