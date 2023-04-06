def gen():
    try:
        yield 1
    finally:
        print('finalize inner')

def func():
    try:
        for x in gen():
            break
    finally:
        print('finalize outer')

func()
print('END')