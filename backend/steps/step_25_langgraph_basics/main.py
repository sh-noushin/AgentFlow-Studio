from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    message: str


def greet(state: GraphState) -> GraphState:
    return {
        "message": f"Hello {state['message']}"
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node("greet", greet)

    graph_builder.add_edge(START, "greet")
    graph_builder.add_edge("greet", END)

    graph = graph_builder.compile()

    result = graph.invoke({
        "message": "Nooshin"
    })

    print(result["message"])


if __name__ == "__main__":
    main()