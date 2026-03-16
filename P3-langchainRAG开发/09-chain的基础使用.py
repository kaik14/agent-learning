from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

# 1. 定义聊天提示词模板
# 使用 MessagesPlaceholder 来占位，以便后续动态插入对话历史 (history)
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗"),
    ]
)

# 2. 准备模拟的对话历史数据
history_data = [
    ("human", "你来写一个唐诗"),
    ("ai", "床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human", "好诗再来一个"),
    ("ai", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
]

# 3. 将历史数据注入模板，并转换成字符串格式
# invoke 会将 history_data 插入到占位符中
model = ChatTongyi(model="qwen3-max")
   
# 4. 初始化通义千问模型
# 注意：这里使用的是 qwen3-max 模型
chain = chat_prompt_template | model

# 5. 调用模型并获取结果
# res = chain.invoke(({"history": history_data}))
res = chain.stream(({"history": history_data}))

for chunk in res:
    print(chunk.content, end="", flush=True)


# # 6. 打印模型回复的内容以及返回对象的类型
# print(res.content, type(res))