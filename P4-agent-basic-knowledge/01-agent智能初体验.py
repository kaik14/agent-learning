from langchain.agents import create_agent
from langchain_community.chat_models import ChatTongyi
from langchain.tools import tool


@tool(description = "查询天气")
def get_weather() -> str:
    return "晴天"


agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],
    system_prompt="你是一个聊天助手，可以回答用户问题。"
)

res = agent.invoke(
    {
        "messages":[
            {"role":"user","content":"明天吉隆坡的天气怎么样？"}
        ]
    }
)

for msg in res["messages"]:
    print(msg.content)
    print(type(msg))#是ai消息对象
    # print(msg["content"])