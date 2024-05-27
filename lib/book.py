#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = self.validate_page_count(page_count)
    
    def validate_page_count(self, page_count):
        if not isinstance(page_count,int):
            return "page_count must be an integer"
        return page_count
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    pass
    
        