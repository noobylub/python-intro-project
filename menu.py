# Code written by F226093
import tkinter as tk
from tkinter import font
from bookSearch import *
from bookCheckout import *
from datetime import date,datetime
from database import allBooks
from bookSelect import plotMatPlot
from bookCreates import addBook

# When user clicks on plot liked, actually runs the functions 
def plotMostLiked():
    typeToLook = likedDisplay.get()
    plotMatPlot(typeToLook)

# The book search, depending on the type, and shows in order to amount checked out
def generalBookSearch():
    print("\n")
    print("Type: " + str(searching.get()))
    print("Book Search for "+str(searchInput.get("1.0", "end-1c")))
    print("---"*30)
    bookSearchResult = searchBook(
        str(searching.get()),
        str(searchInput.get("1.0", "end-1c"))
    )

    print("End of searches ")
    print("-"*100)

# Shows what books a member has 
def memberBooks():
    print("\n")
    print("All books owned by "+ memberIdCheck.get())
    allBooks = bookBorrowedBy(memberIdCheck.get())
    for book in allBooks:
        displayBookInfo(book, True)


# For validation, to make sure that member id does not exceed 4 length and are only numbers
def validate(P):
    if P.isdigit() and len(P) <= 4:
        return True
    return False
# Validating for adding book, the price section
def validatePrice(P):
    if P.isdigit():
        return True
    return False

# Error handling, if program throws error
def errorHandle():
    print("Something went wrong ")
    print("Please make sure to put a four digit number for Member ID")
    print("Please make sure you actually inputted a valid number")

# Adding a new book
def addingBook():
    success_add = addBook(
        
        str(genre_add.get("1.0", "end-1c")),
        str(author_add.get("1.0", "end-1c")),
        str(title_add.get("1.0", "end-1c")),
        priceText.get(),
        True
    )
    if(success_add == True):
        print("Books succesfully added")
    else:
        print("Book unable to add")

# Shows the books that are overdue
def overDueBooks():
    print("\n")
    allBooks = bookOverdue()
    print("All books")
    for x in allBooks[1]:
        displayBookInfo(x,True)

# method for checking out a book
def checkOut():
    try:
        print("\n")
        bookID = int(searchingID.get("1.0", "end-1c"))
        bookCheckOut = checkoutBook(
            bookID,
            # int(checkOutSearchMember.get("1.0", "end-1c")),
            bookText.get(),
            date.today()
        )
        bookCount = len(allBooks())
        if (int(bookID) > bookCount):
            print("Book does not exists")
            searchingID.delete("1.0", "end-1c")
        elif (len(bookText.get()) != 4):
            print("Must be 4 number Digits")
        elif (bookCheckOut == False):
            displayBookStatus(bookID)
        else:
            print("Succesfully Checked-Out book with details")
            displayBookInfo(bookID, False)
    except Exception as E:
        print(E)
        searchingID.delete("1.0", "end-1c")
        bookText.set("")
        errorHandle()

# Methods for checking in a book
def checkIn():
    try:
        print("\n")
        bookID = int(searchingID.get("1.0", "end-1c"))
        bookCount = len(allBooks())
        if (int(bookID) > bookCount):
            print("Book does not exists")
            searchingID.delete("1.0", "end-1c")
            return
        bookCheckIn = checkinBook(
            bookID,
            int(bookText.get()),
            date.today()
        )

        if (len(bookText.get()) != 4):
            print("Must be 4 number Digits")
        elif (bookCheckIn == False):
            displayBookStatus(bookID)
        else:
            print("Succesfull Checked in book with details")
            displayBookInfo(bookID, False)
    except Exception as e:
        # print(e)
        searchingID.delete("1.0", "end-1c")
        bookText.set("")
        errorHandle()

# Method for reserving a book
def reservingBook():
    try:
        print("\n")
        bookID = int(searchingID.get("1.0", "end-1c"))
        reservingBook = reserveBook(
            bookID,
            int(bookText.get()),
            date.today()
        )
        bookCount = len(allBooks())
        if (int(bookID) > bookCount):
            print("Book does not exists")
            searchingID.delete("1.0", "end-1c")

        elif (len(bookText.get()) != 4):
            print("Must be 4 number Digits")
        elif (reservingBook == False):
            displayBookStatus(bookID)
        else:
            print("Succesfully reserved book with details")
            print("Date: " + str(date.today()))
            displayBookInfo(bookID, False)
    except Exception:
        searchingID.delete("1.0", "end-1c")
        bookText.set("")
        errorHandle()

# Start of the menu
# In the menu, F226093 packed everything together so that it is easier to read
bg_color = "#00bfff"

root = tk.Tk()

# displaying the searching function
frameSearch = tk.Frame(root, pady=5, padx=20)
frameSearch.grid(row=0, column=0, columnspan=3)

labelSearch = tk.Label(
    frameSearch, text="Search for a book ordered by how many times checked out")
labelSearch.grid(row=0, column=0, columnspan=3)

searching = tk.StringVar()
searching.set('genre')
genre_RB = tk.Radiobutton(frameSearch, text="Genre", padx=10, pady=10,
                          variable=searching, value="genre")
genre_RB.grid(row=1, column=0)

author_RB = tk.Radiobutton(frameSearch, text="Author", padx=10, pady=10,
                           variable=searching, value="author")
author_RB.grid(row=1, column=1)

title_RB = tk.Radiobutton(frameSearch, text="Title", padx=10, pady=10,
                          variable=searching, value="title")
