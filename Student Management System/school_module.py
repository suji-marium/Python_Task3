class Student:
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.grade_list=[]
    
    def add_grades(self, grades):
        new_grades = list(map(int, grades.split()))
        for grade in new_grades:
            if grade < 0 or grade > 100:
                raise ValueError(f"Invalid Grade: {grade}")
        self.grade_list.extend(new_grades)
        
    
    def avg_grade(self):
        if not self.grade_list:
            return 0
        sum=0
        for grade in self.grade_list:
            sum+=grade
        return sum/len(self.grade_list)

    def display_student_details(self):
        return f"Id: {self.student_id}, Name: {self.name}, Average Grade: {Student.avg_grade(self)}"


class School:
    def __init__(self) :
        self.students={}

    def add_student(self,student):
        if student.student_id in self.students:
            raise ValueError(f"Student with id {student.student_id} already exist")
        self.students[student.student_id]=student
    
    def remove_student(self,student_id):
        if student_id not in self.students:
            raise ValueError("Student Id doesn't exist")
        del self.students[student_id]

    def search_student(self,student_id):
        if student_id not in self.students:
            raise ValueError("Student Id doesn't exist")

        for student in self.students.values():
            if student.student_id==student_id:
                return student.display_student_details()
    
    def list_students(self):
        print("\nStudent List")
        for student in self.students.values():
            yield student.display_student_details()

class AdvancedSchool(School):
    def __init__(self):
        super().__init__()
        self.grade_above_students=list()

    def grade_above(self,threshold_grade):
        for student in self.students.values():
            if student.avg_grade()>threshold_grade:
                self.grade_above_students.append(student)
        if not self.grade_above_students:
            return "No student is available"
        return self.grade_above_students

"""
s1=Student(1,"Suji")

s2=Student(2,"Sumi")
s3=Student(3,"Raju")
s4=Student(4,"Rani")


advanced_school=AdvancedSchool()

advanced_school.add_student(s1)
advanced_school.add_student(s2)
advanced_school.add_student(s3)
advanced_school.add_student(s4)

s1.add_grades([84,80,90])
s2.add_grades([90,85,98])
s3.add_grades([90,87])
s4.add_grades([47,58])



for student in advanced_school.list_students():
    print(student)

advanced_school.grade_above(85)

"""