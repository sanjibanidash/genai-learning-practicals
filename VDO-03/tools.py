from dotenv import load_dotenv
from langchain.tools import tool
from langchain.messages import HumanMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in the given text."""
    return len(text)


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

llm_with_tools = llm.bind_tools([get_text_length])


# Store the conversation
messages = [
    HumanMessage(
        content="What is the length of the text: Hello, how are you?"
    )
]


# Agent loop
while True:

    # Ask Gemini what to do
    response = llm_with_tools.invoke(messages)

    # Save Gemini's response
    messages.append(response)

    # Check whether Gemini wants to use a tool
    if response.tool_calls:

        # Execute every requested tool
        for tool_call in response.tool_calls:

            print("TOOL CALLED:")
            print(tool_call["name"])

            if tool_call["name"] == "get_text_length":

                tool_result = get_text_length.invoke(
                    tool_call["args"]
                )

                print("TOOL RESULT:")
                print(tool_result)

                # Send tool result back to Gemini
                messages.append(
                    ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
                    )
                )

    else:
        # No more tools needed → final answer
        print("\nFINAL ANSWER:")
        print(response.content)
        break