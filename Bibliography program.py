
class Book:
# This program will cite a book in APA Format
    # constructor for the book class
    def __init__(self, author_name, year, title, publisher):
       self.author_name = author_name
       self.year = year
       self.title = title
       self.publisher = publisher
       self.authors = []
    # method to get author/s names
    def input_authors(self):
        for i in range(self.author_name):
           new_author = dict()
           new_author['first'] = input(f"author {i} - Enter first name: ")
           new_author['last'] = input(f"author {i} - Enter last name: ")
           self.authors.append(new_author)
    # prints the details of the object
    def __str__(self):
        cite_str = ""
        for i, author_details in enumerate(self.authors):
            if i == self.author_name - 1 and self.author_name > 1:
                cite_str += " & "
            cite_str += f"{author_details['last']}, {author_details['first'][0]}."
        cite_str += f", ({self.year}). {self.title}. {self.publisher}."
        return cite_str

    #  writes details of the object to a file
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
    # adds attributes and calls the original constructor
    def __init__(self, author_num, year, title, journal, vol, issue, pages, url):
        super().__init__(author_num, year, title, journal)
        self.vol = vol
        self.issue = issue
        self.pages = pages
        self.url = url

    # print article details as a string
    def __str__(self):
        cite_str = ""
        for i, author_details in enumerate(self.authors):
            if i == self.author_name - 1 and self.author_name > 1:
                cite_str += " & "
            cite_str += f"{author_details['last']}, {author_details['first'][0]}."
        cite_str += f", ({self.year}). {self.title}. {self.publisher}, {self.vol}({self.issue}), {self.pages}. {self.url}"
        return cite_str
def create_article_entry():
    author_count = int(input("Enter number of authors: "))
    pub_year = int(input("Enter year of article publication: "))
    article_title = input("Enter title of work: ")
    journal_name = input("Enter the name of the journal: ")
    volume_no = int(input("Enter volume number: "))
    issue_no = int(input("Enter issue number: "))
    page_range = input("Enter page range: ")
    url = input("Enter URL: ")

    # creates an Article class instance
    new_article = Article(author_count, pub_year, article_title, journal_name, volume_no, issue_no, page_range, url)                       
    # records author/s names
    new_article.input_authors()
    # print the citation entry
    print(new_article)
    # save to a file
    filename = input("Enter the name of file to write to: ")
    new_article.write_to_file(filename)
def create_book_entry():
    # get user inputs
    author_count = int(input("Enter number of authors: "))
    pub_year = int(input("Enter year of publication: "))
    work_title = input("Enter title of work: ")
    pub_name = input("Enter the name of the publisher: ")

    # create Book class instance
    new_book = Book(author_count, pub_year, work_title, pub_name)
    # record author/s names
    new_book.input_authors()
    # print citation entry
    print(new_book)
    # save to a file
    filename = input("Enter the name of file to write to: ")
    new_book.write_to_file(filename)
    
def main():
    # loop repeats until user quits by selecting choice number 3
    while True:
        choice = input("Enter a choice:\n1. Cite a book\n2. Cite an article\n3. Quit\n> ")
        if choice == '1':
            create_book_entry()
        elif choice == '2':
            create_article_entry()
        elif choice == '3':
            print("Quitting")
            break
        else:
            print("Invalid format! Please enter correct data format.")

if __name__ == "__main__":
    main()
