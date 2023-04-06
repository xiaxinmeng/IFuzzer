class Person:
        population = 0
        def __del__(self):
                Person.population -= 1

wolf = Person()