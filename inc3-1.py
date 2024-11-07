class User():
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def set_name(self):
        self.__name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f'пользователь успешно добавлен в список')
        print(user_list)

    def remove_user(self, user_list, user):
        user_list.remove(user)



users = []
admin = Admin('a1', 'gosha')
user1 = User('u1', 'stepa')

print(user1.get_name())
admin.add_user(users, user1)





