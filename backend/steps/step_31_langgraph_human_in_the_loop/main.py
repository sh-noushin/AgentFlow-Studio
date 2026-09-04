from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class GraphState(TypedDict):
    action: str
    approved: bool


def ask_for_approval(state: GraphState) -> dict:
    approved = interrupt(
        f"Do you approve this action: {state['action']}?"
    )

    return {
        "approved": approved
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "ask_for_approval",
        ask_for_approval
    )

    graph_builder.add_edge(
        START,
        "ask_for_approval"
    )

    graph_builder.add_edge(
        "ask_for_approval",
        END
    )

    graph = graph_builder.compile(
        checkpointer=InMemorySaver()
    )

    config = {
        "configurable": {
            "thread_id": "conversation-1"
        }
    }

    result = graph.invoke(
        {
            "action": "Cancel order 105",
            "approved": False
        },
        config=config
    )

    print(result["__interrupt__"][0].value)

    user_input = input(
        "Approve? (yes/no): "
    ).strip().lower()

    approved = user_input == "yes"

    result = graph.invoke(
        Command(resume=approved),
        config=config
    )

    print("\nFinal state:")
    print(result)


if __name__ == "__main__":
    main()