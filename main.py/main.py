# main.py

import google.generativeai as genai
from agents import health_agent, loop_optimize_meal_plan, math_agent
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def main():
    print("\n🎉 Welcome to the EduHealth Companion!")
    print("Choose a mode:")
    print("1 — Weekly Healthy Meal Plan")
    print("2 — Math Tutor")
    mode = input("\nEnter 1 or 2: ")

    if mode == "1":
        user_request = input("\nDescribe your goals (e.g., 2000 calories, high protein, vegetarian, etc.): ")
        
        print("\n⏳ Generating initial meal plan...")
        base_plan = health_agent(user_request)

        print("\n🔄 Optimizing your plan...")
        optimized = loop_optimize_meal_plan(base_plan)

        print("\n📅 FINAL HEALTHY WEEKLY PLAN:\n")
        print(optimized)

    elif mode == "2":
        question = input("\nWhat math topic or problem do you need help with?\n> ")
        answer = math_agent(question)

        print("\n📘 MATH TUTOR RESPONSE:\n")
        print(answer)

    else:
        print("Invalid option. Please rerun the program.")

if __name__ == "__main__":
    main()
