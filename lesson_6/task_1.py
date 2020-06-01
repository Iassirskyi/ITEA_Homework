class MyList:

    def __init__(self, element=0):
        self.my_list = [0] * element

    def __getitem__(self, index):
        return self.my_list[index]

    def __setitem__(self, index, value):
        self.my_list[index] = value

    def set_list(self, other_list):
        self.my_list = other_list[:]

    def __str__(self):
        return str(self.my_list)

    def my_pop(self):
        pop_list = []
        for i in self.my_list:
            if i != self.my_list[-1]:
                pop_list.append(i)
        self.my_list = pop_list
        return pop_list

    def my_append(self, item):
        self.my_list = self.my_list[:] + [item]
        return self.my_list

    def my_insert(self, element, value):
        self.my_list = self.my_list[:value] + [element] + self.my_list[value:]
        return self.my_list

    def my_clear(self):
        self.my_list = []

    def my_index(self, element):

        for index, elements in enumerate(self.my_list):
            if elements == element:
                return index

    def my_remove(self, element):
        for index, elements in enumerate(self.my_list):
            if elements == element:
                self.my_list = self.my_list[:index] + self.my_list[(index + 1):]
                return self.my_list

    def __add__(self, other):
        sum_list = MyList()
        sum_list.set_list(self.my_list[:] + other[:])
        return sum_list