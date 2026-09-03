
#should be installed : python -m pip install python-dotenv
from dotenv import load_dotenv
from google import genai


def main() -> None:
    load_dotenv()

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents="What is the difference between an LLM and an AI agent? Explain it with a simple example."
    )

    print(response.text)


if __name__ == "__main__":
    main()