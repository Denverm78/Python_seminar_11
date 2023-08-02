# Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str 
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)

import time

class MyString(str):
    """The class has all the capabilities of a string and additionally stores
        the name of the author of the line and the time of creation"""
    
    def __new__(cls, text, nameAuthor):
        instance = super().__new__(cls, text)
        instance.text = text
        instance.t = time.time()
        instance.author = nameAuthor
        return instance

    def __str__(self):
        return f'{self.text}, автор - {self.author}, время создания - {self.t}'

text1 = "Random text"
text2 = "Other text"
d = MyString(text1, "Alexandr Pushkin")
e = MyString(text2, "Nikita Sergeev")

print(d)
print(d.t)
print(d.author)
print(d.__dict__)
# help(MyString)
print(e)