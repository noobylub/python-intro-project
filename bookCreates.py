# Code written by F226093
from datetime import datetime
from datetime import timedelta
from otherMethods import createRandomTime
from database import addBook
import random;




# creating a new book is the method below 
def newBook(Genre, Title, Author, price, date=False):
    dateAdded = datetime.today().strftime("%m-%d-%y")
    if(date == False):
        earlierDate = datetime.strptime('1/1/2008 ', '%m/%d/%Y ')
        laterDate = datetime.strptime('1/1/2022 ', '%m/%d/%Y ')
        dateAdded = createRandomTime(earlierDate, laterDate).strftime("%m-%d-%y")
    if(Genre == "" or Title == "" or Author == "" or price ==""):
        return False
    if(price < 0):
        return False
    addBook(Genre, Title, Author, price,dateAdded)
    return True



# Populating with random data and random books 
# All for the sake of testing when creating a book currently commented out as it is not needed anymore,
#  needed only in the beggin
# def createDummyData():
#     genres = ["Fantasy", "Historical-Fiction",
#               "Non-Fiction", "Classics", "Science-Fiction","Fantasy-Fiction"]
#     titles = ["Little Riding Hood", "A new life", "A new border",
#               "W HY", "Originals", "Watch out for aliens", "Romeo","Juliet","Borneo","Alien","Monster"]
#     authors = ["Bob Marley", "Gnarly Squad", "Soban Adnan",
#                "John Smith", "Adam Smith", "Mouse Facebook"]
    
#     newBook(genres[random.randint(0, len(genres)-1)], titles[random.randint(0,
#             len(titles)-1)], authors[random.randint(0,len(authors)-1)], random.randint(0, 500) )
# f = open('Book_info.txt', 'w')
# f.write("")
# for x in range(20):
#     createDummyData(); 


# newBook("Classics","Best Title", "James","£12", True)