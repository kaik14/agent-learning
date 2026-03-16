from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

#得到模型对象 
model = ChatTongyi(model_name="qwen3-max")

message = [

    #普通写法
    # SystemMessage(content="你是一个边塞诗人"),#系统设定
    # HumanMessage(content="写一首唐诗"),#用户消息
    # AIMessage(content="锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),#ai回复消息
    # HumanMessage(content="按照你上一个回复的格式写一首古诗")

    #简写写法 元组   这样子写的话就可以把import的第二个message导包不用了
    ("system","你是一个边塞诗人"),#系统设定
    ("human","写一首唐诗"),#用户消息
    ("ai","锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),#ai回复消息
    ("human","按照你上一个回复的格式写一首古诗")

]

res = model.stream(input=message)   #流式输出

for chunk in res:
    print(chunk.content, end="", flush=True)