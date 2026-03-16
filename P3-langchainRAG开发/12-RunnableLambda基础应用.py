from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers  import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda


#创建模型
model = ChatTongyi(model_name="qwen3-max")

#定义解析器
parser = StrOutputParser()
json_parser = JsonOutputParser()


First_Prompt = PromptTemplate.from_template(
    "我邻居姓:{lastname},他刚生了个{gender},请起一个名字,并且只需要回答我那个名字就行了" 
)

Second_Prompt = PromptTemplate.from_template(
    "请简单解析这个名字,名字为:{name}"
)

my_func = RunnableLambda(lambda ai_message: ai_message.content)

chain = First_Prompt | model | my_func | Second_Prompt | model | parser

res = chain.stream(input={"lastname": "王", "gender": "男"})

for chunk in res:
    print(chunk, end="", flush=True)

