#!/usr/bin/python3
"""
Import ABC (Abstract Base Class) and abstractmethod
from the abc module, these allow you to create abstract classes.

"""


class VerboseList(list):
    # Override append to print a message after adding an item
    def append(self, item):
        super().append(item)  # Call the original list.append
        print(f"Added [{item}] to the list")

    # Override extend to print how many items were added
    def extend(self, iterable):
        count = len(iterable)  # Number of elements being added
        super().extend(iterable)  # Call the original list.extend
        print(f"Extended the list with [{count}] items")

    # Override remove to print a message before removing the item
    def remove(self, item):
        print(f"Removed [{item}] from the list")
        super().remove(item)  # Call the original list.remove

    # Override pop to print a message before removing the item
    def pop(self, index=-1):
        item = self[index]  # Retrieve the element before removal
        print(f"Popped [{item}] from the list")
        return super().pop(index)  # Call the original list.pop
