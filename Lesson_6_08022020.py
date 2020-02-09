# def print_human_name(human):
#     print(human['name'])
#
#
# h1 = {'name': 'qwe'}
# h2 = {'name': 'asd'}
# h3 = {'name': 'zxc'}
# h4 = {'full_name': 'zxc'}
#
# print_human_name(h4)

class Phone:
    def __init__(self, phone_model):
        self.model = phone_model
        self.__id = 987654321
        self._loading()

    def call(self):
        print('calling')

    def _loading(self):
        print(self.model, 'loading')

    def get_id(self):
        return self.__id


# my_phone_1 = Phone('nokia 1100')
# print(my_phone_1.get_id())
# print(my_phone_1._Phone__id)
# my_phone_1.call()
# print(my_phone_1.model)

class SmartPhone(Phone):

    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')


# my_s_phone = SmartPhone('nokia6600')
# my_s_phone.call()
# my_s_phone.sms()


class Iphone(SmartPhone):
    def __init__(self, phone_model):
        super().__init__(phone_model)
        self.iphone_lamp = True
        print('show logo')

    def sms(self):
        print('Imessage sending')

    def player(self):
        print('music...')

    def browser(self):
        print('internet...')


# iphone = Iphone('6')
# iphone.sms()

class NextGenerationPhone(Iphone):
    def touch_id(self):
        print('touch_id')

    def pay(self):
        print('pay')


class Huawei(NextGenerationPhone):
    pass


class Samsung(NextGenerationPhone):
    pass


# qwe = Samsung(1)
# asd = Huawei(2)

class Player:
    def player_method(self):
        print('player_method')


class Navigator:
    def nav_method(self):
        print('nav_method')


class MobilePhone(Player, Navigator):
    def mob(self):
        print('mob')


# mob = MobilePhone()
# mob.player_method()
# mob.nav_method()
# mob.mob()


class Auto:
    def start(self, param1, param2=None):
        if param2 is not None:
            print(param1 + param2)
        else:
            print(param1)


# a = Auto()
# a.start(50)
# a.start(50, 200)


class Transport:
    def show_info(self):
        print('родитель')


class Auto(Transport):
    def show_info(self):
        print('дочерний')

t = Transport()
t.show_info()

a = Auto()
a.show_info()



