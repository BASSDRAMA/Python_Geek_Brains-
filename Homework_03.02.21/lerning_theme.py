# class MotorsportTranport(object):
#     def __init__(self, year, color, auto_type):
#         self.year = year
#         self.color = color
#         self.auto_type = auto_type
#
#     def stop(self):
#         print('Тормоз в пол.... *вззззззжжжжж*')
#
#     def drive_fast(self):
#         print('Тапку в пол!....*WHHRRRRRRRRRR!!!*')
#
# range_rover_sport = MotorsportTranport(2012, 'white', 'crossover')
#
# range_rover_sport.drive_fast()
# range_rover_sport.stop()
#
# class Student:
#     def __init__(self, name, surname, group):
#         self.name = name
#         self.surname = surname
#         self.group = group
#
#     def recognize(self):
#         print(f'Меня зовут {self.name} по фамилии {self.surname}. Я учусь в группе {self.group}')
#
# student1 = Student('Олексей', "Нувульный", "Политтехнологии-33")
#
# student1.recognize()

# class Animal:
#     def usual_action(self):
#         print('kidding around')
#     def sound(self):
#         print('*animal sounds*')
#
# class Cat(Animal):
#     def sound(self):
#         print('*mew mew*')
#     def action(self):
#         print('Something has just dropped from the table')
#
# emi = Cat()
#
# emi.usual_action()
# emi.action()
# emi.sound()

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type, number_served):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#     def describe_restaurant(self):
#         print(f'Taking your attention {self.restaurant_name} with {self.cuisine_type} cuisine inside')
#
#     def open_restaurant(self):
#         print(f'{self.restaurant_name} is Open now')
#
#     def set_number_served(self, visitors):
#         self.number_served = visitors
#
#     def increment_number_served(self, pple):
#         self.number_served += pple
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, number_served):
#         super().__init__(restaurant_name, cuisine_type, number_served)
#         self.flavors = ('Chokolate', 'Vanilla', 'Cherry', 'Raspberry Pie')
#
#     def show_flavors(self):
#         print(f'Choose your fav taste {self.flavors}!!!')
#
#
# iceland_icecream = IceCreamStand('IceLand IceCram', 'icecream', 0)
#
# print(iceland_icecream.restaurant_name)
# iceland_icecream.show_flavors()
#
# #
# black_hat = Restaurant('Black Hat', 'European', 11)
# print(black_hat.restaurant_name)
# print(black_hat.cuisine_type)
# black_hat.increment_number_served(30)
# black_hat.increment_number_served(10)
# black_hat.increment_number_served(23)
# print(f'Visitors served today: {black_hat.number_served}')
# black_hat.describe_restaurant()
# black_hat.open_restaurant()


# dodo_pizza = Restaurant('DODO Pizza', 'Pizza')
# dodo_pizza.describe_restaurant()
#
# burger_king = Restaurant('Burger King', 'Burgers')
# burger_king.describe_restaurant()



class Privileges:
    def __init__(self, privileges_list=('ban allowed', 'remove user allowed', 'add mes allowed')):
        self.privileges_list = privileges_list

    def show_privileges(self):
        print(f'hi, my great ruler. here s your privileges: {self.privileges_list}')


class User:
    def __init__(self, name, last_name, email, age):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0
    def greet_user(self):
        print(f'Hi, {self.name}, Nice to see u')

    def describe_user(self):
        print(f'Your name is {self.name} {self.last_name},'
              f' u r {self.age} years old. \n Check up your email {self.email} ')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Oleg', 'Kuzin', 'razdvasobakashlyandex.sru', 21)

user1.greet_user()
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f'Logins tried: {user1.login_attempts}')
user1.reset_login_attempts()
print(f'Logins tried: {user1.login_attempts}')


class Admin(User):
    def __init__(self, name, last_name, email, age):
        super().__init__(name, last_name, email, age)
        self.privileges = Privileges()



admin1 = Admin('Oleg', 'Kuzin', 'lll', 22)
admin1.privileges.show_privileges()