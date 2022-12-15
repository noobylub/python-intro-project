# Code written by F226093
from database import allBooksStripped, logFileRead
from datetime import datetime
# search a book by its type

# Utility method, showing the book given the ID
def searchID(id):
    books = allBooksStripped()
    for line in books:

        bookId = line[0]
        if (int(bookId) == int(id)):
            return line
    return (False)



# Utility method showing the amount of times a book has been checked out
def showLikedBook(bookId):
    datas = logFileRead()
    amountCheckedOut = 0
    for entry in datas:
        if (str(entry[0]) == str(bookId) and (str(entry[2]) == "Checkout" or str(entry[2]== "Fully-Checked-Out"))):
            amountCheckedOut += 1
    return bookId, amountCheckedOut




# Method to check the book status given the ID
def checkAvaiable(bookID):
    logs = logFileRead()
    
    idCheckedOut = ""
    personReserved = ""
    reserved = False
    bookAvaiable = True
    overDueDate = ""
    for entries in logs:
        # The four states, Checkedout but avaiable, Checked out with reserved
        # Checked in with reserved, Checked in and avaiable to reserve
        bookExist = searchID(bookID)
        if (bookExist == False):
            bookAvaiable = False
        elif (str(bookID) == str(entries[0]) and entries[2] == "Checkout"):
            overDueDate = entries[4]
            bookAvaiable = False
            idCheckedOut = entries
        elif (str(bookID) == str(entries[0]) and str(entries[2]) == "Reserve"):
            bookAvaiable = False
            reserved = True
            personReserved = entries
        elif (str(bookID) == str(entries[0]) and str(entries[2]) == "Fully-Checked-Out"):
            bookAvaiable = False
            reserved = False
            idCheckedOut = entries
            personReserved = ""
            overDueDate = entries[4]
        elif (str(bookID) == str(entries[0]) and str(entries[2]) == "Checkin"):
            bookAvaiable = True
            idCheckedOut = ""

    return bookAvaiable, idCheckedOut, reserved, personReserved,overDueDate





# Display the book status in a more friendly manner
def displayBookStatus(bookId):
    print("-"*30)
    statusBook = checkAvaiable(bookId)
    if (statusBook[0] == True and statusBook[2] == False):
        print("Book can not be Checked in")
        print("Book is Avaiable to check out")
    elif (statusBook[0] == False and statusBook[2] == False):
        print("Book is checked out by " + statusBook[1][1])
        print("Book is avaiable to reserve")
        print("Book is due by "+ statusBook[4])
    elif (statusBook[0] == True and statusBook[2] == True):
        print("Book is reseved")
        print("Book can only be checked out by " + statusBook[3][1])
    else:
        print("Book is checked out by " + statusBook[1][1])
        print("Book is reserved by " + statusBook[3][1])
        print("Book is due by "+ statusBook[4])


# Displaying the book info in a more friendly look 
def displayBookInfo(bookId, showStatus):
    book = searchID(bookId)
    print("Book ID: " + book[0])
    print("Genre: " + book[1])
    print("Title: " + book[2])
    print("Author: " + book[3])
    print("Price: " + book[4])
    print("Date Purchased: " + book[5])
    amountCheckedOut = showLikedBook(book[0])[1]
    print("Amount Checked-Out:"+ str(amountCheckedOut))
    if (showStatus == True):
        displayBookStatus(bookId)
    print("\n")

# Showing all the books given a search type and keywords to search them
def searchBook(type, search):
    allBookSpecific = []
    if (str(type) == "genre"):
        toShow = 1
    elif (str(type) == "author"):
        toShow = 3
    elif (str(type) == "title"):
        toShow = 2
    else:
        return ("Please show a valid type")
    books = allBooksStripped()
    # Ordering them
    allBookToDisplay = []
    for book in books:
       
        if (str(book[toShow]) == str(search)):
            amountChecked = showLikedBook(book[0])[1]
            allBookToDisplay.append((book, amountChecked))

    sorting = sorted(allBookToDisplay, key=lambda tup: tup[1], reverse=True)
    for x in sorting:
        displayBookInfo(x[0][0],True)
        allBookSpecific.append(x[0])
    return(allBookSpecific)


# list all of the books that are overdue
def bookOverdue():
    overDueBooks = []
    allID = []
    currentDate = datetime.today().strftime('%Y-%m-%d')
    newDate =datetime.strptime((currentDate), '%Y-%m-%d')
    
    Books= allBooksStripped()
    for book in Books:
        bookStatus = checkAvaiable(book[0])
        if(bookStatus[0] == False):
            overDueDate = datetime.strptime(bookStatus[4], '%m-%d-%y')
            
            if(overDueDate<newDate):
                
                overDueBooks.append(book)
                allID.append(book[0])
    return overDueBooks,allID


# Shows all the books borrowed by given member ID
def bookBorrowedBy(memberID):
    bookOwned = []
    allBooks = allBooksStripped()
    for book in allBooks:
        bookStatus = checkAvaiable(book[0])
        if(bookStatus[0]==False):
            if(str(bookStatus[1][1]) == str(memberID)):
                bookOwned.append(book[0])
    return bookOwned


print(bookBorrowedBy(4417))









