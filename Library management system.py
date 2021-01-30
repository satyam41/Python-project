import mysql.connector as sql

conn = sql.connect(host="localhost",user="root",passwd="satyam",database="library")

cur = conn.cursor()

while (True):

    print("======Welcome to KVS library======")

    menu = '''
        Please choose correct option.
            1.Display all book.
            2.Issue book.
            3.Return book.
            4.Exit.
    '''
    print(menu)

    choice = int(input("Please choose your choice (1 to 4): "))

    if choice == 1:
        cur.execute("select * from book")
        data = cur.fetchall()
        for row in data:
            print(row)

    elif choice == 2:
        try:
            bookId = input("Enter book id: ")
            nameOfHolder = input("Enter your name: ")
            bookName = input("Enter which book you want to issue: ")
            value = "insert into issuer values ({}, '{}', '{}')".format(bookId, nameOfHolder, bookName)
            cur.execute(value)
            conn.commit()
            cur.execute("delete from book where book_name = '{}'".format(bookName))
            conn.commit()
            print(f"{bookName} is issued in your name {nameOfHolder}.")
        except:
            print(f"Sorry this book is not avaliable in our library now. {bookName} is issued to some one.")

    elif choice == 3:
        try:
            book_id = input("Enter book id: ")
            book_name = input("Enter book name: ")
            author_name = input("Enter author name: ")
            pub = input("Enter publishers: ")
            price = input("Enter price of the book: ")
            type_ = input("Enter type of the book: ")
            bookValue = "insert into book values ({},'{}','{}','{}',{},'{}')".format(book_id,book_name,author_name,pub,price,type_)
            cur.execute(bookValue)
            conn.commit()
            nameOfReturner = input("Enter your name: ")
            returner = "insert into returner values ({},'{}','{}')".format(book_id,nameOfReturner,book_name)
            cur.execute(returner)
            conn.commit()
            print(f"You have return {book_name}. Thank You for returning this book. I hope you enjoyed so much.")
        except:
            print("Please check your entry.")
        
    elif choice == 4:
        print("Thank you for Visit KVS library.")
        break
    cont = input("Do you wnat to continue with this app? If yes type 'Y' else type 'N' : ")
    if (cont == 'Y' or cont == 'y'):
        continue
    else:
        print("Thank You for using this app.")
        break