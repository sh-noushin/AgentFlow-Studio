from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    message: str


def first_step(state: GraphState) -> dict:
    return {
        "message": state["message"] + " -> first"
    }


def second_step(state: GraphState) -> dict:
    return {
        "message": state["message"] + " -> second"
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "first_step",
        first_step
    )

    graph_builder.add_node(
        "second_step",
        second_step
    )

    graph_builder.add_edge(
        START,
        "first_step"
    )

    graph_builder.add_edge(
        "first_step",
        "second_step"
    )

    graph_builder.add_edge(
        "second_step",
        END
    )

    graph = graph_builder.compile()

    mermaid = graph.get_graph().draw_mermaid()

    print(mermaid)


if __name__ == "__main__":
    main()