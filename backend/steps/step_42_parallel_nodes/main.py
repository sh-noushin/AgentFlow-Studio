from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    number: int
    doubled: int
    squared: int
    result: str


def double_number(state: GraphState) -> dict:
    return {
        "doubled": state["number"] * 2
    }


def square_number(state: GraphState) -> dict:
    return {
        "squared": state["number"] * state["number"]
    }


def combine_results(state: GraphState) -> dict:
    return {
        "result": (
            f"Doubled: {state['doubled']}, "
            f"Squared: {state['squared']}"
        )
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "double_number",
        double_number
    )

    graph_builder.add_node(
        "square_number",
        square_number
    )

    graph_builder.add_node(
        "combine_results",
        combine_results
    )

    graph_builder.add_edge(
        START,
        "double_number"
    )

    graph_builder.add_edge(
        START,
        "square_number"
    )

    graph_builder.add_edge(
        ["double_number", "square_number"],
        "combine_results"
    )

    graph_builder.add_edge(
        "combine_results",
        END
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "number": 5,
        "doubled": 0,
        "squared": 0,
        "result": ""
    })

    print(result["result"])


if __name__ == "__main__":
    main()