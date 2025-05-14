#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Grade structure
typedef struct {
    int marks;
    char grade;
} Grade;

// Course structure
typedef struct {
    char code[10];  // Maximum length for course code
    char name[50];  // Maximum length for course name
} Course;

// Student structure
typedef struct {
    char regNo[10];  // Format: STD001 to STD999
    char name[50];   // Maximum length for student name
    int age;
    Course course;
    Grade grade;
} Student;

// Node structure for linked list
typedef struct Node {
    Student student;
    struct Node* next;
} Node;

// Function prototypes
void calculate_grade(Grade* grade);
void initialize_students(Node** head);
void display_students(Node* head);
void edit_student_marks(Node* head);
void recalculate_all_grades(Node* head);
void free_list(Node* head);

int main() {
    Node* head = NULL;
    int choice;

    // Initialize with 15 students
    initialize_students(&head);

    while (1) {
        printf("\nSTUDENT MANAGEMENT SYSTEM\n");
        printf("1. Display all students\n");
        printf("2. Edit student marks\n");
        printf("3. Recalculate all grades\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                display_students(head);
                break;
            case 2:
                edit_student_marks(head);
                break;
            case 3:
                recalculate_all_grades(head);
                printf("All grades recalculated successfully!\n");
                break;
            case 4:
                free_list(head);
                printf("Exiting program...\n");
                return 0;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
}

void calculate_grade(Grade* grade) {
    if (grade->marks >= 70) grade->grade = 'A';
    else if (grade->marks >= 60) grade->grade = 'B';
    else if (grade->marks >= 50) grade->grade = 'C';
    else if (grade->marks >= 40) grade->grade = 'D';
    else grade->grade = 'F';
}

void initialize_students(Node** head) {
    Course courses[3] = {
        {"MATH101", "Mathematics"},
        {"CS101", "Computer Science"},
        {"PHY101", "Physics"}
    };

    Node* current = NULL;

    for (int i = 0; i < 15; i++) {  // Create exactly 15 students
        Node* newNode = (Node*)malloc(sizeof(Node));

        // Generate student data
        snprintf(newNode->student.regNo, 10, "STD%03d", i+1);
        snprintf(newNode->student.name, 50, "Student_%d", i+1);
        newNode->student.age = 17 + (i % 4);  // Ages between 17-20
        newNode->student.course = courses[i % 3];
        newNode->student.grade.marks = 35 + (i * 3);  // Marks range from 38-80
        calculate_grade(&newNode->student.grade);
        newNode->next = NULL;

        if (*head == NULL) {
            *head = newNode;
            current = newNode;
        } else {
            current->next = newNode;
            current = current->next;
        }
    }
}

void display_students(Node* head) {
    printf("\n%-10s %-15s %-5s %-10s %-10s %-5s\n",
           "RegNo", "Name", "Age", "Course", "Marks", "Grade");
    printf("-------------------------------------------------\n");

    Node* current = head;
    while (current != NULL) {
        printf("%-10s %-15s %-5d %-10s %-10d %-5c\n",
               current->student.regNo,
               current->student.name,
               current->student.age,
               current->student.course.code,
               current->student.grade.marks,
               current->student.grade.grade);
        current = current->next;
    }
}

void edit_student_marks(Node* head) {
    char regNo[10];  // Buffer for registration number
    int newMarks;

    printf("Enter student registration number: ");
    scanf("%9s", regNo);  // Read up to 9 characters to prevent buffer overflow

    Node* current = head;
    while (current != NULL) {
        if (strcmp(current->student.regNo, regNo) == 0) {
            printf("Current marks: %d\n", current->student.grade.marks);
            printf("Enter new marks (0-100): ");
            scanf("%d", &newMarks);

            if (newMarks < 0 || newMarks > 100) {
                printf("Invalid marks! Must be between 0-100.\n");
                return;
            }

            current->student.grade.marks = newMarks;
            calculate_grade(&current->student.grade);
            printf("Marks updated successfully!\n");
            return;
        }
        current = current->next;
    }

    printf("Student with RegNo %s not found!\n", regNo);
}

void recalculate_all_grades(Node* head) {
    Node* current = head;
    while (current != NULL) {
        calculate_grade(&current->student.grade);
        current = current->next;
    }
}

void free_list(Node* head) {
    Node* current = head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
}
