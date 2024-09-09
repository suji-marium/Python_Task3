
from school_module import Student,AdvancedSchool 

def main():
    advanced_school=AdvancedSchool()
    while True:
        print("\nStudent Management System \n1. Add Students \n2. Remove Students \n3. Search Student By id \n4. Display Student List \n5. Display students with an average grade above the given threshold. \n6. Exit")

        ch=input("Enter the choice: ")
        if ch=="1":
            try:
                student_id=int(input("Enter the Student Id: "))
                name=input("Enter the Student Name: ")
                grades_input = input("Enter the grades seperating them with a space: ")
                s=Student(student_id,name)
                advanced_school.add_student(s)
                s.add_grades(grades_input)
                print("Student Added Successfully")

            except ValueError as e:
                print(f"Error: {e}")
                
            except Exception as e:
                print(e)


        elif ch=="2":
            try:
                student_id=int(input("Enter the student id of the student to be deleted: "))
                advanced_school.remove_student(student_id)
                print("Student Deleted Suucessfully")
            
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="3":
            try:
                student_id=int(input("Enter the Student Id of the student to be searched: "))
                print(advanced_school.search_student(student_id))
            
            except ValueError as e:
                print(f"Error: {e}")

        elif ch=="4":
            for student in advanced_school.list_students():
                print(student)
        
        elif ch=="5":
            try:
                threshold_grade=float(input("Enter the threshold grade: "))
                for student in advanced_school.grade_above(threshold_grade):
                        print(student.display_student_details())

            except ValueError as e:
                print(f"Error: {e}")
                
            except Exception as e:
                print(e)
        
        elif ch=="6":
            print("Exiting")
            break


if __name__=="__main__":
    main()