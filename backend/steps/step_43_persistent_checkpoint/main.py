#should be installed :python -m pip install langgraph-checkpoint-sqlite


from pathlib import Path
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict, total=False):
    count: int


def increment(state: GraphState) -> dict:
    current_count = state.get("count", 0)

    return {
        "count": current_count + 1
    }


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

    graph_builder.add_edge(
        "increment",
        END
    )

    database_path = Path(__file__).with_name(
        "checkpoints.sqlite"
    )

    config = {
        "configurable": {
            "thread_id": "conversation-1"
        }
    }

    with SqliteSaver.from_conn_string(
        str(database_path)
    ) as checkpointer:

        graph = graph_builder.compile(
            checkpointer=checkpointer
        )

        result = graph.invoke(
            {},
            config=config
        )

        print("Count:")
        print(result["count"])


if __name__ == "__main__":
    main()