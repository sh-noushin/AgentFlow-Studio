from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver


@tool
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price based on item price and quantity."""
    return price * quantity


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    checkpointer = InMemorySaver()

    agent = create_agent(
        model=model,
        tools=[calculate_total],
        checkpointer=checkpointer,
        system_prompt="You are a helpful AI assistant."
    )

    config = {
        "configurable": {
            "thread_id": "conversation-1"
        }
    }

    print("AgentFlow Studio")
    print("Type 'exit' to close the application.")

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            print("Chat closed.")
            break

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            },
            config=config
        )

        final_message = result["messages"][-1]

        print(f"\nAgent: {final_message.content}")


if __name__ == "__main__":
    main()