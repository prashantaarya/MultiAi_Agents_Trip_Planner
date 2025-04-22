# backend/validation.py
from typing import List

def get_valid_input(prompt: str, valid_choices: List[str] = None, input_type: str = "text") -> str:
    """Reusable function to get validated input from user."""
    while True:
        user_input = input(prompt).strip()
        if input_type == "text" and user_input:
            return user_input
        elif input_type == "int" and user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        elif valid_choices and user_input.lower() in [choice.lower() for choice in valid_choices]:
            return user_input.lower()
        else:
            print("⚠️ Invalid input. Please try again.")
