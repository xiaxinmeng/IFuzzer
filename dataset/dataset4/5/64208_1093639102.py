class Dog:
    @property
    def age(self):
        return 42

if __name__ == '__main__':
    import inspect
    age_property = Dog.__dict__['age']
    lines, size = inspect.getsourcelines(age_property.fget)
    print(''.join(lines))