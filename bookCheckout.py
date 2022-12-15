# Code written by F226093
from otherMethods import createRandomTime
from datetime import datetime
from bookSearch import searchID, checkAvaiable

from datetime import date 
import random
from database import bookDataMethods,allBooks


# Shows the status of all books
# Listing the books four possible scenarios mentioned in book search
def statusOfBooks():
    data = allBooks()
    totalBooks = len(data)
    checkedOutBooks = []
    checkedInBooks = []
    fullyReserved = []
    bookReserved = []
    for x in range(totalBooks):
        currentBook = x+1
        avaiable = checkAvaiable(currentBook)
        if (avaiable[0] == True and avaiable[2] == False):
            checkedInBooks.append(currentBook)
        elif (avaiable[0] == True and avaiable[2] == True):
            checkedInBooks.append(currentBook)
            bookReserved.append(currentBook)
        elif (avaiable[0] == False and avaiable[2] == True):
            fullyReserved.append(currentBook)
        elif (avaiable[0] == False and avaiable[2] == False):
            checkedOutBooks.append(currentBook)

    return checkedInBooks, checkedOutBooks, fullyReserved, bookReserved

print(statusOfBooks())

# Showing error message
def messageNotNumbers():
    print("\n")
    print("-"*30)
    print("Please input four digit numbers please ")



# Checking out a book with some validity checks
def checkoutBook(bookID, memberID, dateIn = False):
    bookInfo = searchID(bookID)
    # Checking avaibality from method shown in BookSearch
    avaiable = checkAvaiable(bookID)
    if (bookInfo == False):
        return (False)

    # Below is to generate random date for random data for testing purposes
    if(dateIn == False):
        start = datetime.strptime(str(bookInfo[5]), '%m-%d-%y')
        d2 = datetime.strptime('1/1/2026 ', '%m/%d/%Y ')
        d1 = start
        dateIn = createRandomTime(d1, d2).strftime("%m-%d-%y")
    else:
        dateIn = dateIn.strftime("%m-%d-%y")
   
    # Checking if book is avaiable and reserved, in that case, 
    # only the person reserving can checkbook out
    if (avaiable[2] == True and int(memberID) != int(avaiable[3][1])):
        return (False)
    if (avaiable[2] == True and int(memberID) == int(avaiable[3][1])):
        bookDataMethods(bookID, memberID, dateIn, "reserve-check-out")
        return (True)
    
    # If not reserved, check if book is actually avaiable 
    if (avaiable[0] == False):
        return (False)
    
    print(dateIn)
    bookDataMethods(bookID, memberID, dateIn, "check-out")
    return (True)


# Method for checking in books
def checkinBook(bookID, memberID, dateIn = False):
    bookAvaiable = checkAvaiable(bookID)
    bookInfo = searchID(bookID)
    # Check if book is not avaible to check in, if they are, 
    # you should not be able to check in
    if (bookAvaiable[0] == True):
        return (False)
    
    
    
    # Below is to generate random date for random data for testing purposes
    if(dateIn is False):
        start = datetime.strptime(str(bookInfo[5]), '%m-%d-%y')
        d2 = datetime.strptime('1/1/2026 ', '%m/%d/%Y ')
        d1 = start
        dateIn = createRandomTime(d1, d2).strftime("%m-%d-%y")
    dateIn = dateIn.strftime("%m-%d-%y")
    
   
    bookDataMethods(bookID, memberID, dateIn, "check-in")
    
    return (True)


# Method for reserving a book with validity checkes
def reserveBook(bookID, memberID, dateIn = False):
    bookavaiable = checkAvaiable(bookID)
    # If book avaiable, can't reserve, just checkin
    if (bookavaiable[0] == True):
        return False
    # If book is reserved by someone else, cant reserve
    elif (bookavaiable[2] == True):
        return False

    # Below is to generate random date for random data
    if(dateIn == False):
        bookInfo = searchID(bookID)
        
        start = datetime.strptime(str(bookInfo[5]), '%m-%d-%y')
        d2 = datetime.strptime('1/1/2026 ', '%m/%d/%Y ')
        d1 = start
        dateIn = createRandomTime(d1, d2).strftime("%m-%d-%y")
    dateIn = dateIn.strftime("%m-%d-%y")

    bookDataMethods(bookID, memberID, dateIn, "reserve")
    return True



# Creating random data, with amount being hte number of random data there is
def createData(amount):
    lengOfBooks = len(allBooks())
    print("stare")
    allMembers = []
    for (x) in range(20):
        while True:
            ran = random.randint(1000, 5000)
            if (ran not in allMembers):
                allMembers.append(ran)
                break
    # Generate fake data
    f = open('logfile.txt', 'w')
    f.write("")
    ran = 1
    for x in range(amount):
        # If its one checkout a book
        ran = random.randint(1, 3)
        # In the case that no books checeked out and multiple books reserved
        # you have to check out some books
        if (len(statusOfBooks()[1]) == 0 and len(statusOfBooks()[2]) > 0):
            ran = 1

        # In the case that all books are checked in
        elif (len(statusOfBooks()[1]) == 0 and len(statusOfBooks()[2]) == 0):
            ran = 1
    
        print(ran)
        print("Books avaiable")
        print(len(statusOfBooks()[0]))
        print("Books checkedout ")
        print(len(statusOfBooks()[1]))
        print("Books reserved")
        print(len(statusOfBooks()[2]))
        print("Books avaiable to only reserved People")
        print(len(statusOfBooks()[3]))
        
        if (ran == 1):
            while True:
                putThis = checkoutBook(random.randint(
                    1, lengOfBooks), random.choice(allMembers))
                if (putThis == True):
                    break
        # If its two return a book
        elif (ran == 2):
            while True:
                num = random.randint(1, lengOfBooks)

                # check if book is avaiable
                bookavaiable = checkAvaiable(num)

                if (bookavaiable[0] == False):
                    print(num)
                    checkinBook(num, random.choice(allMembers))
                    break
        elif (ran == 3):
            while True:

                putThis = reserveBook(random.randint(
                    1, lengOfBooks), random.choice(allMembers))
                if (putThis == True):
                    break
# createData(100)

