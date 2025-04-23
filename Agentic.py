class SimpleAIAgent:
    def __init__(self, name="AIAgent"):
        self.name = name
        self.knowledge_base = {
            "hello": "Hello! How can I help you today?",
            "hi": "Hi there! What can I do for you?",
            "how are you": "I'm just code, but I'm doing great!",
            "what is your name": f"My name is {self.name}.",
            "bye": "Goodbye! Have a great day!"
        }

    def respond(self, message):
        message = message.lower().strip()
        for key in self.knowledge_base:
            if key in message:
                return self.knowledge_base[key]
        return "I'm not sure how to respond to that."

# Example usage
if __name__ == "__main__":
    agent = SimpleAIAgent("HelperBot")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break
        response = agent.respond(user_input)
        print(f"Agent: {response}")
