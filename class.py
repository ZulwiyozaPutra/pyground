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

    def print_average_marks(self):
        print(self.average())

    @staticmethod
    def static_to_school():
        print("I'm going to school")

    @classmethod
    def student_to_school(cls):
        student = cls("Unknown name", "Unknown school")
        print("I'm  going to school %s" % student.school)

    def just_to_school(self):
        print("I'm going to %s school" % self.school)


anna = Student("anna", "MIT")
anna.marks.append(56)
anna.marks.append(70)
anna.print_average_marks()

Student.student_to_school()


class Store(object):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name,
        # plus " - franchise"
        name = store.name + " - franchise"
        new_store = cls(name)
        return new_store

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{name}, total stock price: {total}".format(
            name=store.name, total=store.stock_price())


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
print(Store.franchise(store))  # -> a Store with name "Test - franchise"
print(Store.franchise(store2))  # -> a Store with name "Amazon - franchise"
print(Store.store_details(store))  # -> "Test, total stock price: 0"
print(Store.store_details(store2))