title_RB.grid(row=1, column=2)

button = tk.Button(frameSearch, text="Search", bg=bg_color,
                   relief="raised", bd=5)
button.configure(command=generalBookSearch)
button.grid(row=2, column=2)

searchInput = tk.Text(frameSearch, height=1, width=20, padx=5, pady=5)
searchInput.grid(row=2, column=0, columnspan=2)


frameBook = tk.Frame(root, padx=20, pady=5).grid(row=3, column=0, columnspan=3)

# Functions to Check in, Reserve and Checkout a book
labelCheckIn = tk.Label(frameBook, text="Check-In Book", bg='blue',
                        width=31).grid(row=3, column=0, columnspan=3, pady=(10, 5))
labelBookId = tk.Label(frameBook, text="Book ID").grid(row=4, column=0)

# Text 
searchingID = tk.Text(frameBook, height=1, width=18, padx=5,
                          pady=5)
searchingID           .grid(row=4, column=1, columnspan=2)
labelMember = tk.Label(frameBook, text="Member ID").grid(row=5, column=0)

# Text
bookText= tk.StringVar()
checkInSearchMember = tk.Entry(frameBook,  width=15, textvariable=bookText,
                               validate="key",
                               validatecommand=(root.register(validate), "%P")
                               )
checkInSearchMember.grid(row=5, column=1, columnspan=2)

# Buttons for the three functions 
checkInButton = tk.Button(frameBook, text="Check-In Book", bg=bg_color,
                          relief="raised", bd=5, command=checkIn).grid(row=6, column=0, columnspan=1)

checkInButton = tk.Button(frameBook, text="Check-Out Book", bg=bg_color,
                          relief="raised", bd=5, command=checkOut).grid(row=6, column=1, columnspan=1)
                          
checkInButton = tk.Button(frameBook, text="Reserve Book", bg=bg_color,
                          relief="raised", bd=5, command=reservingBook).grid(row=6, column=2, columnspan=1)





# Showing matplotlib for different types of favorite to suggest what to order
framePlot = tk.Frame(root, pady=5, padx=20)
framePlot.grid(row=7, column=0, columnspan=3)
labelSearch = tk.Label(
    framePlot, text="Look for most checked out Book Type")
labelSearch.grid(row=7, column=0, columnspan=3, pady=(20, 5))

likedDisplay = tk.StringVar()
likedDisplay.set('genre')
genre_RB = tk.Radiobutton(framePlot, text="Genre", padx=10, pady=10,
                          variable=likedDisplay, value="genre")
genre_RB.grid(row=8, column=0)

author_RB = tk.Radiobutton(framePlot, text="Author", padx=10, pady=10,
                           variable=likedDisplay, value="author")
author_RB.grid(row=8, column=1)

title_RB = tk.Radiobutton(framePlot, text="Title", padx=10, pady=10,
                          variable=likedDisplay, value="title")
title_RB.grid(row=8, column=2)

matPlotButt = tk.Button(framePlot, text="Show Result", relief="raised",
                        command=plotMostLiked).grid(row=9, column=0, columnspan=3)


# Function to add a book
add_Frame = tk.Frame(root, padx=5, pady=5)
add_Frame.grid(row=9, column=0,columnspan=3)
labelSearch = tk.Label(
    add_Frame, text="Add a new Book")
labelSearch.grid(row=9, column=0, columnspan=3, pady=(15, 5))

author_add = tk.Label(add_Frame, text="Author").grid(row=9, column=0)
author_add = tk.Text(add_Frame, height=1, width=18, padx=5,
                    pady=5)
author_add.grid(row=9, column=2, columnspan=2)

genre_add = tk.Label(add_Frame, text="Genre").grid(row=10, column=0)
genre_add = tk.Text(add_Frame, height=1, width=18, padx=5,
                    pady=5)
genre_add.grid(row=10, column=2, columnspan=2)

title_add = tk.Label(add_Frame, text="Title").grid(row=11, column=0)
title_add = tk.Text(add_Frame, height=1, width=18, padx=5,
                    pady=5)
title_add.grid(row=11, column=2, columnspan=2)

price_add = tk.Label(add_Frame, text="Price").grid(row=12, column=0)
priceText = tk.StringVar()
price_add  = tk.Entry(add_Frame,  width=15, textvariable=priceText, validate="key",
                                validatecommand=(root.register(validatePrice), "%P")
                                )
price_add .grid(row=12, column=2, columnspan=2)

matPlotButt = tk.Button(add_Frame, text="Add book", relief="raised",
                        command=addingBook).grid(row=13, column=0, columnspan=3)


# Function to display the overdue books 
overDueBooks = tk.Button(root, text="Show OverDue Books", relief="raised",
                        command=overDueBooks, padx=10,pady=10).grid(row=16, column=0, columnspan=3, padx=10,pady=(10))

# # Function to display what book a member has 
labelMember = tk.Label(frameBook, text="MemberID").grid(row=14, column=0, pady=(20,5))

memberIdCheck = tk.StringVar()
reserveMember = tk.Entry(frameBook,  width=15, textvariable=memberIdCheck, validate="key",
                         validatecommand=(root.register(validate), "%P")
                         )
reserveMember.grid(row=14, column=1, columnspan=2,pady=(20,5))

overDueBooks = tk.Button(root, text="Member ID book Check", relief="raised",
                        command=memberBooks, padx=5,pady=5).grid(row=15, column=0, columnspan=3, padx=2,pady=2)
# Run the Tkinter event loop
root.mainloop()
