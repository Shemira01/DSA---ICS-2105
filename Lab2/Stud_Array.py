class Grade:
    def __init__(self, marks=0):
        self.marks = marks
        self.grade = self.calculate_grade()
    
    def calculate_grade(self):
        if self.marks >= 70: return 'A'
        elif self.marks >= 60: return 'B'
        elif self.marks >= 50: return 'C'
        elif self.marks >= 40: return 'D'
        else: return 'F'

class Course:
    def __init__(self, code="", name=""):
        self.code = code
        self.name = name

class Student:
    def __init__(self, regNo="", name="", age=0, course=None, marks=0):
        self.regNo = regNo
        self.name = name
        self.age = age
        self.course = course if course else Course()
        self.grade = Grade(marks)
    
    def update_marks(self, new_marks):
        self.grade = Grade(new_marks)
    
    def __str__(self):
        return (f"RegNo: {self.regNo:<8} Name: {self.name:<15} Age: {self.age:<3} "
                f"Course: {self.course.code:<7} Marks: {self.grade.marks:<3} "
                f"Grade: {self.grade.grade}")

class StudentListArray:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def edit_student_marks(self, regNo, new_marks):
        for student in self.students:
            if student.regNo == regNo:
                student.update_marks(new_marks)
                return True
        return False
    
    def calculate_all_grades(self):
        for student in self.students:
            student.grade.grade = student.grade.calculate_grade()
    
    def display_all(self):
        print("\n" + "="*80)
        print(f"{'ARRAY-BASED STUDENT LIST':^80}")
        print("="*80)
        for student in self.students:
            print(student)
        print("="*80 + "\n")

def initialize_students():
    math = Course("MATH101", "Mathematics")
    cs = Course("CS101", "Computer Science")
    physics = Course("PHY101", "Physics")
    
    student_list = StudentListArray()
    
    for i in range(1, 16):
        regNo = f"STD{i:03d}"
        name = f"Student_{i}"
        age = 17 + (i % 4)
        course = [math, cs, physics][i % 3]
        marks = 35 + (i * 3)
        student_list.add_student(Student(regNo, name, age, course, marks))
    
    return student_list

def array_based_interface():
    student_list = initialize_students()
    
    while True:
        print("\nARRAY-BASED STUDENT MANAGEMENT")
        print("1. View all students")
        print("2. Edit student marks")
        print("3. Recalculate all grades")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            student_list.display_all()
        
        elif choice == "2":
            regNo = input("Enter student registration number (e.g., STD001): ")
            try:
                new_marks = int(input("Enter new marks (0-100): "))
                if 0 <= new_marks <= 100:
                    if student_list.edit_student_marks(regNo, new_marks):
                        print(f"Marks for {regNo} updated successfully!")
                    else:
                        print("Student not found!")
                else:
                    print("Marks must be between 0-100!")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == "3":
            student_list.calculate_all_grades()
            print("All grades recalculated based on current marks!")
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    array_based_interface()