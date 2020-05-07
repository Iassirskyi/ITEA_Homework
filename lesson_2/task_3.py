class Dot:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = value

    def get_z(self):
        return self.z

    def set_z(self, value):
        self.z = value

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return x, y, z

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return x, y, z

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x, y, z

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return x, y, z

    def __neg__(self):
        return Dot(- self.x, - self.y, - self.z)





my_dot = Dot(1, 2, 3)
my_dot_2 = Dot(4, 5, 6)
truediv_dot = my_dot / my_dot_2
print(truediv_dot)