from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessageChunk
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
        tools=[calculate_total],
        system_prompt="You are a helpful AI assistant."
    )

    for chunk in agent.stream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "I want to buy 4 items. "
                        "Each item costs 19.50 euros. "
                        "Calculate the total and explain the result."
                    )
                }
            ]
        },
        stream_mode="messages",
        version="v2",
    ):
        if chunk["type"] == "messages":
            token, metadata = chunk["data"]

            if isinstance(token, AIMessageChunk) and token.text:
                print(token.text, end="", flush=True)

    print()


if __name__ == "__main__":
    main()