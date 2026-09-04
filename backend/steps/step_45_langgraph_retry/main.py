from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy


class GraphState(TypedDict):
    result: str


attempt = 0


def unstable_node(state: GraphState) -> dict:
    global attempt

    attempt += 1

    print(f"Attempt: {attempt}")

    if attempt < 3:
        raise RuntimeError("Temporary error")

    return {
        "result": "Success"
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "unstable_node",
        unstable_node,
        retry_policy=RetryPolicy(
            max_attempts=3,
            retry_on=RuntimeError
        )
    )

    graph_builder.add_edge(
        START,
        "unstable_node"
    )

    graph_builder.add_edge(
        "unstable_node",
        END
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "result": ""
    })

    print("\nFinal result:")
    print(result["result"])


if __name__ == "__main__":
    main()