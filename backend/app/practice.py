#1.函数
def say_hello(name):
    print(f"Hello, {name}")


say_hello("Ray")
say_hello("Agent")
#2.类型注解
def get_file_type(filename: str) -> str:
    return filename.split(".")[-1]


def calculate_file_size_kb(size_bytes: int) -> float:
    return size_bytes / 1024


print(get_file_type("test.pdf"))
print(calculate_file_size_kb(2048))
#3。基础类用法
class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email


user = User(1, "ray", "ray@example.com")

print(user.user_id)
print(user.username)
print(user.email)
#4.dataclass
from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    username: str
    email: str
user = User(user_id=1, username="ray",email="ray@example.com")
print(user)