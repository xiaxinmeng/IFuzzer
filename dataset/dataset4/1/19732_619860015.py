from itertools import combinations


class NotSortable:
    def __init__(self, id_):
        self.id = id_

    def __repr__(self):
        return f'{self.id}'


sorted([NotSortable(3), NotSortable(2)])
## TypeError: '<' not supported between instances of 'NotSortable' and 'NotSortable'
combs = list(combinations([NotSortable(3), NotSortable(2), NotSortable(4), NotSortable(1)], 2))
print(combs)
## [(3, 2), (3, 4), (3, 1), (2, 4), (2, 1), (4, 1)]