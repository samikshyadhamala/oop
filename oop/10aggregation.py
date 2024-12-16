#aggregation=a relationship where one objects(the whole) contains reference to one or more independent objects(the parts)
#Aggression (Inheritance): The Toy Car is a Toy and just gets more stuff added to it.
#Composition: The Toy Car has-a Toy Engine that helps it work, but they’re still separate.
class library:#independent
    def __init__(self,lib_name):#creating a library ,give it a name
        self.lib_name=lib_name#store the name of the library
        self.read=[]#create an empty list to store books
    
    def add_books(self,book):#add a books to the library
        self.read.append(book)#add the book to the book list
        
    def list_read_book(self):#list all the books int he library
        for broke in self.read:
            print(f"{broke.title} by {broke.author}")
            
        
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
library1=library("royal library")#ceate a new library

book1=book("abc","me")#creates a new books
book2=book("def","you")
book3=book("ghi","we")

# print(book1.title)

library1.add_books(book1)#add the book to the library
library1.add_books(book2)
library1.add_books(book3)

library1.list_read_book()#list all the book in the libraryl
#if we delete library objects the book will still exists 