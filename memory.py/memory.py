# memory.py

class StudentMemory:
    """
    Simple in-memory storage for tracking math weaknesses
    and previously learned topics.
    """
    def __init__(self):
        self.memory = {
            "weak_topics": [],
            "past_questions": []
        }

    def add_weak_topic(self, topic):
        if topic not in self.memory["weak_topics"]:
            self.memory["weak_topics"].append(topic)

    def add_question(self, question):
        self.memory["past_questions"].append(question)

    def get_memory(self):
        return self.memory
