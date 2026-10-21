import abc
from enum import Enum

class TreeType(Enum):
    DECIDUOUS = "лиственное"
    CONIFEROUS = "хвойное"


class Tree(abc.ABC):
    def __init__(self, name: str, age: int, tree_type: TreeType):
        self.name = name
        self.age = age
        self.tree_type = tree_type

    def print_info(self):
        print(f"Название: {self.name}, Возраст: {self.age}, Тип: {self.tree_type.value}", end="")

    @abc.abstractmethod
    def get_type(self) -> str:
        pass


class ForestTree(Tree):
    def __init__(self, name: str, age: int, tree_type: TreeType, wood_volume: float):
        super().__init__(name, age, tree_type)
        self.wood_volume = wood_volume

    def print_info(self):
        super().print_info()
        print(f", Количество древесины: {self.wood_volume}")

    def get_type(self) -> str:
        return "ForestTree"


class FruitTree(Tree):
    def __init__(self, name: str, age: int, tree_type: TreeType, harvest_mass: float, storage_life: int):
        super().__init__(name, age, tree_type)
        self.harvest_mass = harvest_mass
        self.storage_life = storage_life

    def print_info(self):
        super().print_info()
        print(f", Масса урожая: {self.harvest_mass}, Срок хранения: {self.storage_life}")

    def get_type(self) -> str:
        return "FruitTree"


class TreeContainer:
    def __init__(self):
        self.trees = []

    def load_from_file(self, filename: str):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")
                    if not parts or parts[0] == "":
                        continue
                    
                    kind = parts[0]
                    name = parts[1]
                    age = int(parts[2])
                    tree_type = TreeType.CONIFEROUS if parts[3].lower() == "хвойное" else TreeType.DECIDUOUS
                    
                    if kind == "Forest":
                        wood_volume = float(parts[4])
                        self.trees.append(ForestTree(name, age, tree_type, wood_volume))
                    elif kind == "Fruit":
                        harvest_mass = float(parts[4])
                        storage_life = int(parts[5])
                        self.trees.append(FruitTree(name, age, tree_type, harvest_mass, storage_life))
        except FileNotFoundError:
            print(f"ошибка: файл {filename} не найден")

    def print_all_trees(self):
        for tree in self.trees:
            tree.print_info()

    def count_by_types_and_kinds(self):
        deciduous_count = 0
        coniferous_count = 0
        forest_count = 0
        fruit_count = 0
        
        for tree in self.trees:
            if tree.tree_type == TreeType.DECIDUOUS:
                deciduous_count += 1
            else:
                coniferous_count += 1
                
            if tree.get_type() == "ForestTree":
                forest_count += 1
            elif tree.get_type() == "FruitTree":
                fruit_count += 1
                
        print(f"Лиственных: {deciduous_count}, Хвойных: {coniferous_count}")
        print(f"Лесных: {forest_count}, Плодовых: {fruit_count}")

    def print_sorted(self):
        self.trees.sort(key=lambda tree: (tree.name, -tree.age))
        self.print_all_trees()


def main():
    with open("trees.txt", "w", encoding="utf-8") as f:
        f.write("Forest;Дуб;120;лиственное;15.5\n")
        f.write("Fruit;Яблоня;15;лиственное;50.0;30\n")
        f.write("Forest;Сосна;80;хвойное;8.2\n")
        f.write("Fruit;Груша;15;лиственное;40.0;20\n")
        f.write("Forest;Дуб;45;лиственное;4.1\n")

    container = TreeContainer()
    container.load_from_file("trees.txt")
    
    print("все деревья из файла")
    container.print_all_trees()
    
    print("\nстатистика по типам и видам")
    container.count_by_types_and_kinds()
    
    print("\nсортировка (по названию (возрастание), по возрасту (убывание))")
    container.print_sorted()

if __name__ == "__main__":
    main()