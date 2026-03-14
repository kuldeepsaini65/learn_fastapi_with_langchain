from langchain_openai import ChatOpenAI, OpenAI
from langchain_classic.prompts import PromptTemplate
from dotenv import load_dotenv
from openai import RateLimitError

load_dotenv()

question = input("Please ask your Question regarding GK:- ")

template = PromptTemplate(template=""" Suppose yoou are an Gernal Knowlege Teacher. Your role is to Answer the query of the students regarding the gernal knowledge. and if students query is outside of gernal knowledge or question is not in the context of gernal knowledge then you should return one word answer NotAllowed. Student Question : {question} """,
input_variables=['question'], 
validate_template=True
)

template.save('template/gk_template.json')

# t_invoke = template.invoke({
#     'question':question
# })

# model = ChatOpenAI(model='gpt-4.1-mini-2025-04-14', temperature=1.2, max_completion_tokens=10)
# response = model.invoke(t_invoke)
# print(response)
# print('--------')
# print(response.content)


