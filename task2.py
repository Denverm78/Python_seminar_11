# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# 📌 list-архивы также являются свойствами экземпляра

class Archive():
    """The class stores a couple of properties: a number and a string"""
    
    _flag = None

    def __new__(cls, number: int, text: str):
        """The function creates archive lists with old data"""
        
        if cls._flag == None:
            cls._flag = super().__new__(cls)
            cls._flag.archNumber = []
            cls._flag.archText = []
        elif cls._flag != None:
            cls._flag.archText.append(cls._flag.text)
            cls._flag.archNumber.append(cls._flag.number)
        return cls._flag

    def __init__(self, number: int, text: str):
        self.number = number
        self.text = text
        
    def __str__(self):
        return f'{self.archText}, {self.archNumber}, {self.text}, {self.number}'


t1 = Archive(10, "Разработка грунта вручную в траншеях")
t2 = Archive(12, "Засыпка вручную траншей, пазух котлованов")
t3 = Archive(14, "Нанесение нормальной антикоррозионной изоляции")

print(t3)
# help(Archive)
