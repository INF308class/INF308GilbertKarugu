class Book:
    # constructor for the book class
    def __init__(self, author_num, year, title, publisher):
       self.author_num = author_num
       self.year = year
       self.title = title
       self.publisher = publisher
       self.authors = []

    # method to get author names
    def input_authors(self):
        for i in range(self.author_num):
           new_author = dict()
           new_author['first'] = input(f"author {i} - Enter first name: ")
           new_author['last'] = input(f"author {i} - Enter last name: ")
           self.authors.append(new_author)
