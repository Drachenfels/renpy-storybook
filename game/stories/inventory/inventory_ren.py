"""renpy
init -100 python:
"""


class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        print("Adding item", item, "to slot", len(self._items))
        self._items.append(item)

    def get_list_of_items(self, limit=25):
        items = self._items[:limit]

        if len(items) < 25:
            items += [None] * (25 - len(items))

        return items

    def remove_item(self, idx):
        print("Removing item from slot", idx)
        self._items.pop(idx)


class Item:
    def __init__(self, name, image):
        self.name = name
        self.image = image
