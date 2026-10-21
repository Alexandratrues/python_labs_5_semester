class Student:
    _id_counter = 1

    def __init__(self, name: str, course: int, group: int, record_book: str):
        if not name or not record_book:
            print("конструктор без параметров запрещен")
            return

        self.id = Student._id_counter
        Student._id_counter += 1
        
        self.name = name
        self.course = course
        self.group = group
        self.record_book = record_book

    def copy_from(self, other):
        self.name = other.name
        self.course = other.course
        self.group = other.group
        self.record_book = other.record_book

    def get_average_grade(self) -> float:
        return 0.0

    def print_info(self):
        print(f"ID: {self.id}, имя: {self.name}, курс: {self.course}, группа: {self.group}, зачетка: {self.record_book}", end="")

    def get_type(self) -> str:
        return "Student"


class StudentSession1(Student):
    def __init__(self, name: str, course: int, group: int, record_book: str, grades1: list[int]):
        super().__init__(name, course, group, record_book)
        self.grades1 = (grades1 + [0] * 4)[:4]

    def copy_from(self, other):
        super().copy_from(other)
        if other.get_type() in ("StudentSession1", "StudentSession2"):
            self.grades1 = list(other.grades1)

    def get_average_grade(self) -> float:
        if not self.grades1:
            return 0.0
        return sum(self.grades1) / len(self.grades1)

    def print_info(self):
        super().print_info()
        print(f", оценки 1 сессии: {self.grades1}, средний балл: {self.get_average_grade():.2f}")

    def get_type(self) -> str:
        return "StudentSession1"


class StudentSession2(StudentSession1):
    def __init__(self, name: str, course: int, group: int, record_book: str, grades1: list[int], grades2: list[int]):
        super().__init__(name, course, group, record_book, grades1)
        self.grades2 = (grades2 + [0] * 5)[:5]

    def copy_from(self, other):
        super().copy_from(other)
        if other.get_type() == "StudentSession2":
            self.grades2 = list(other.grades2)

    def get_average_grade(self) -> float:
        all_grades = self.grades1 + self.grades2
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)

    def print_info(self):
        Student.print_info(self)
        print(f", оценки 1 сессии: {self.grades1}, оценки 2 сессии: {self.grades2}, средний балл (год): {self.get_average_grade():.2f}")

    def get_type(self) -> str:
        return "StudentSession2"


def print_group_avg_session1(university: list, group_num: int):
    total_sum = 0
    count = 0
    
    for obj in university:
        if obj.group == group_num:
            if obj.get_type() in ("StudentSession1", "StudentSession2"):
                if obj.get_type() == "StudentSession2":
                    temp = StudentSession1(obj.name, obj.course, obj.group, obj.record_book, obj.grades1)
                    total_sum += temp.get_average_grade()
                else:
                    total_sum += obj.get_average_grade()
                count += 1
                
    if count > 0:
        print(f"средний балл группы {group_num} после 1 сессии: {total_sum / count:.2f}")
    else:
        print(f"в группе {group_num} нет студентов после 1 сессии")


def print_group_avg_year(university: list, group_num: int):
    total_sum = 0
    count = 0
    
    for obj in university:
        if obj.group == group_num:
            if obj.get_type() == "StudentSession2":
                total_sum += obj.get_average_grade()
                count += 1
                
    if count > 0:
        print(f"средний балл группы {group_num} после 2 сессий (за год): {total_sum / count:.2f}")
    else:
        print(f"в группе {group_num} нет студентов после 2 сессий")


def main():
    sostav_univera = []

    sostav_univera.append(StudentSession1("Иван Иванов", 1, 101, "ЗАЧ-001", [4, 5, 4, 3]))
    sostav_univera.append(StudentSession1("Петр Петров", 1, 101, "ЗАЧ-002", [5, 5, 5, 4]))
    sostav_univera.append(StudentSession2("Анна Сидорова", 1, 101, "ЗАЧ-003", [4, 4, 5, 5], [5, 5, 4, 4, 5]))
    sostav_univera.append(StudentSession2("Олег Кузнецов", 1, 102, "ЗАЧ-004", [3, 3, 4, 3], [4, 3, 3, 4, 4]))

    print("список всех студентов")
    for obj in sostav_univera:
        obj.print_info()

    print("\nсредние баллы по группам")
    print_group_avg_session1(sostav_univera, 101)
    print_group_avg_year(sostav_univera, 101)

if __name__ == "__main__":
    main()
