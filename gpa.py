import json
import os

GRADE = {
    "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0,
    "F": 0.0
}

FILE = "data.json"

def load_courses():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_courses(courses):
    with open(FILE, "w") as f:
        json.dump(courses, f, indent=2)

def add_course(courses):
    name = input("What is the name of the course: ").strip()
    credits = float(input("How many credits is the course: ").strip())
    grade = input("What grade did u get in the course: ").strip().upper()

    if grade not in GRADE:
        print("Invalid grade")
        return

    courses.append({"name": name, "credits": credits, "grade": grade})
    print("Added.")

def list_courses(courses):
    if not courses:
        print("No courses")
        return
    for i, c in enumerate(courses, 1):
        print(f"{i}. {c['name']} | {c['credits']} credits | {c['grade']}")

def calc_gpa(courses):
    total_points = 0
    total_credits = 0

    for c in courses:
        total_points += GRADE[c["grade"]] * c["credits"]
        total_credits += c["credits"]

    if total_credits == 0:
        return 0
    return total_points / total_credits

def main():
    courses = load_courses()

    while True:
        print("\n1 Add  2 List  3 GPA  4 Save  5 Load  6 Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_course(courses)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            print(f"GPA: {calc_gpa(courses):.2f}")
        elif choice == "4":
            save_courses(courses)
            print("Saved.")
        elif choice == "5":
            courses = load_courses()
            print("Loaded.")
        elif choice == "6":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
