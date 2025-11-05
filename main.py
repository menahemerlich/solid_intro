from classes.exercise_s1.book import Book
from classes.exercise_s1.save_to_file import Save_to_file
from classes.exercise_s2.student import Student
from classes.exercise_s2.grade_calculator import GradeCalculator
from classes.exercise_s3.order import Order
from classes.exercise_s3.invoice_printer import InvoicePrinter
from classes.exercise_o1.square import Square
from classes.exercise_o1.circle import Circle
from classes.exercise_o1.rectangle import Rectangle
from classes.exercise_o2.credit_card import CreditCardPayment
from classes.exercise_o2.pay_pal import PayPalPayment
from classes.exercise_o2.crypto import CryptoPayment
from classes.exercies_o3.email_notifier import EmailNotifier
from classes.exercies_o3.sms_notifier import SMSNotifier
from classes.exercies_o3.push_notifier import PushNotifier
from classes.liskov.drone import Drone
from classes.liskov.tank import Tank

book1 = Book("book", "r.lev", "story")
Save_to_file.Save_to_file("test", book1)
student1 = Student("Avi", [75, 100, 68, 90])
GradeCalculator.average_grade(student1)
order1 = Order(["appel", "banana"], 12.5)
InvoicePrinter.print_invoice(order1)
print(Square().area(5))
print(Circle().area(5))
print(Rectangle().area(2, 4))
pay1 = CreditCardPayment()
pay2 = PayPalPayment()
pay3 = CryptoPayment()
pay1.pay(10)
pay2.pay(15)
pay3.pay(20)
not1 = EmailNotifier()
not2 = SMSNotifier()
not3 = PushNotifier()
not1.send("email")
not2.send("sms")
not3.send("push")
drone = Drone("drone")
tank = Tank("tank")
drone.fly()
tank.fly()


