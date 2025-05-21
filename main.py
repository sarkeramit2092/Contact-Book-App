book_list ={}

while True:
    print("\nWelcome to Book App")
    print("1. Create Book Entry")
    print("2. View Book List")
    print("3. Update Book Entry")
    print("4. Delete Book Entry")
    print("5. Search Book Details")
    print("6. Count Books")
    print("7. Exit App")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Book Name: ")
        if name in book_list:
            print(f"Book Name {name} already exists!!")
        else:
            author = input("Enter Author Name: ")
            price = input("Enter Price: ")
            review = input("Enter your short Review: ")
            book_list[name] = {"author":author, "price":int(price), "review":review}
            print(f"Book Name: {name} has been created successfully!!")

    elif choice == "2":
        name = input("Enter Book Name: ")
        if name in book_list:
            book_list = book_list[name]
            print (f"Book Name: {name}, author:{author}, price:{int(price)}, review:{review}")
        else:
            print("Book not Found!!")
    
    elif choice == "3":
        name = input("Enter Book Name to Update: ")
        if name in book_list:
            author = input("Enter Update Author Name: ")
            price = input("Enter Update Price: ")
            review = input("Enter your Updated short Review: ")
            book_list[name] = {"author":author, "price":int(price), "review":review}
            print(f"Book Name: {name} has been Updated successfully!!")
        else:
            print("Book not Found!!")