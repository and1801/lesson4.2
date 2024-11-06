class Test():
    def public_func(self):
        print('публичный метод')

    def _protected_func(self):
        print('защищенный метод')

    def __private_func(self):
        print('приватный метод')

    def test_private(self):
        self.__private_func()

test1 = Test()

test1.public_func()

test1._protected_func()

test1.test_private()