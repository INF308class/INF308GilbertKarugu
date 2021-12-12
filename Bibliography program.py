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
    # prints the details of the object
    def __str__(self):
        cite_str = ""
        for i, author_details in enumerate(self.authors):
            if i == self.author_num - 1 and self.author_num > 1:
                cite_str += " & "
            cite_str += f"{author_details['last']}, {author_details['first'][0]}."
        cite_str += f", ({self.year}). {self.title}. {self.publisher}."
        return cite_str

    # this method writes the details of the object to a file
    def write_to_file(self, filename):
        try:
            with open(filename, 'a') as f:
                f.write(self.__str__())
                f.write("\n")
        except:
            print(" Error while writing to file!")
        else:
            print(" Successfully written to file!")
class Article(Book):
    # add some additional attributes and call the original constructor
    def __init__(self, author_num, year, title, journal, vol, issue, pages, url):
        super().__init__(author_num, year, title, journal)
        self.vol = vol
        self.issue = issue
        self.pages = pages
        self.url = url

    # print details of the article using __str__ method
    def __str__(self):
        cite_str = ""
        for i, author_details in enumerate(self.authors):
            if i == self.author_num - 1 and self.author_num > 1:
                cite_str += " & "
            cite_str += f"{author_details['last']}, {author_details['first'][0]}."
        cite_str += f", ({self.year}). {self.title}. {self.publisher}, {self.vol}({self.issue}), {self.pages}. {self.url}"
        return cite_str
