
import enum
from concurrent.futures import ThreadPoolExecutor


class MyEnum(enum.IntFlag):
    one = 1


with ThreadPoolExecutor() as executor:
    print(list(executor.map(MyEnum.one.__or__, range(1000))))
