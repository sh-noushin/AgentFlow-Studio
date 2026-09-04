from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    name: str
    greeting: str
    final_message: str


def create_greeting(state: GraphState) -> dict:
    return {
        "greeting": f"Hello {state['name']}"
    }


def create_final_message(state: GraphState) -> dict:
    return {
        "final_message": f"{state['greeting']}! Welcome to LangGraph."
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "create_greeting",
        create_greeting
    )

    graph_builder.add_node(
        "create_final_message",
        create_final_message
    )

    graph_builder.add_edge(
        START,
        "create_greeting"
    )

    graph_builder.add_edge(
        "create_greeting",
        "create_final_message"
    )

    graph_builder.add_edge(
        "create_final_message",
        END
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "name": "Nooshin",
        "greeting": "",
        "final_message": ""
    })

    print(result["final_message"])


if __name__ == "__main__":
    main()