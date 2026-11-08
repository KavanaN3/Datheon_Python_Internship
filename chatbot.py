
import re

# Chatbot responses
responses = {
    "greeting": "Hello! Welcome to our AI chatbot.",
    "courses": "We offer Python, Java, AI, Machine Learning, and Web Development.",
    "fees": "Our course fees depend on the selected course. Please contact the office for details.",
    "placements": "Our placement cell helps students prepare for interviews and jobs.",
    "hours": "Our office is open from 9 AM to 5 PM, Monday to Saturday.",
    "thanks": "You're welcome! Happy to help.",
    "goodbye": "Goodbye! Have a great day!"
}

# Intent patterns
intents = {
    "greeting": r"\b(hi|hello|hey|good morning|good evening)\b",
    "courses": r"\b(course|courses|python|java|machine learning|web development)\b",
    "fees": r"\b(fee|fees|price|cost)\b",
    "placements": r"\b(placement|placements|job|jobs|career|interview)\b",
    "hours": r"\b(hours|timing|time|open|working hours)\b",
    "thanks": r"\b(thank|thanks)\b",
    "goodbye": r"\b(bye|goodbye|exit|quit)\b"
}


# Function to identify user intent
def get_response(user_input):
    user_input = user_input.lower()

    for intent, pattern in intents.items():
        if re.search(pattern, user_input):
            return responses[intent]

    return "Sorry, I didn't understand. Please ask about courses, fees, placements, or hours."


# Main chatbot function
def chatbot():
    print("=" * 40)
    print("       WELCOME TO AI CHATBOT")
    print("=" * 40)

    print("Ask about courses, fees, placements, or hours.")
    print("Type 'exit' to stop the chatbot.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please enter something.")
            continue

        response = get_response(user_input)

        print("Bot:", response)

        if re.search(intents["goodbye"], user_input.lower()):
            break


# Program execution
if __name__ == "__main__":
    chatbot()
