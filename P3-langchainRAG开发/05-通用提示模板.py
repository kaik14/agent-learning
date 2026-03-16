from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model_name="qwen-max")

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字,简单回答"
)

# prompt_text = prompt_template.format(lastname="王", gender="男")

# res = model.invoke(input=prompt_text)

# print(res)

chain = prompt_template | model #chain写法

res = chain.invoke(input={"lastname": "王", "gender": "男"})

print(res)