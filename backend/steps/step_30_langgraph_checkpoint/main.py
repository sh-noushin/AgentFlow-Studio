from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    message: str


def update_message(state: GraphState) -> dict:
    return {
        "message": f"{state['message']} - processed"
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "update_message",
        update_message
    )

    graph_builder.add_edge(
        START,
        "update_message"
    )

    graph_builder.add_edge(
        "update_message",
        END
    )

    checkpointer = InMemorySaver()

    graph = graph_builder.compile(
        checkpointer=checkpointer
    )

    config = {
        "configurable": {
            "thread_id": "conversation-1"
        }
    }

    result = graph.invoke(
        {
            "message": "Hello"
        },
        config=config
    )

    print("Result:")
    print(result)

    saved_state = graph.get_state(config)

    print("\nSaved state:")
    print(saved_state.values)


if __name__ == "__main__":
    main()