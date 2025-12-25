# GPA Planner (Python)

A terminal-based GPA calculator written in Python that allows students to track courses, calculate a weighted GPA, and save academic data for future use. This project focuses on core programming fundamentals such as data structures, file handling, and user input.

## Features
- Add courses with name, credits, and letter grade
- Calculate weighted GPA using course credits
- View all entered courses in a clean list format
- Save course data to a JSON file
- Load previously saved course data
- Simple menu-driven terminal interface

## Setup
1. Clone or download this repository
2. Ensure the project directory contains:
   - `gpa.py`
   - `data.json`

3. Run the program:
   python gpa.py

## How to Use
When the program starts, you will see a menu:

1 Add  
2 List  
3 GPA  
4 Save  
5 Load  
6 Quit  

- Add: Enter a course name, number of credits, and letter grade
- List: View all added courses
- GPA: Calculate and display your current weighted GPA
- Save: Save course data to data.json
- Load: Load saved course data from data.json
- Quit: Exit the program

## GPA Calculation
The GPA is calculated using a standard 4.0 scale and weighted by course credits:

GPA = (sum of (grade points × credits)) / (sum of credits)

## Technologies Used
- Python
- JSON (data persistence)
- File I/O
- Dictionaries and lists

## Purpose
This project was built to reinforce Python fundamentals such as loops, conditionals, functions, data modeling, and persistent storage, while solving a real-world academic planning problem.

## Future Improvements
- Edit or remove courses
- Support multiple semesters
- What-if GPA planning
- Improved input validation
