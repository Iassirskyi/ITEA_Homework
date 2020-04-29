def bank(deposit, years, percent):
    return deposit + (int(deposit)*float(percent)/100)*int(years)

deposit = int(input('Your cash: '))
years = int(input('How many years: '))
percent = float(input('What is percent: '))
my_deposit = bank(deposit, years, percent)
print(f'after {years} years you take {my_deposit}')