from person import Person
from course import Course

class Student(Person):
    def __init__(self, first_name, last_name, major, courses=None):
        super().__init__(first_name, last_name)
        self.major = major
        self.courses = courses or []

    def add_course(self, course):
        self.courses.append(course)

    def change_major(self, new_major):
        self.major = new_major

    def get_credits(self):
        return sum([course.credits for course in self.courses])

    def get_gpa(self):
        total_grade_points = sum([grade_map[course.grade] * course.credits for course in self.courses])
        return total_grade_points / self.get_credits() if self.get_credits() > 0 else 0.0

grade_map = {
    "A"  : 4.0,
    "A-" : 3.7,
    "B+" : 3.3,
    "B"  : 3.0,
    "B-" : 2.7,
    "C+" : 2.3,
    "C"  : 2.0,
    "C-" : 1.7,
    "D+" : 1.3,
    "D"  : 1.0,
    "F"  : 0.0
}
