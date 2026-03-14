from langchain_openai import ChatOpenAI
from langchain_classic.prompts import load_prompt
from dotenv import load_dotenv

load_dotenv()


question = 'my name is kuldeep'

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

template = load_prompt('template/gk_template.json')


chain = template | model
result = chain.invoke({'question':question})
print(result, '\n\n------\n\n')
print(result.content)