# tee ratkaisusi tänne
class Course:
    def __init__(self, name, grade, credits):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade):
        if grade> self.__grade:
            self.__grade = grade

    @property
    def credits(self):
        return self.__credits


class ClassRecords:

    def __init__(self):
        self.__records = {}

    def add_entry(self, name, grade, credit):
        if name not in self.__records.keys():
            course = Course(name, grade, credit)
            self.__records[name] = course
            return
        self.__records[name].grade = grade

    def get_entry(self, name):
        if name not in self.__records:
            print('no entry for this course')
            return
        course = self.__records[name]
        print(f'{name} ({course.credits} cr) grade {course.grade}')

    def get_stats(self):
        credits = 0
        count = 0
        grade = []
        for course in self.__records.values():
            credits += int(course.credits)
            count +=1
            grade.append(int(course.grade))

        print(f'{count} completed courses, a total of {credits} credits')
        print(f'mean {sum(grade)/len(grade):.1f}')
        print('grade distribution')
        print(f'5: {grade.count(5)*'x'}')
        print(f'4: {grade.count(4)*'x'}')
        print(f'3: {grade.count(3)*'x'}')
        print(f'2: {grade.count(2)*'x'}')
        print(f'1: {grade.count(1)*'x'}')
            

class ClassRecordsApplication:

    def __init__(self):
        self.__classrecord = ClassRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_entry(self):
        name = input('course: ')
        grade = input('grade: ')
        credits = input('credits: ')
        self.__classrecord.add_entry(name, grade, credits)

    def get_entry(self):
        course = input('course: ')
        self.__classrecord.get_entry(course)

    def get_stats(self):
        self.__classrecord.get_stats()

    def execute(self):
        self.help()
        while True:
            print('')
            command = input('command: ')
            if command == '1':
                self.add_entry()
            elif command == '2':
                self.get_entry()
            elif command == '3':
                self.get_stats()
            elif command == '0':
                break
            else:
                self.help()

app = ClassRecordsApplication()
app.execute()