from dotenv import load_dotenv
from google import genai


def main() -> None:
    load_dotenv()

    client = genai.Client()

    chat = client.chats.create(
        model="gemini-3.1-flash-lite"
    )

    print("AgentFlow Studio Chat")
    print("Type 'exit' to close the application.")

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            print("Chat closed.")
            break

        response = chat.send_message(user_message)

        print(f"\nGemini: {response.text}")


if __name__ == "__main__":
    main()