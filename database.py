# Code written by F226093
# The methods that actually write to the database 
from datetime import datetime,timedelta

# These define all the methods required to check in, checkout, reserve a book
def bookDataMethods(bookID, memberID, date, method):
    print(date)
    print("runs")
    currentDate = datetime.strptime(str(date), "%m-%d-%y")
    extraDays = timedelta(days=21)
    dueDate = currentDate + extraDays
    f = open('logfile.txt', 'a')
    if(method == "check-out"):
        f.write(str(bookID) + ":"+str(memberID) + ":Checkout" + ":"+str(date)+":"+str(dueDate.strftime("%m-%d-%y")))
        f.write('\n')
    elif(method == "reserve-check-out"):
        f.write(str(bookID) + ":"+str(memberID) + ":Fully-Checked-Out" + ":"+str(date)+":"+str(dueDate.strftime("%m-%d-%y")))
        f.write('\n')
    elif(method == "check-in"):
        f.write(str(bookID) + ":"+str(memberID) + ":Checkin" + ":"+str(date))
        f.write('\n')
    elif(method == "reserve"):
        f.write(str(bookID)+":"+str(memberID) + ":" + "Reserve"+":"+str(date))
        f.write('\n')
    f.close()

# All books raw
def allBooks():
    f = open("Book_Info.txt", "r")
    data = f.readlines()
    f.close()
    return data

# reading all the book records and put them in array 
def allBooksStripped():
    books = allBooks()
    allBook = []
    for line in books:
        s = line.strip()
        entries = s.split(":")
        allBook.append(entries)
    return allBook


# Reading all the log records and putting them in array 
def logFileRead():
    f = open('logfile.txt', 'r')
    data = f.readlines()
    allLogs = []
    for x in data:
        s = x.strip()
        entries = s.split(":")
        allLogs.append(entries)
    return(allLogs)

# Adding a new book 
def addBook(Genre, Title, Author, price, purchaseDate):
    f = open("Book_Info.txt", "a")

    id = len(allBooksStripped())+1
    
    f.write(str(id) + ":" + str(Genre) + ":"+str(Title)+":"+str(Author) +
            ":£"+str(price)+":"+str(purchaseDate))
    f.write('\n')
    f.close()



