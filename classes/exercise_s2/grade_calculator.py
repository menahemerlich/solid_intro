
class GradeCalculator:
    @staticmethod
    def average_grade(student):
        average = 0
        for i in student.grades:
            average += i
        average = average / len(student.grades)
        print(average)







