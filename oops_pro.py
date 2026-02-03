class chatbook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = []

    def add_page(self, content):
        self.pages.append(content)

    def get_page(self, page_number):
        if 0 <= page_number < len(self.pages):
            return self.pages[page_number]
        else:
            return "Page not found."

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Total Pages: {len(self.pages)}"