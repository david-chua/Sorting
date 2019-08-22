def insertion_sort(books):
    for i in range(1, len(books)):
        current_book = books[i]
        j = i
        while j > 0 and current_book.genre < books[j-1].genre:
            books[j] = books[j-i]
            j -= 1
    return books
