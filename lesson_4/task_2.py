from datetime import date


class User:

    user_dict = {'User1': 'user1',
                 'User2': 'user2', }

    def __init__(self, login, password):

        self._login = login
        self._password = password
        self._post = None
        self._time = None

    def get_login(self, name):
        self._login = name
        return self._login

    def check_login(self, name):
        if name in self.user_dict:
            return False
        else:
            return True

    def check_password(self):

        digits = []
        upper = []

        if len(password) < 5:
            print('Password must be > 5 letters')

        for i in password:
            if i.isdigit():
                digits.append(i)
                for j in password:
                    if j.isupper():
                        upper.append(j)

        if len(digits) == 0:
            print('Password must contain numbers')
        elif len(upper) == 0:
            print('Password must contain one upper letter')
            return False
        else:
            return True

    def confirm_password(self, confirm_password):
        self._password = confirm_password
        return True

    def create_user(self):
        self.user_dict[self._login] = [self._password]

    def create_post(self, some_text):
        self.user_dict[self._login] = [self._password, some_text, str(date.today())]
        return self.user_dict


class UserAdmin(User):

    admin_dict = {'admin': 'admin'}

    def __init__(self, login, password):
        super().__init__(login, password)

    def show_user(self):
        return self.user_dict


print('Welcome to simple social network')

name = ''
password = ''
adm_name = ''
adm_password = ''
users = User(name, password)
users_admin = UserAdmin(adm_name, adm_password)

while True:

    network = int(input(f'Please enter what you want to do: \n1) Create account'
                        f'\n2) Join \n3) Admin only \n4) Exit\n  '))

    if network == 1:

        name = input('Enter your login ')
        if not users.check_login(name):
            print(f'User {name} its all ready create, try another ')
            continue
        users.get_login(name)

        password = input('Enter your password ')
        if not users.check_password():
            continue

        confirm = input('Confirm your password: ')
        if not users.confirm_password(confirm):
            continue

        users.create_user()
        print(f'User {name} was created')
        post = input(f'Welcome {name} in simple social network\n Do you want to create your firs post?'
              f'\nEnter yes/no ')

        if post == 'yes':
            text = input('Enter your text ')
            users.create_post(text)
            print('You added your post')
            exit = input('Do you want to exit? ')
            if exit == 'yes':
                print('See you next time')

        elif post == 'no':
            exit = input('Do you want to exit? ')
            if exit == 'yes':
                print('See you next time')
        continue

    if network == 2:

        name = input('Enter your login ')
        if not name in users.user_dict:
            print(f'User {name} not found, please registered to enter ')
            continue
        users.get_login(name)
        password = input('Enter your password ')
        if password != users.user_dict[name][0]:
            print('Wrong password')
            continue
        else:
            print(f'Welcome back {name}')
        users.confirm_password(password)
        action = input('Dou you want to create post? ')
        if action == 'yes':
            text = input('Enter your text ')
            users.create_post(text)
        print('You added your post')
        exit = input('Do you want to exit? ')
        if exit == 'yes':
            print('See you next time')
        continue

    if network == 3:

        print(f'You want enter like admin')
        adm_name = input('Enter your login ')
        if not adm_name in users_admin.admin_dict:
            print('Wrong login, try again')
            continue
        adm_password = input('Enter your password: ')
        if adm_password == users_admin.admin_dict[adm_name]:
            print(f'Welcome back {adm_name}')
        else:
            continue

        action = input('Do you want to see information about users ')
        if action == 'yes':
            print(users_admin.show_user())
        continue

    if network == 4:
        print('Have a nice day, good luck')
        break