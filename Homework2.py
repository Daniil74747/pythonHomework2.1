class student:
    name: str
    age: int
    group: str
    money: int
    rest: int

    def __init__(self, name, age, group, money, work, rest):
        self.name = name
        self.age = age
        self.group = group
        self.money = money
        self.work = work
        self.rest = rest
    def printInfo(self):
        print(f"student: {student1.name} - {student1.age} - {student1.group} - {student1.money}")

    input(str('Did you work today?'))
    def work(self):

        if self.work:
            print(f'{self.name} earned 10$/hour')
        else:
            print(f'{self.name} dont earn nothing')
student1 = student(name='Daniil', age=14, group='C2126', money=0, work=0, rest=0)
student1.printInfo()