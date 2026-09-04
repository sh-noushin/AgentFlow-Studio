from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import Command


class GraphState(TypedDict):
    approved: bool
    status: str


def check_approval(
    state: GraphState
) -> Command[Literal["execute", "reject"]]:

    if state["approved"]:
        return Command(
            update={
                "status": "approved"
            },
            goto="execute"
        )

    return Command(
        update={
            "status": "rejected"
        },
        goto="reject"
    )


def execute(state: GraphState) -> dict:
    return {
        "status": "Action executed"
    }


def reject(state: GraphState) -> dict:
    return {
        "status": "Action rejected"
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "check_approval",
        check_approval
    )

    graph_builder.add_node(
        "execute",
        execute
    )

    graph_builder.add_node(
        "reject",
        reject
    )

    graph_builder.add_edge(
        START,
        "check_approval"
    )

    graph_builder.add_edge(
        "execute",
        END
    )

    graph_builder.add_edge(
        "reject",
        END
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "approved": True,
        "status": ""
    })

    print(result)


if __name__ == "__main__":
    main()