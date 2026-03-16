from openai import OpenAI
# 获取client对象 openai类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 调用模型
response = client.chat.completions.create(
    model="deepseek-v3",
    messages=[       
        {"role":"system","content":"你是AI助理,回答很简洁"},
        {"role":"user","content":"小明有2条宠物狗"},
        {"role": "assistant","content":"好的"},
        {"role":"user","content":"小红有3只宠物猫"},
        {"role": "assistant","content": "好的"},
        {"role":"user","content":"总共有几个宠物?"}       
    ],
    stream=True
)

# 处理结果
# print(response.choices[0].message.content)

for chunk in response:
    print(
        chunk.choices[0].delta.content, 
        end="",   #每一段之间以空格分格
        flush=True #立刻刷新缓冲区
    )