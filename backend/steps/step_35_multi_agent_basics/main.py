from typing import TypedDict

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    question: str
    route: str
    answer: str


def choose_agent(state: GraphState) -> dict:
    question = state["question"].lower()

    if "angular" in question:
        return {
            "route": "angular"
        }

    return {
        "route": "csharp"
    }


def route_to_agent(state: GraphState) -> str:
    return state["route"]


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    csharp_agent = create_agent(
        model=model,
        tools=[],
        system_prompt="You are a senior C# developer."
    )

    angular_agent = create_agent(
        model=model,
        tools=[],
        system_prompt="You are a senior Angular developer."
    )

    def call_csharp_agent(state: GraphState) -> dict:
        result = csharp_agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": state["question"]
                }
            ]
        })

        return {
            "answer": result["messages"][-1].content
        }

    def call_angular_agent(state: GraphState) -> dict:
        result = angular_agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": state["question"]
                }
            ]
        })

        return {
            "answer": result["messages"][-1].content
        }

    graph_builder = StateGraph(GraphState)

    graph_builder.add_node(
        "choose_agent",
        choose_agent
    )

    graph_builder.add_node(
        "csharp_agent",
        call_csharp_agent
    )

    graph_builder.add_node(
        "angular_agent",
        call_angular_agent
    )

    graph_builder.add_edge(
        START,
        "choose_agent"
    )

    graph_builder.add_conditional_edges(
        "choose_agent",
        route_to_agent,
        {
            "csharp": "csharp_agent",
            "angular": "angular_agent"
        }
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
        "question": "What is dependency injection in C#?",
        "route": "",
        "answer": ""
    })

    print(result["answer"])


if __name__ == "__main__":
    main()