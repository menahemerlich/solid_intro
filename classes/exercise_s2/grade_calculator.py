
class GradeCalculator:
    def __init__(self, student):
        average = 0
        for i in student.grades:
            average += i
        average = average / len(student.grades)
        print(average)







