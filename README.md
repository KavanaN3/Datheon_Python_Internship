This project is a rule-based interactive chatbot developed using Python. It communicates with users through the terminal and provides predefined responses based on keywords and regular expressions.

The chatbot can answer questions about courses, fees, placements, office hours, greetings, and other basic queries.
Prerequisites:
- Python 3 installed
- Visual Studio Code installed
Steps:
1. Download or clone the project.
2. Extract the project folder if downloaded as a ZIP file.
3. Open the folder in Visual Studio Code.
4. Open the VS Code terminal.
5. Check Python installation:
```
python --version
```
No external Python packages are required because the project uses Python's built-in re module.
- Python 3
- Regular Expressions (re module)
- Visual Studio Code
- Command-line terminal
Task 4 – Rule-Based Interactive Terminal Assistant
1. Open the task4_chatbot folder in VS Code.
2. Open the terminal.
3. Execute:
```
python chatbot.py
```
4. Ask questions such as:
   - Hello
   - What courses do you offer?
   - What are the fees?
   - Tell me about placements.
   - What are your working hours?
5. Type exit to close the chatbot.
```
task4_chatbot/
│
├── chatbot.py
├── README.md
```
Program workflow:
1. User enters a message.
2. The chatbot converts the message to lowercase.
3. Regular expressions identify the user's intent.
4. The matching predefined response is displayed.
5. The chatbot continues until the user types exit.
