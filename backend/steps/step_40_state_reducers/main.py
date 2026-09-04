import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    logs: Annotated[list[str], operator.add]


def first_step(state: GraphState) -> dict:
    return {
        "logs": ["First step completed"]
    }


def second_step(state: GraphState) -> dict:
    return {
        "logs": ["Second step completed"]
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

    result = graph.invoke({
        "logs": []
    })

    print(result["logs"])


if __name__ == "__main__":
    main()