# Task 4: Rule-Based Interactive Terminal Assistant

## 1. Project Description
This project is a simple rule-based interactive chatbot developed using Python. It allows users to interact with a terminal assistant by asking questions about courses, fees, placements, and working hours.

The chatbot identifies user questions using keyword matching and provides predefined responses.

## 2. Features
- Responds to greetings.
- Provides information about courses.
- Answers questions about fees.
- Provides placement information.
- Shares working hours.
- Handles unknown questions with a default response.
- Allows users to exit the chatbot.

## 3. Technologies Used
- Python 3
- Regular Expressions (`re` module)

## 4. Installation Instructions
1. Install Python 3.
2. Download or clone this project.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.

## 5. How to Run
Execute the following command:

```bash
python chatbot.py
```

Start asking questions in the terminal. Type `exit` to stop the chatbot.

## 6. Project Architecture

```text
task4_chatbot/
│
├── chatbot.py
├── README.md
└── task4_output
```

## 7. How It Works
1. The chatbot starts and displays a welcome message.
2. The user enters a question.
3. The program checks the input against predefined keywords and patterns.
4. The chatbot displays the matching response.
5. The process continues until the user types `exit`.

## 8. Output 
The `task4_output` file shows the chatbot running successfully in the terminal.

## 9. Conclusion
This project demonstrates basic Python programming, string handling, regular expressions, conditional logic, and interactive terminal applications.

Developed as part of the Datheon Python Programming Internship.
