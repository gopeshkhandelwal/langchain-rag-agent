
from langchain.agents import initialize_agent, AgentType
from agent_app.rag import DocumentQA
from agent_app.weather import CityWeather
from agent_app.config import get_llm

llm = get_llm()

agent = initialize_agent(
    tools=[DocumentQA, CityWeather],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=5,
    agent_kwargs={
        "prefix": (
            "You are an AI assistant with access to two tools: DocumentQA and CityWeather.\n"
            "Use tools only if the question is clearly about internal documents or current weather.\n"
            "If the query is vague, general, or unrelated, DO NOT use any tools.\n\n"
            "Here is an example to follow:\n\n"
            "Question: What is the weather in New York?\n"
            "Thought: This is a weather-related question. I should use the CityWeather tool.\n"
            "Action: CityWeather\n"
            "Action Input: New York\n"
            "Observation: The weather in New York is sunny with a temperature of 25°C.\n"
            "Final Answer: The weather in New York is sunny and 25°C.\n\n"
            "Now begin for the user's input."
        ),
        "format_instructions": """Use this format:

Question: the user query
Thought: reason about what to do
Action: one of [DocumentQA, CityWeather] (optional)
Action Input: the input to the tool (optional)
Observation: result of the tool (only if Action was used)
Final Answer: the response to the user

Only use plain text in Action and Action Input — no code, no parentheses, no function calls.

If no tool is needed, skip Action and Observation and go directly to Final Answer.
""".strip()
    }
)

if __name__ == "__main__":
    print("\n🧠 Agentic AI is ready. Type your query or 'quit' to exit.\n")
    while True:
        user_input = input("📝 Your Query: ")
        if user_input.strip().lower() in ["quit", "exit"]:
            print("👋 Exiting. Goodbye!")
            break
        try:
            response = agent.invoke(user_input)
            print("\n✅ Final Answer:", response, "\n")
        except Exception as e:
            print(f"⚠️ Error processing query: {e}\n")
