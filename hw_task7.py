# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# 📌 Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    """The class contains a description of the matrix and operations on it"""
    def __init__(self, my_matrix):  
        self.rows = len(my_matrix)      
        self.cols = len(my_matrix[0])
        self.my_matrix = my_matrix
        
        
    def __str__(self):
        """Matrix output to the screen"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.my_matrix])
        

    def __add__(self, other):
        """Calculates the sum of matrices"""
        if self.rows != other.rows or self.cols != other.cols:
            print("Матрицы нельзя сложить, так как у них разный размер")
            exit()
        sum_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                sum_matrix[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
        return Matrix(sum_matrix)
    
    
    def __eq__(self, other):
        """Comparison of matrices for equality"""
        if self is other:
            return True
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.my_matrix[i][j] != other.my_matrix[i][j]:
                    return False
        return True
    

    def __mul__(self, other):
        """Multiplying a matrix by a number"""
        mul_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                mul_matrix[i][j] = self.my_matrix[i][j] * other
        return Matrix(mul_matrix)
    

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
matrix3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix1)
print()
print(matrix2)
print()
print(matrix3)
print()

print(f'{matrix1 == matrix2 = }')
print(f'{matrix1 == matrix3 = }')

print(f'{matrix1 != matrix2 = }')
print(f'{matrix1 != matrix3 = }')
print()
# print(matrix1 + matrix2)
print(matrix1 + matrix3)
print()
print(matrix1 * 5)