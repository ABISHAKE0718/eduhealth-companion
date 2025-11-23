# agents.py

import google.generativeai as genai
from tools import google_search
from memory import StudentMemory

memory = StudentMemory()

# -------------------------------
# HEALTH MEAL PLANNER AGENT
# -------------------------------
def health_agent(user_input):
    """
    Generates a healthy weekly menu plan.
    Uses: Google search + Gemini
    """
    search_results = google_search("healthy weekly meal plan nutrition")
    
    prompt = f"""
    You are a health planning agent.
    User request: {user_input}
    
    Search results for nutrition guidelines:
    {search_results}
    
    Create a 7-day healthy meal plan.
    Include breakfast, lunch, dinner.
    Include a clean ingredients list.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text


# -------------------------------
# LOOP AGENT FOR MEAL OPTIMIZATION
# -------------------------------
def loop_optimize_meal_plan(initial_plan):
    """
    Simple loop agent to refine the plan.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")

    for i in range(2):  # loop two times for refinement
        prompt = f"""
        Improve this meal plan. Make it healthier, more balanced, 
        and ensure calorie targets are realistic:
        {initial_plan}
        """
        result = model.generate_content(prompt)
        initial_plan = result.text

    return initial_plan


# -------------------------------
# MATH TUTOR AGENT
# -------------------------------
def math_agent(user_input):
    """
    Helps students learn math with personalized feedback.
    """
    model = genai.GenerativeModel("gemini-1.5-pro")

    # Apply prior memory
    past = memory.get_memory()

    prompt = f"""
    You are a friendly math tutor.
    User question: {user_input}

    Student weaknesses:
    {past["weak_topics"]}

    Give step-by-step explanations.
    After solving, suggest next related topics.
    """

    response = model.generate_content(prompt)

    # Add user question to memory
    memory.add_question(user_input)

    # Simple weakness detection (very basic)
    if any(word in user_input.lower() for word in ["fraction", "divide", "division"]):
        memory.add_weak_topic("fractions")

    return response.text
