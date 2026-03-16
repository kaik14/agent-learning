from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers  import StrOutputParser

model = ChatTongyi(model_name="qwen3-max")

parser = StrOutputParser()

PromptTemplate = PromptTemplate.from_template(
    "我邻居姓:{lastname},他刚生了个{gender},请起名,简单回答:" 
)

chain = PromptTemplate | model | parser

res = chain.invoke(input={"lastname": "王", "gender": "男"})

print(res,type(res))