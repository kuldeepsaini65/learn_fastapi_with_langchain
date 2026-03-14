from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from openai import APIConnectionError

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Chat history stored globally
chats = [
    SystemMessage(content="Answer in less words. Only return necessary words.")
]


def ask_ai(question):
    global chats

    chats.append(HumanMessage(content=question))

    try:
        result = model.invoke(chats)

        chats.append(AIMessage(content=result.content))

        print(result.content)
        print('--------\n')
        print(chats)

    except APIConnectionError:
        print('Check your internet connection')


while True:
    user_input = input("Ask Me :- ")

    if user_input.lower() in ["exit", "quit"]:
        break

    ask_ai(user_input)