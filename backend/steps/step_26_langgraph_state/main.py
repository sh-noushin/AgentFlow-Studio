from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    name: str
    greeting: str


def create_greeting(state: GraphState) -> dict:
    return {
        "greeting": f"Hello {state['name']}"
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "create_greeting",
        create_greeting
    )

    graph_builder.add_edge(
        START,
        "create_greeting"
    )

    graph_builder.add_edge(
        "create_greeting",
        END
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "name": "Nooshin",
        "greeting": ""
    })

    print(result)


if __name__ == "__main__":
    main()