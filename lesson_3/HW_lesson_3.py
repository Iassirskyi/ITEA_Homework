class MyStack:

    def __init__(self):

        self.items = []

    def empty(self):
        return self.items == []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()


    def show(self):
        return self.items


    def size(self):
        return len(self.items)



class MyQueue:

    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop(0)

    def show(self):
        return self.items


    def size(self):
        return len(self.items)


class ComplexNumber:

    def __init__(self, real, image):

        self.real = real
        self.image = image
        self.number = self.complex_num(real, image)


    @staticmethod
    def complex_num(real, image):
        return complex(real, image)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        real = self.real + other.real
        image = self.image + other.image
        return ComplexNumber(real, image)

    def __sub__(self, other):
        real = self.real - other.real
        image = self.image - other.image
        return ComplexNumber(real, image)

    def __mul__(self, other):
        real = self.real * other.real
        image = self.image * other.image
        return ComplexNumber(real, image)

    def __truediv__(self, other):
        real = self.real / other.real
        image = self.image / other.image
        return ComplexNumber(real, image)


num = ComplexNumber(1, 2)
print(num)
num_2 = ComplexNumber(3, 4)
sum_num = num + num_2
print(sum_num)





