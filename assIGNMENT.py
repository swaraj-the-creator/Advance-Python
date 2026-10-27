i = 0
while i <= 10:
    books = ["Dragonball Z", "Harry Potter", "Dragonball Super", "The Jungle Book", "Batman"]
    copy_counts = [26, 6, 27, 0, 5]
    late_fees2 = ["₹500", "₹410", "₹510", "₹300", "₹150"]
    library = {book: count for book, count in zip(books, copy_counts)}
    library_prices = {book: count for book, count in zip(books, late_fees2)}
    print("\nFull Library Stock : ", library)
    print("Price Of Each Book : ",library_prices,"\n")
    available_books = [book for book in books if library[book] > 0]
    print("Books Available:", available_books)
    chosen_book = input("Which book do you want to borrow? ")
    if chosen_book not in library or library[chosen_book] == 0:
        print(chosen_book, "is not in stock available! Stopping the checker.")
        exit()
    late_fees = [500, 410, 510, 300, 150]
    extra_fee = int(input("Enter the extra library fee to add to every book: "))
    updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
    print("Updated Fees:", updated_fees)
    book_index = books.index(chosen_book)
    chosen_fee = updated_fees[book_index]
    print("Extra amount for", chosen_book, "after update:", chosen_fee)
    library[chosen_book] = library[chosen_book] - 1
    print(chosen_book, "borrowed! Remaining copies:", library[chosen_book])
    print("\n===== LIBRARY BOOK AVAILABILITY CHECKER =====")
    print("Book Borrowed:", chosen_book)
    print("Outdated prices:", late_fees2)
    print("Updated prices (price which will you pay) :", chosen_fee)
    print("Updated Library Stock:", library)
    print("=============================================")
    print(f"Adding more books for {chosen_book}")
    cust = input("Any more customer (yes/no): ")
    if cust != "yes" or cust != "Yes" or cust != "yEs" or cust != "yeS" or cust != "YEs" or cust != "YeS" or cust != "yES" or cust != "YES":
        continue
    else:
        break
