from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

model_with_tools = model.bind_tools([multiply])


def call_model(state: MessagesState) -> dict:
    response = model_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


def main() -> None:
    graph_builder = StateGraph(MessagesState)

    graph_builder.add_node(
        "assistant",
        call_model
    )

    graph_builder.add_node(
        "tools",
        ToolNode([multiply])
    )

    graph_builder.add_edge(
        START,
        "assistant"
    )

    graph_builder.add_conditional_edges(
        "assistant",
        tools_condition
    )

    graph_builder.add_edge(
        "tools",
        "assistant"
    )

    graph = graph_builder.compile()

    result = graph.invoke({
        "messages": [
            {
                "role": "user",
                "content": "What is 6 multiplied by 7?"
            }
        ]
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()