
class HaveLength:
    def __len__(self):
        return 123456789

def func(obj):
    print("len", len(obj))

def main():
    func(HaveLength())

main()
