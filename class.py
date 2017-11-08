class LotteryPlayer(object):
    def __init__(self, name, age):
        self.name = age
        self.age = age
        self.number = (5, 9, 12, 3, 1, 21)


rob = LotteryPlayer("Rob", 23)
andy = LotteryPlayer("andy", 24)


class Student(object):
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anna = Student("anna", "MIT")
anna.marks.append(56)
anna.marks.append(70)
print(anna.average())
