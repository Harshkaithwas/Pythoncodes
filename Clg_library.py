class Liberary:
      def __init__(self, listofBooks):
            self.books = listofBooks
                
      def displayAvailableBooks(self):
            print("Books present in this liberary are : ")
            for book in self.books:
                  print("\t -> " + book)

      def borrowBook(self, bookName):
            if bookName in self.books:
                  print(f"This book {bookName} is been issued on your name. please keep it save and return with in 30 days ")
                  self.books.remove(bookName)
                  return True
            else:
                  print(f"Sorry this book {bookName} is already been issued to someone . Please wait for availability")
                  return False

      def returnBook(self, bookName):
            self.books.append(bookName)
            print("Thanks for returning the book")


class Student:
      def requestBook(self):
            self.book = input("Enter the name you want to request")
            return self.book

      def returnBook(self):
            self.book = input("Enter the name you want to return")
            return self.book



if __name__ == "__main__":
      collegeLiberary = Liberary(["algorithms", "Django", "Machine Learning", "python", "C-programming"])
      Student = Student()
      # collegeLiberary.displayAvailableBooks()
      while(True):
            Welcome_MSG = '''
             ===========Welcome_To_Liberary===========
                        Please choose an option:
                        1. List of all the books
                        2. Request a book
                        3. Return a book
                        4. Exit the liberary
            '''
            print(Welcome_MSG)

            a = int(input("Enter a choice : "))
            if a ==1 :
                  collegeLiberary.displayAvailableBooks()
            elif a==2 :
                  collegeLiberary.borrowBook(Student.requestBook())
            elif a ==3 :
                  collegeLiberary.returnBook(Student.returnBook())
            elif a== 4:
                  print("Thanks for Visisting Us")
                  exit()
            else:
                  print("Invalid input")

