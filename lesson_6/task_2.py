class MyDict:

    def __init__(self, *args):
        self.my_dict = {}
        for key, values in args:
            self.my_dict[key] = values

    def __getitem__(self, key):
        return self.my_dict[key]

    def __setitem__(self, key, value):
        self.my_dict[key] = value

    def set_dict(self, new_dict):
        self.my_dict = new_dict

    def __str__(self):
        return str(self.my_dict)

    def __add__(self, other):
        sum_dict = MyDict()
        sum_dict.set_dict({**self.my_dict, **other.my_dict})
        return sum_dict
