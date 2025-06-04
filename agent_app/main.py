
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
    handle_parsing_errors=True,  # ✅ Prevent output format issues
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
        "format_instructions": """
Use this format:

Question: user query
Thought: your reasoning
Action: one of [DocumentQA, CityWeather]
Action Input: plain input to the tool
Observation: result from the tool
Final Answer: the final user-facing response

Only use Action if necessary. DO NOT write tool calls like DocumentQA(question: ...). Just write:
Action: DocumentQA
Action Input: Intel Tiber AI Cloud
""".strip()
    }
)

# === Prompt Loop ===
if __name__ == "__main__":
    print("\n🧠 Agentic AI is ready. Type your query or 'quit' to exit.\n")

    while True:
        user_input = input("📝 Your Query: ")
        if user_input.strip().lower() in ["quit", "exit"]:
            print("👋 Exiting. Goodbye!")
            break
        try:
            response = agent.invoke(user_input)
            print("\n✅", response, "\n")
        except Exception as e:
            print(f"⚠️ Error processing query: {e}\n")
