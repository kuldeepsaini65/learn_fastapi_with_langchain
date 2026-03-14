from langchain_classic.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from openai import RateLimitError, APIConnectionError
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()



model = ChatOpenAI(model='gpt-4', temperature=1, max_completion_tokens=50)

chat_template =  ChatPromptTemplate([
    ('system', 'you are a helpfull customer support agent of jio telecome. return cant help if query is byond this. and also return answer in simple text not like AIMessage(content="xxxx") and answer should be  less than 30 words'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('user', '{query}')
])

chat_history = []


user_query = input('Ask me:- ')

with open('chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())


chain = chat_template | model

response = chain.invoke({'chat_history':chat_history, 'query':user_query})

with open('chat_history.txt', 'a') as file:
    file.write(f"HumanMessage(content='{user_query}')\n")
    file.write(f"AIMessage(content='{response.content}')\n")

print(response.content)





