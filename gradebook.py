# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:03:06 2023

@author: araba
"""

def convert_to_letter_grade(numericScore):
    if numericScore >= 94:
        return "A"
    elif numericScore >= 89:
        return "A-"
    elif numericScore >= 85:
        return "B+"
    elif numericScore >= 82:
        return "B"
    elif numericScore >= 79:
        return "B-"
    elif numericScore >= 76:
        return "C+"
    elif numericScore >= 73:
        return "C"
    elif numericScore >= 70:
        return "C-"
    elif numericScore >= 67:
        return "D+"
    elif numericScore >= 64:
        return "D"
    elif numericScore >= 60:
        return "D-"
    else:
        return "E"

def compute_class_average(numStudents, sumOfClassGrades):
    classAverage = sumOfClassGrades / numStudents
    letterGrade = convert_to_letter_grade(classAverage)
    return (classAverage, letterGrade)

def main():
    numStudents = int(input("Enter the number of students in your class: "))
    sumOfClassGrades = 0
    for i in range(numStudents):
        grade = int(input(f"Enter the grade for student {i+1}: "))
        sumOfClassGrades += grade
        letterGrade = convert_to_letter_grade(grade)
        print(f"Student {i+1} received a {letterGrade} ({grade})")
    
    classAverage, classLetterGrade = compute_class_average(numStudents, sumOfClassGrades)
    print(f"\nClass average is {classAverage} ({classLetterGrade})")

if __name__ == "__main__":
    main()
 
