class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level

    def __repr__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Invalid user.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print(f"User with ID {user_id} not found.")

    def list_users(self):
        return self._users

    def __repr__(self):
        return f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


# Пример использования
if __name__ == "__main__":
    # Создаем админа
    admin = Admin(1, "Alice")

    # Создаем пользователей
    user1 = User(2, "Bob")
    user2 = User(3, "Charlie")

    # Админ добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Выводим список пользователей
    print("Current users:")
    for user in admin.list_users():
        print(user)

    # Админ удаляет пользователя
    admin.remove_user(2)

    # Выводим список пользователей после удаления
    print("Users after removal:")
    for user in admin.list_users():
        print(user)