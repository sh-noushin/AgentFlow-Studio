from typing import Literal, TypedDict

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command
from pydantic import BaseModel


class GraphState(TypedDict):
    question: str
    answer: str


class RouteDecision(BaseModel):
    route: Literal["csharp_agent", "angular_agent"]


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

router_model = model.with_structured_output(
    RouteDecision
)


def supervisor(
    state: GraphState
) -> Command[Literal["csharp_agent", "angular_agent"]]:

    decision = router_model.invoke(
        f"""
        Decide which agent should answer this question.

        Question:
        {state["question"]}
        """
    )

    return Command(
        goto=decision.route
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