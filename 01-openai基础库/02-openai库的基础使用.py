from openai import OpenAI
# 获取client对象 openai类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 调用模型
response = client.chat.completions.create(
    model="deepseek-v3",
    messages=[
        {"role": "system", "content": "你是python编程专家 说话直接易懂"},
        {"role": "assistant", "content": "我是python编程专家"},
        {"role": "user", "content": "输出一个乘法表"},       
    ],
)

# 处理结果
print(response.choices[0].message.content)