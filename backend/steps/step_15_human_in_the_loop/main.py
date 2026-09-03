from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command


@tool
def cancel_order(order_id: int) -> str:
    """Cancel an order by its ID."""
    return f"Order {order_id} was cancelled."


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    agent = create_agent(
        model=model,
        tools=[cancel_order],
        middleware=[
            HumanInTheLoopMiddleware(
                interrupt_on={
                    "cancel_order": {
                        "allowed_decisions": [
                            "approve",
                            "reject"
                        ]
                    }
                }
            )
        ],
        checkpointer=InMemorySaver(),
        system_prompt=(
            "You are a helpful assistant. "
            "Use the cancel_order tool when the user asks to cancel an order."
        )
    )

    config = {
        "configurable": {
            "thread_id": "conversation-1"
        }
    }

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Cancel order 105."
                }
            ]
        },
        config=config
    )

    if "__interrupt__" in result:
        interrupt = result["__interrupt__"][0]

        action = interrupt.value["action_requests"][0]

        print("\nApproval required")
        print(f"Tool: {action['name']}")
        print(f"Arguments: {action['args']}")

        decision = input(
            "\nApprove this operation? (yes/no): "
        ).strip().lower()

        if decision == "yes":
            result = agent.invoke(
                Command(
                    resume={
                        "decisions": [
                            {
                                "type": "approve"
                            }
                        ]
                    }
                ),
                config=config
            )

        else:
            result = agent.invoke(
                Command(
                    resume={
                        "decisions": [
                            {
                                "type": "reject",
                                "message": "The user rejected the operation."
                            }
                        ]
                    }
                ),
                config=config
            )

    final_message = result["messages"][-1]

    print("\nAgent:")
    print(final_message.content)


if __name__ == "__main__":
    main()