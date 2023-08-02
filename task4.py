# Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста и для пользователя.

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
        return f'Архив: {self.archText}, {self.archNumber},\nТекущие значения: {self.text}, {self.number}'


    def __repr__(self):
        return f'Archive: {self.text = }, {self.number = }'


t1 = Archive(10, "Разработка грунта вручную в траншеях")
t2 = Archive(12, "Засыпка вручную траншей, пазух котлованов")
t3 = Archive(14, "Нанесение нормальной антикоррозионной изоляции")

print(t3)
print(repr(t3))