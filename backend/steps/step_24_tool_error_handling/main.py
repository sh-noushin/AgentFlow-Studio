from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def get_order_status(order_id: int) -> str:
    """Get the status of an order."""

    orders = {
        101: "Processing",
        102: "Shipped",
        103: "Delivered"
    }

    if order_id not in orders:
        raise ValueError("Order not found.")

    return orders[order_id]


@wrap_tool_call
def handle_tool_error(request, handler):
    try:
        return handler(request)

    except Exception as error:
        return ToolMessage(
            content=f"Tool error: {error}",
            tool_call_id=request.tool_call["id"]
        )


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    agent = create_agent(
        model=model,
        tools=[get_order_status],
        middleware=[handle_tool_error]
    )

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "What is the status of order 999?"
            }
        ]
    })

    final_message = result["messages"][-1]

    print(final_message.content)


if __name__ == "__main__":
    main()