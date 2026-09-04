from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    name: str
    message: str


def create_greeting(state: GraphState) -> dict:
    return {
        "message": f"Hello {state['name']}"
    }


def add_welcome_message(state: GraphState) -> dict:
    return {
        "message": f"{state['message']}! Welcome to AgentFlow Studio."
    }


def create_greeting_subgraph():
    subgraph_builder = StateGraph(GraphState)

    subgraph_builder.add_node(
        "create_greeting",
        create_greeting
    )

    subgraph_builder.add_edge(
        START,
        "create_greeting"
    )

    subgraph_builder.add_edge(
        "create_greeting",
        END
    )

    return subgraph_builder.compile()


def main() -> None:
    greeting_subgraph = create_greeting_subgraph()

    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "greeting_subgraph",
        greeting_subgraph
    )

    graph_builder.add_node(
        "add_welcome_message",
        add_welcome_message
    )

    graph_builder.add_edge(
        START,
        "greeting_subgraph"
    )

    graph_builder.add_edge(
        "greeting_subgraph",
        "add_welcome_message"
    )

    graph_builder.add_edge(
        "add_welcome_message",
        END
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "name": "Nooshin",
        "message": ""
    })

    print(result["message"])


if __name__ == "__main__":
    main()