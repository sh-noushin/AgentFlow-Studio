from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import Command


class GraphState(TypedDict):
    question: str
    answer: str


def supervisor(
    state: GraphState
) -> Command[Literal["csharp_agent", "angular_agent"]]:

    question = state["question"].lower()

    if "angular" in question:
        return Command(
            goto="angular_agent"
        )

    return Command(
        goto="csharp_agent"
    )


def csharp_agent(state: GraphState) -> dict:
    return {
        "answer": "The C# agent received the question."
    }


def angular_agent(state: GraphState) -> dict:
    return {
        "answer": "The Angular agent received the question."
    }


def main() -> None:
    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "supervisor",
        supervisor
    )

    graph_builder.add_node(
        "csharp_agent",
        csharp_agent
    )

    graph_builder.add_node(
        "angular_agent",
        angular_agent
    )

    graph_builder.add_edge(
        START,
        "supervisor"
    )

    graph_builder.add_edge(
        "csharp_agent",
        END
    )

    graph_builder.add_edge(
        "angular_agent",
        END
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "question": "What are signals in Angular?",
        "answer": ""
    })

    print(result["answer"])


if __name__ == "__main__":
    main()