from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers  import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

#创建模型
model = ChatTongyi(model_name="qwen3-max")

#定义解析器
parser = StrOutputParser()
json_parser = JsonOutputParser()


First_Prompt = PromptTemplate.from_template(
    "我邻居姓:{lastname},他刚生了个{gender},请起名,请用封装为json格式返回,key为name,value为起的名字:" 
)

Second_Prompt = PromptTemplate.from_template(
    "请简单解析这个名字,名字为:{name}"
)

chain = First_Prompt | model | parser | Second_Prompt | model | parser

res = chain.stream(input={"lastname": "王", "gender": "男"})

for chunk in res:
    print(chunk, end="", flush=True)

