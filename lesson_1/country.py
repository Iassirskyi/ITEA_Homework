country_dict = dict(
    Italy = 'Rome',
    France = 'Paris',
    Ukraine = 'Kyiv',
    Spain = 'Madrid',
    Germany = 'Berlin'
)

some_list = ['Ukraine', 'France', 'Argentina', 'Japan']

for i in some_list:
    if i in country_dict.keys():
        print(country_dict[i])