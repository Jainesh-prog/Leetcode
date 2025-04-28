import random

class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}  # \U0001f50e Maps value -> its index in array
        self.arr = []         # \U0001f4e6 Array of inserted values

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False  # Already exists
        self.arr.append(val)
        self.val_to_idx[val] = len(self.arr) - 1  # \U0001f4dd Save index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False  # Doesn't exist

        # ✏️ Move the last element to the position of the element to delete
        last_element = self.arr[-1]
        idx_to_remove = self.val_to_idx[val]

        self.arr[idx_to_remove] = last_element
        self.val_to_idx[last_element] = idx_to_remove

        # ❌ Remove last element
        self.arr.pop()
        del self.val_to_idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)  # \U0001f3af Random access in O(1)
