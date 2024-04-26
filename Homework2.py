class student:
    name: str
    age: int
    group: str
    money: int
    rest: int
    mark: int
    day: int

    def __init__(self, name, age, group, money, work, mark, day):
        self.name = name
        self.age = age
        self.group = group
        self.money = money
        self.work = work
        self.mark = mark
        self.day = day
    def printInfo(self):
        print(f"student: {student1.name} - {student1.age} - {student1.group} - {student1.money}")
    def work(self):
        
        if self.work:
            print(f'{self.name} earned 50$ ')
            self.money += 50
        else:
            print(f'{self.name} spend 25$')
            self.money -= 25
        if self.money < 200:
            print(f'{self.name} time to work')
        else:
            print(f'{self.name} can rest')

    def mark(self):
        if self.mark < 9:
            print(f'{self.name} time to learn')
        else:
            print(f'{self.name} studies well')

    def day(self):
        if self.day == 365:
            print(f'{self.name} lives year')
        else:
            self.day += 1
            print(f'{self.name} lives {self.day}')

student1 = student(name='Daniil', age=14, group='C2126', money=0, work=0, mark=0, day=0)
student1.printInfo()