from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price based on item price and quantity."""
    return price * quantity


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    agent = create_agent(
        model=model,
        tools=[calculate_total]
    )

    # Send the user request to the agent.
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "I want to buy 4 items. "
                        "Each item costs 19.50 euros. "
                        "What is the total price?"
                    )
                }
            ]
        }
    )

    final_message = result["messages"][-1]

    print(final_message.content)


if __name__ == "__main__":
    main()