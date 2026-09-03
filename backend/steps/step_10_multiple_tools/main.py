from datetime import date

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price based on item price and quantity."""
    return price * quantity


@tool
def get_order_status(order_id: int) -> str:
    """Get the current status of an order by its ID."""

    orders = {
        101: "Processing",
        102: "Shipped",
        103: "Delivered",
        105: "Cancelled",
    }

    return orders.get(order_id, "Order not found")


@tool
def get_current_date() -> str:
    """Get the current system date."""
    return date.today().isoformat()


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    agent = create_agent(
        model=model,
        tools=[
            calculate_total,
            get_order_status,
            get_current_date,
        ],
        system_prompt=(
            "You are a helpful assistant. "
            "Use the available tools whenever a user request matches a tool."
        ),
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is the status of order 105?"
                }
            ]
        }
    )

    final_message = result["messages"][-1]

    print(final_message.content)


if __name__ == "__main__":
    main()