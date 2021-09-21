import os
import hashlib


class Password:
    def __init__(self, passwd=''):
        self.N = 8
        self.password = passwd
        salt = os.urandom(self.N)
        self.storage = salt + self.make_key(passwd, salt)

    def make_key(self, passwd, salt):
        return hashlib.pbkdf2_hmac(
            'sha256',  # Используемый алгоритм хеширования
            passwd.encode('utf-8'),  # Конвертируется пароль в байты
            salt,  # Предоставляется соль
            10000)

    def get_storage(self):
        return self.storage

    def set_storage(self, storage):
        self.storage = storage

    def check_passwd(self, passwd):
        salt = self.storage[:self.N]
        return self.storage[self.N:] == self.make_key(passwd, salt)


if __name__ == '__main__':
    ph = Password(input())
    print(ph.get_storage())
    while (psw := input()):
        print(ph.check_passwd(psw))


