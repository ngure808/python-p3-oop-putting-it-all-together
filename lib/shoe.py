#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = self.validate_size(size)
        self.condition = "New"

    def validate_size(self, size):
        if not isinstance(size, int):
            return "size must be an integer"
        return size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"