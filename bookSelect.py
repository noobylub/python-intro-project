# Code written by F226093

from bookSearch import checkAvaiable, searchID, showLikedBook
import matplotlib.pyplot as plt
from database import logFileRead, allBooksStripped


# shows the most liked type, genre, author or title
def likedCategory(type):
    topLiked = []
    if (str(type) == "genre"):
        toShow = 1
    elif (str(type) == "author"):
        toShow = 3
    elif (str(type) == "title"):
        toShow = 2
    else:
        return ("Please show a valid type")
    datas = allBooksStripped()
    for entry in datas:
        if (str(entry[toShow]) not in str(topLiked)):
            totalCheckedOut = showLikedBook(entry[0])
            topLiked.append((entry[toShow], totalCheckedOut[1]))
        if (str(entry[toShow] in str(topLiked))):
            indexTochange = 0
            for index, value in enumerate(topLiked):
                if (str(value[0]) == str(entry[toShow])):
                    indexTochange = index
            amountAdd = showLikedBook(entry[0])
            total = int(amountAdd[1]) + int(topLiked[indexTochange][1])
            # print(allGenre[indexTochange][1])
            topLiked[indexTochange] = (entry[toShow], total)
    twoArray = list(map(list, zip(*topLiked)))

    return (twoArray)


# Plots the results in a matplotlib
def plotMatPlot(type):
    fig, ax = plt.subplots()
    allLikedThings = likedCategory(type)
    fruits = allLikedThings[0]
    counts = allLikedThings[1]
    ax.bar(fruits, counts)
    ax.set_ylabel('Amount Checked Out')
    ax.set_title('Most Checked out book')
    ax.legend(title=type)
    plt.show()


# Like most checked out book for the different types, author, title, and genre


# Display what that member has
def searchMember(memberID):
    f = open("Book_Info.txt", "r")
    data = f.readlines()
    totalBooks = len(data)
    bookByMember = []
    for x in range(totalBooks):
        currentBook = x+1
        bookInfo = checkAvaiable(currentBook)
        if (bookInfo[0] == False and str(bookInfo[1][1]) == str(memberID)):
            bookByMember.append(bookInfo[1])
    return bookByMember
