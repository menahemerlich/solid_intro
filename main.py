from classes.exercise_s1.book import Book
from classes.exercise_s1.save_to_file import Save_to_file
from classes.exercise_s2.student import Student
from classes.exercise_s2.grade_calculator import GradeCalculator

book1 = Book("book", "r.lev", "story")
Save_to_file("test", book1)
student1 = Student("Avi", [75, 100, 68, 90])
GradeCalculator(student1)




