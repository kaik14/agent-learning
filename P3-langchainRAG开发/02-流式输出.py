from langchain_community.llms.tongyi import Tongyi

#qwen3-max是聊天模型 qwen-max是大语言模型
model = Tongyi(model_name="qwen-max")

#调用invoke想模型提问
# res = model.invoke(input="你是谁呀能做什么？") invoke是直接给出回复

res = model.stream(input="你是谁呀能做什么？")

for chunk in res:
    print(chunk, end="", flush=True)

