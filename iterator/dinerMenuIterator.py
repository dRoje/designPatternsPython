from iterator import Iterator
from menuItem import MenuItem
from typing import List


class DinerMenuIterator(Iterator):
    def __init__(self, items):
        # type: (List(MenuItem)) -> None
        assert isinstance(items, list)
        self.items = items
        self.position = 0

    def next(self):
        menuItem = self.items[self.position]
        self.position += 1
        return menuItem

    def hasNext(self):
        if self.position >= self.items.__len__() or self.items[self.position] is None:
            return False
        else:
            return True

    def remove(self):
        if self.position <= 0:
            raise Exception("Cant remove an item, do next()")
        self.items.pop(self.position)



