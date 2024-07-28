
"""
abs is built-in function , it return the absolute value of giving parametre (int ,float)
__abs__ to let know python what to do when abs() is called for an instance
"""

a = -44
b = 3 + 4j
abs_a = abs(a)
abs_b = abs(b)
print("the value: ", a, "the absolut value: ", abs_a)
print("the value: ", b, "the absolut value: ", abs_b)


class CrazyNumber:

    def __init__(self):
        self.cn = -6

    def __abs__(self):
        return abs(self.cn)


crazyNumber = CrazyNumber()

print("__abs__ :", abs(crazyNumber))
