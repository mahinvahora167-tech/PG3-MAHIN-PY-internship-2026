library={101:{"title":"phython basics","author":"john","copies":5},
         102:{"title":"data science","author":"alice","copies":3},
         103:{"title":"ai guide","author":"bob","copies":4}
} 

book_id=102

if book_id in library and library[book_id]["copies"]>0:
    library[book_id]["copies"]-=1

    print(library)