from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    count: int


def increment(state: GraphState) -> dict:
    return {
        "count": state["count"] + 1
    }


def should_continue(state: GraphState) -> str:
    if state["count"] < 3:
        return "continue"

    return "end"


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "increment",
        increment
    )

    graph_builder.add_edge(
        START,
        "increment"
    )

    graph_builder.add_conditional_edges(
        "increment",
        should_continue,
        {
            "continue": "increment",
            "end": END
        }
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "count": 0
    })

    print(result["count"])


if __name__ == "__main__":
    main()