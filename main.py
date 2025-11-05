from classes.exercise_s1.book import Book
from classes.exercise_s1.save_to_file import Save_to_file
from classes.exercise_s2.student import Student
from classes.exercise_s2.grade_calculator import GradeCalculator
from classes.exercise_s3.order import Order
from classes.exercise_s3.invoice_printer import InvoicePrinter

book1 = Book("book", "r.lev", "story")
Save_to_file.Save_to_file("test", book1)
student1 = Student("Avi", [75, 100, 68, 90])
GradeCalculator.average_grade(student1)
order1 = Order(["appel", "banana"], 12.5)
InvoicePrinter.print_invoice(order1)




