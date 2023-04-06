
# main.py
import sys

sys.path.append("src")

from src import user_1, user_2, user_3


if __name__ == '__main__':
    print(user_1.OBJECT is user_2.OBJECT) # True
    print(user_1.OBJECT is user_3.OBJECT) # False
