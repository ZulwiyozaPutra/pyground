class Student(object):
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        friend = cls(friend_name, origin.school, salary)
        return friend


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent("Anna", "Oxford", 200.0)
roy = WorkingStudent.friend(anna, "Greg", 900.0)
print(roy.salary)
