class Person:
    def __init__(self, fio: str):
        self.fio = fio

    def print_info(self):
        print(f"ФИО: {self.fio}")


class Student(Person):
    def __init__(self, fio: str, course: int, group: int):
        super().__init__(fio)
        self.course = course
        self.group = group

    def print_info(self):
        print(f"студент ФИО: {self.fio}, курс: {self.course}, группа: {self.group}")


class Professor(Person):
    def __init__(self, fio: str, department: str):
        super().__init__(fio)
        self.department = department

    def print_info(self):
        print(f"преподаватель ФИО: {self.fio}, кафедра: {self.department}")


def main():
    sostav_univera = []

    while True:
        print("\nМЕНЮ")
        print("1. ввести студента")
        print("2. ввести преподавателя")
        print("3. вывести студентов")
        print("4. вывести преподавателей")
        print("5. конец")
        
        choice = input("выберите пункт: ")

        if choice == "5":
            break

        if choice == "1":
            fio = input("введите ФИО студента: ")
            course = int(input("введите курс: "))
            group = int(input("введите группу: "))
            sostav_univera.append(Student(fio, course, group))
        elif choice == "2":
            fio = input("введите ФИО преподавателя: ")
            department = input("введите кафедру: ")
            sostav_univera.append(Professor(fio, department))
        elif choice == "3":
            print("\nсписок студентов")
            for obj in sostav_univera:
                if isinstance(obj, Student):
                    obj.print_info()
        elif choice == "4":
            print("\nсписок преподавателей")
            for obj in sostav_univera:
                if isinstance(obj, Professor):
                    obj.print_info()
        else:
            print("нет такого пункта")

if __name__ == "__main__":
    main()
