from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    score: int
    result: str


def check_score(state: GraphState) -> dict:
    return {}


def choose_route(state: GraphState) -> str:
    if state["score"] >= 60:
        return "pass"

    return "fail"


def passed(state: GraphState) -> dict:
    return {
        "result": "You passed."
    }


def failed(state: GraphState) -> dict:
    return {
        "result": "You failed."
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node("check_score", check_score)
    graph_builder.add_node("passed", passed)
    graph_builder.add_node("failed", failed)

    graph_builder.add_edge(
        START,
        "check_score"
    )

    graph_builder.add_conditional_edges(
        "check_score",
        choose_route,
        {
            "pass": "passed",
            "fail": "failed"
        }
    )

    graph_builder.add_edge("passed", END)
    graph_builder.add_edge("failed", END)

    graph = graph_builder.compile()

    result = graph.invoke({
        "score": 75,
        "result": ""
    })

    print(result["result"])


if __name__ == "__main__":
    main()